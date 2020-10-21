import argparse
# __init__ファイル内の関数は,相対参照している。より良い方法があるか？...
# from . import create_app
# from flask_socketio import SocketIO, emit, join_room, leave_room, \
#       close_room, rooms, disconnect

app = create_app()
# import os
# app = create_app(os.getenv('FLASK_CONFIGURE_MODE'))

# 非同期処理に使用するライブラリの指定
# `threading`, `eventlet`, `gevent`から選択可能
# async_mode = None
# socketio = SocketIO(app, async_mode=async_mode)


# スレッドを格納するためのグローバル変数
thread = None
# 以下何らかの処理
# create_appが見つかり次第実行される。
# app.pyでrunコマンドが実行されるタイミングで制御を行える？


# @socketio.on('connect', namespace='/test')
# def test_connect():
#     global thread
#     if thread is None:
#         thread = socketio.start_background_task(target=background_thread)
#     emit('my response', {'data': 'Connected', 'count': 0})

if __name__ == '__main__':
    # socketio.run(app, debug=True)
    # herokuが引数を
    print(" what is default parameters")
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=int(os.environ.get('PORT', 8000)), help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    arg_parser.add_argument('--host', default='0.0.0.0', help='host')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, host=options.host, port=options.port)