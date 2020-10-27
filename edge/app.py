from flask import Flask, render_template, request
 

 
import subprocess #シェルスクリプト起動やコマンド実行用
 
 
app = Flask(__name__)
 
@app.route('/')
def index(title='Helllo!'):
    message = 'World!!'
    return render_template('index.html',title=title,message=message)
 
 
#ajaxで使用
@app.route('/control', methods=['POST'])
def control():
 
    param1 = request.form['param1'];
    param2 = request.form['param2'];
　　
    cmd = param1 + ' ' + param2
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout_data,stderr_data = p.communicate()
    res = stdout_data
 
    return res
 
if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.31', port=8080)