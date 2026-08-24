from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My Flask App</title>
    </head>
    <body>
        <h1>Hello Vasikar</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
