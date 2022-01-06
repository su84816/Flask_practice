from flask import Flask , render_template
from flask import request, redirect, url_for
# from flask_ngrok import run_with_ngrok

app = Flask(__name__) #代表目前執行的模組
# run_with_ngrok(app)

@app.route("/") #函式的裝飾:以函示為基礎,提供附加功能
def home():
    return "home page,hello"

@app.route('/input')#處理的網站路徑
#定義如何處理
def input():
    return render_template('user_input.html') 

# @app.route('/input_v1')
# def input_v1():
#     return render_template('user_input_v1.html') 

# @app.route('/input_v2')
# def input_v2():
#     return render_template('user_input_v2.html') 

# @app.route('/info')
# def info():
#     return render_template('user_info.html')

if __name__=="__main__": #如果以主程式執行
    app.run() #啟動伺服器sss666

#Procfile 裡面的web gunicorn app(檔名):app(第2行的變數)
#如果修改程式(本機端開發完)>要重新部署(不用初始化)>git add .>git commit -m "note">git push heroku master
#heroku網址:https://bestplace1130liff.herokuapp.com/ 
#看log:heroku logs --tail