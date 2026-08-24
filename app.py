from flask import Flask

app = Flask(__name__)

students = ["Vasikar", "Ravi", "Rahul", "Arun"]

@app.route("/")
def home():

    html = """
    <html>
    <head>
        <title>Student List</title>
    </head>

    <body style="background-color: lightblue; font-family: Arial;">

        <div style="
            width: 400px;
            margin: 100px auto;
            padding: 30px;
            background-color: white;
            text-align: center;
            border-radius: 10px;
        ">

            <h1 style="color: darkblue;">
                Student List
            </h1>

            <ul style="list-style-type: none; padding: 0;">
    """

    for student in students:
        html += f"""
                <li style="
                    background-color: lightgray;
                    margin: 10px;
                    padding: 10px;
                    border-radius: 5px;
                ">
                    {student}
                </li>
        """

    html += """
            </ul>

        </div>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)
