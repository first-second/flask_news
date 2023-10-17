from flask import Flask,render_template
import requests
app = Flask(__name__)

app.static_url_path = '/static'

# Define the folder where static files are stored (the 'static' subdirectory)
app.static_folder = 'static'
@app.route('/')
def home():
    API_KEY="ee976b9f40b84b11af9136c525cc5618"
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey='+API_KEY
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return render_template("home.html", context=articles)

if __name__=="__main__":
    app.run(debug=True)