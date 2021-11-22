# coding:utf-8
 
from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import time
import config

from datetime import timedelta

from predict import predict

 
#设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
app = Flask(__name__)
# 设置静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)
 

import datetime
import random

def create_uuid(): #生成唯一的图片的名称字符串，防止图片显示时的重名问题
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
    randomNum = random.randint(0, 100);  # 生成的随机整数n，其中0<=n<=100
    if randomNum <= 10:
        randomNum = str(0) + str(randomNum)
    uniqueNum = str(nowTime) + str(randomNum)
    return uniqueNum
 
# @app.route('/upload', methods=['POST', 'GET'])
@app.route('/upload', methods=['POST', 'GET'])  # 添加路由
def upload():
    if request.method == 'POST':
        f = request.files['file']
        
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "only allow upload image type, include png、PNG、jpg、JPG、bmp"})
 
 
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        os.makedirs(config.input_dir, exist_ok=True)
        filename = create_uuid() + '.' + f.filename.rsplit('.', 1)[1]
        upload_path = os.path.join(basepath, 'static/inputs', filename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
 
        # 使用Opencv转换一下图片格式和名称
        # img = cv2.imread(upload_path)
        # cv2.imwrite(os.path.join(basepath, 'static/images', 'test.jpg'), img)

        predict(filename)
 
        user_input = request.form.get("name")
        return render_template('upload_ok.html',userinput=user_input,val1=time.time(),filename=filename)
 
    return render_template('upload.html')
 
 
if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=8080, debug=True)