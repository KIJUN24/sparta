from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'melon.db')
db = SQLAlchemy(app)

class Melon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.rank}등: {self.title} by {self.artist}'


with app.app_context():
    db.create_all()
    # 멜론 뮤직 스크래핑

    url = "https://www.melon.com/chart/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('table > tbody > tr')
    for tr in trs:
        rank = tr.select_one('.rank').text
        title_melon = tr.select_one('.rank01 > span > a').text
        artist_melon = tr.select_one('.rank02 > a').text
        image_melon = tr.select_one('img')['src']
        song = Melon(username="Melon", rank=rank, title=title_melon, artist=artist_melon, image_url=image_melon)
        db.session.add(song)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
