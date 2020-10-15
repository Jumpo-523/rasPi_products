from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

from io import BytesIO
from PIL import Image, ImageOps
import requests

# API
bp = Blueprint("api", __name__)


@bp.route("/send_image", methods=["POST"]) 
def send_image():
    # curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/pi/Desktop/image.jpg" 100.64.1.11:5000/send_image
    # 上記コマンドでraspberry piから送信
    # https://stackoverflow.com/questions/47515243/reading-image-file-file-storage-object-using-cv2
    # read methodが必要
    image = request.files["file"].read()
    # https://teratail.com/questions/222843
    img = Image.open(BytesIO(image))
    # flipped_img = ImageOps.flip(img)
    # flipped_img.save("image.jpg")
    img.save("image.jpg")
    return "image received!"



# https://pythonhosted.org/RPIO/rpio_py.html#gpio-input-output
# GPIOのmoduleの中身を理解するためのdocumentation
# 、grove Piを経由せずにsensordataを音センサー（SEN02281P）から取得してボットを作成している。
# http://dotnsf.blog.jp/archives/1052664142.html 



