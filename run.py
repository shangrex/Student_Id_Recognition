import os
import sys
import json
import numpy as np
import time
from PIL import Image, ImageDraw
import skimage

sys.path.append('Mask_RCNN/') 
from mrcnn.config import Config
import mrcnn.utils as utils
from mrcnn import visualize
import mrcnn.model as modellib

from config import InferenceConfig


# initialize
inference_config = InferenceConfig()

# Recreate the model in inference mode
model = modellib.MaskRCNN(mode="inference", config=inference_config, model_dir='model')
model_path = 'model/mask_rcnn_id_0010.h5'

# Load trained weights (fill in path to trained weights here)
print("Loading weights from ", model_path)
model.load_weights(model_path, by_name=True)

def predict_img(image_path):
    # image_path = '/Users/oscar/Downloads/134953936_777470856176430_4857825600277326723_n.jpg'
    img = skimage.io.imread(image_path)
    img_arr = np.array(img)
    results = model.detect([img_arr], verbose=1)
    r = results[0]

    print(f'rois: ' + str(r['rois']) + '\n\nclass_ids: ' + str(r['class_ids']))
    print(f'image path: {image_path}')

    visualize.display_instances(img, r['rois'], r['masks'], r['class_ids'], ['BG', 'name', 'pic', 's', 'card'], r['scores'], figsize=(5,5))

    return {'rois': r['rois'], 'class_ids': r['class_ids']}