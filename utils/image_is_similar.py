import base64
import urllib.request
import cv2
import os

def is_similar(src, local):
    os.environ["OPENCV_LOG_LEVEL"] = "ERROR"
    filename = "temp.png"
    if src.startswith("data:image"):
        header, encoded = src.split(",", 1)
        image_data = base64.b64decode(encoded)
        with open(filename, "wb") as f:
            f.write(image_data)
    else:
        urllib.request.urlretrieve(src, filename)
    img_src = cv2.imread(filename)
    img_local = cv2.imread(local)
    if img_src is None or img_local is None:
        if os.path.exists(filename):
            os.remove(filename)
        raise ValueError("이미지를 읽을 수 없습니다.")
    hist_src = cv2.calcHist([cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
    hist_local = cv2.calcHist([cv2.cvtColor(img_local, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
    try:
        result = cv2.matchTemplate(img_src, img_local, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
    except cv2.error:
        max_val = 0
    os.remove(filename)
    hist_similarity = cv2.compareHist(hist_src, hist_local, cv2.HISTCMP_CORREL)
    if hist_similarity > 0.9 or max_val > 0.9:
        return True
    return False