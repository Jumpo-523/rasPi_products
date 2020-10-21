
# __init__ファイル内の関数は,相対参照している。より良い方法があるか？...
from . import create_app
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
    app.run(debug=True)