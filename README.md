# rasPi_products

https://github.com/pallets/flask/blob/1.1.2/examples/tutorial/flaskr/　flaskのチュートリアルを元に、rasberry Piで定期的に撮影する画像を 別PCで立ち上げている flask applicationに送信するアプリ。

将来的に画像解析を実施し、自分の姿勢が猫背になっていないか監視するアプリケーションを作成する予定。


raspberry pi側はtake_shot.py及び以下のコマンドをcron実行して画像を送信する。
```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/pi/Desktop/image.jpg" <ip-address>:5000/send_image
```
