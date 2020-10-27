from flask import Flask, render_template, request
import subprocess #シェルスクリプト起動やコマンド実行用
import numpy as np
import cv2, time, json, base64, requests
 
app = Flask(__name__)
 
@app.route('/')
def index():
    message = 'Test for connection!!'
    return message
 
 
#ajaxで使用

@app.route('/control', methods=['POST'])
def control():
    """
    WEB APP側から写真撮影依頼を送信
    → 
    [RP]写真撮影：take_image()
    →
    [RP]:人がいるのか検知する？
    →
    [RP]: send_imageでWEB APP側に画像送信
    """
    param1 = request.form['param1']
    param2 = request.form['param2']
　　
    cmd = param1 + ' ' + param2
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout_data,stderr_data = p.communicate()
    res = stdout_data
    image = take_image()
    send_image(image, destination_url="http://localhost:8080/save")

    return res


def take_image():
    # take an image
    img = None
    return img

def send_image(img, destination_url):
  # 画像を送信可能な形式に変換してJSONに格納
  _, encimg = cv2.imencode(".png", img)
  img_str = encimg.tostring()
  img_byte = base64.b64encode(img_str).decode("utf-8")
  img_json = json.dumps({'image': img_byte}).encode('utf-8')

  # HTTPリクエストを送信
  response = requests.post(destination_url, data=img_json)
  print('{0} {1}'.format(response.status_code, json.loads(response.text)["message"]))
 
if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.31', port=8080)