from flask import Flask,render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")

# jsldfjlsjfljre324243224523424
# sdf
#https://jsldfjlsjfljre324243224523424.ngrok.io/github-webhook/