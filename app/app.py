from flask import Flask, render_template

app = Flask(__name__)

try:
	f = open('text.txt', 'r')
except:
	f = open('text.txt', 'w')
text = f.read()

@app.route("/")
def hello():
    return render_template('index.html', text=text)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)