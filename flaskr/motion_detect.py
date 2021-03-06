# -*- coding: utf-8 -*-

from flask import Blueprint, current_app
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

import json

# from flaskr.auth import login_required
# from flaskr.db import get_db
import os
# import yaml

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn)

from io import BytesIO
# from PIL import Image, ImageOps
import requests

# API
bp = Blueprint("motion_detection", __name__)


# global variableに睡眠状態持たせておく。
# やりたいことは、友達・家族からLINEで寝ているか？確認する文言が発話されたら、
# 私が寝室でゴロゴロしているかどうかをraspberry Piで検知→その結果をbotに発話させることである。
# （もっといい方法があるはず。友達・家族からの発話を踏まえてrasberryPiで検知が走るようにしたい。）
# とりあえずまず作ってみる。
# まずは、LINE botを作成してみる。https://qiita.com/kotamatsuoka/items/c4e651f1cb6c4490f4b8

is_sleep = False


LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@bp.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']

    logger = current_app.logger
    body = request.get_data(as_text=True)
    logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def response_message(event):
    # import pdb; pdb.set_trace()
    print(event)
    # notesのCarouselColumnの各値は、変更してもらって結構です。
    notes = [CarouselColumn(thumbnail_image_url="https://cdn-ak.f.st-hatena.com/images/fotolife/m/mon3221/20171209/20171209094534.png",
                            title="寝坊確認",
                            text="田久保が寝ているかどうかを人感センサーで感知します。",
                            # actions=[{"type": "message","label": "サイトURL","text": "https://renttle.jp/notes/kota/7"}]
                            ),

             CarouselColumn(thumbnail_image_url="https://renttle.jp/static/img/renttle03.jpg",
                            title="ReleaseNote】創作中の活動を報告する機能を追加しました。",
                            text="創作中や考え中の時点の活動を共有できる機能を追加しました。",
                            actions=[
                                {"type": "message", "label": "サイトURL", "text": "https://renttle.jp/notes/kota/6"}]),

             CarouselColumn(thumbnail_image_url="https://renttle.jp/static/img/renttle04.jpg",
                            title="【ReleaseNote】タグ機能を追加しました。",
                            text="「イベントを作成」「記事を投稿」「本を登録」にタグ機能を追加しました。",
                            actions=[
                                {"type": "message", "label": "サイトURL", "text": "https://renttle.jp/notes/kota/5"}])]

    messages = TemplateSendMessage(
        alt_text='template',
        template=CarouselTemplate(columns=notes),
    )

    line_bot_api.reply_message(event.reply_token, messages=messages)

@bp.route("/ask_motion", methods=["GET"]) 
def ask_motion():
    """
    raspberry pi側に立てたflask serverに対し、人感センサーを動かし、人間がいるかいなかを検知させる。
    30秒間確認し、検知できた場合、「1」を返す。
    """
    # import pdb; pdb.set_trace()
    # curl -X POST -H "Content-Type: application/json" -d '{"is_sleeping":0}' localhost:5000/motion_detect
    res = requests.get(f'http://{os.environ["My_Raspberry_PI_IP_ADDRESS"]}:9999/motion_detect')
    
    return res.text

@bp.route("/receive_motion", methods=["POST"]) 
def receive_motion():
    # import pdb; pdb.set_trace()
    # curl -X POST -H "Content-Type: application/json" -d '{"is_sleeping":0}' localhost:5000/motion_detect
    data_dict = json.loads(request.data.decode("utf-8"))
    # https://teratail.com/questions/222843
    still_sleeping = data_dict["is_sleeping"]
    if still_sleeping==1:
        is_sleep = True
    return "Okay I understand that he is sleeping!" if still_sleeping else ""

