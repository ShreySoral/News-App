from flask import Flask,render_template
import requests
app=Flask(__name__)
@app.route('/')
def index():
    url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d277c1aadd1e4e3e9402e5ff056bf970"
    r=requests.get(url).json()
    cases={
        "articles":r["articles"]
    }
    return render_template('index.html',case=cases)

if __name__ == '__main__':
    app.run(debug=True)