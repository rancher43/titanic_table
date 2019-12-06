from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/")
def hello():
	tit = pd.read_csv('data/titanic.csv')
	df = tit.head()
	return df.to_html()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
