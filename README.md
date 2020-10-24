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

        【ひたすら503エラーを履いてくる。】
        →デプロイの段階でサーバエラー履いていることが予想される。
        - herokuに渡したconfig情報を渡せていない。
        - line-bot-sdkモジュールをrequirement.txtに入れないとダメかもしれない。

        - ホスト環境汚れていることに起因するかもなので環境整えて、docker上でもう一回やり直したほうがいいかもしれない。
        https://nokt2018.hatenablog.com/entry/2018/09/29/030557

        - ERRORの出どころ理解した。
            まず、Procfileの書き忘れだった。
            次に依存モジュールのnot found

            - PORTの指定[`${PORT}`heroku側で指定しているポート番号を利用する。]
            相対参照は、モジュール化してしまうと🆖になる。
            application server uWSGI経由で無いと、localhost限定でサーバが立ち上がってしまう（DEV環境？）
        
        10/22
        残ったエラーは全て、Flask内部の処理を理解すれば解決するものなので、一旦ここで作業中断。

        https://qiita.com/rebi/items/efd1c36f0a9e46222d80
        に基づいて、LINE上にMSGを送信することが出来ました！

        LINE APIの仕様の問題なのか、「ごめんなさい」文がいまだ表示されてしまう問題が依然発生しています。。

        