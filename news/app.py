from flask import Flask, render_template
import requests
from decouple import config

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'


@app.route('/')
def home():
    api_key = config('API_KEY')
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey='+api_key
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return render_template("home.html", context=articles)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,)
