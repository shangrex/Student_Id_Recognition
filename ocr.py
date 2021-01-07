import cv2
import re
import pytesseract
import PIL
from cnocr import CnOcr
import  mxnet  as  mx

import matplotlib.pyplot as plt

def text_reg(img_path, rois, class_ids):
    # img = cv2.imread(image_path)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    index = list(class_ids).index(3)
    pos = list(rois)[index]

    s_id = img[pos[0]:pos[2], (pos[1] - 30):pos[3]]

    # print(f'size: {img.shape}')

    s = pytesseract.image_to_string(s_id)
    # print(s)

    word1 = "".join(re.findall("[a-zA-Z0-9]*", s))
    print(word1[-9:])

    ocr  = CnOcr()

    # [ 644  894  804 1287]

    index = list(class_ids).index(1)
    pos = list(rois)[index]

    name = img[pos[0]:pos[2], (pos[1] - 30):pos[3]]

    plt.imshow(name)
    plt.show()

    img = mx.nd.array(name)
    res  = ocr.ocr(name)
    print( "姓名:" , res)