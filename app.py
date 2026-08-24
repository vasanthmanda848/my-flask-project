from flask import Flask

app = Flask(__name__)

students = ["Vasikar", "Ravi", "Rahul", "Arun"]

@app.route("/")
def home():

    result = "<h1>Students</h1><ul>"

    for student in students:
        result += f"<li>{student}</li>"

    result += "</ul>"

    return result

if __name__ == "__main__":
    app.run(debug=True)
