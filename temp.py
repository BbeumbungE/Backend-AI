import json
from boto3 import client
from botocore.exceptions import NoCredentialsError
from fastapi import FastAPI, File, UploadFile
from aio_pika import connect, IncomingMessage, Message
from dotenv import load_dotenv
import os
import tensorflow as tf
import tensorflow_addons as tfa
from models import Residual_Block, Pix2Pix_Generator
from utils import preprocess_edge, postprocess_result
import numpy as np
import cv2
from PIL import Image
import requests
import io
from io import BytesIO
import time

# 이미지 URL
image_url = "https://aicanvas-mw.s3.ap-northeast-2.amazonaws.com/item/avatar/crocodile.png"

# 이미지를 가져옵니다.
response = requests.get(image_url)

# # bmw generator
# bmw_generator = Pix2Pix_Generator(input_channels=1, output_channels=3, name=f"bmw_generator")
# bmw_ckpt = tf.train.Checkpoint(generator=bmw_generator)
# bmw_ckpt.restore("./checkpoints/bmw/ckpt-1")  # trained for 19 epoches (with batch_size = 4) using 11476 images

# # 응답이 성공인지 확인합니다.
# if response.status_code == 200:

#     sketch = Image.open(io.BytesIO(response.content))
#     sketch = sketch.convert('L')
#     sketch = np.array(sketch)
#     sketch = np.expand_dims(sketch, axis=-1)
#     sketch = preprocess_edge(sketch)

#     result = bmw_generator(sketch)
#     result = postprocess_result(result)
    
# else:
#     print("Failed to retrieve the image.")

# print(time.time())
# print(int(time.time()))


import random
tmp_list = list(range(1, 101))
random.shuffle(tmp_list)
print(tmp_list)
