# rasPi_products

https://github.com/pallets/flask/blob/1.1.2/examples/tutorial/flaskr/　flaskのチュートリアルを元に、rasberry Piで定期的に撮影する画像を 別PCで立ち上げている flask applicationに送信するアプリ。

将来的に画像解析を実施し、自分の姿勢が猫背になっていないか監視するアプリケーションを作成する予定。



raspberry pi側
---
raspberry pi側はtake_shot.py及び以下のコマンドをcron実行して画像を送信する。
```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/pi/Desktop/image.jpg" <ip-address>:5000/send_image
```


ネタリスト

- ひたすらn度寝してしまうので、布団に横たわっている場合叱咤してくれる目覚ましを作りたい。


### LINEで

ひたすらn度寝してしまうので、布団に横たわっている場合叱咤してくれる目覚ましを作りたい。
    - コミットメントとして、家族・友人に二度寝状況を伝えるだけのBOTを作ってみる。

    - heroku の使い方を学ぶ
        - `git push heroku master`でheroku serverにPUSHするとデプロイしてくれる。 https://qiita.com/sayama0402/items/e2c9e65786259dc55e11