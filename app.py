from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
import base64
import datetime
from db import db_init, db
from models import Videos
import utils
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.sqlite3'
db_init(app)

@app.route('/')
def main():
    res = utils.get_videos_dict()
    if res == False:
        return "Video Directory cannot found."
    if not Videos.query.all():
        for name, path in res.items():
            vid = Videos(name, path)
            db.session.add(vid)
            db.session.commit()
    
    rows = []
    row = []
    videos = Videos.query.all()
    for i in range(len(videos)):
        row.append(videos[i])
        if(len(row) == 2):
            rows.append(row)
            row = []            
    return render_template('main.html', rows=rows)

@app.route('/video-show', methods=['GET', 'POST'])
def video_show():
    ret_list = [[], [], []]
    if request.method == 'POST':
        vid_list = request.form.getlist('check')
        for i in range(len(vid_list)):
            ret_list[i // 3].append(vid_list[i])
    print(ret_list)
    return render_template("video-show.html", videos = ret_list)
if __name__ == '__main__':
      app.run(debug = True)