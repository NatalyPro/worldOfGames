from Score import get_score
from Utils import BAD_RETURN_CODE
from flask import Flask

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        score = get_score()
        return f"""
            <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
            """
    except ValueError as e:
        return f"""
        <html>
<head>
<title>Scores Game</title>
</head>
<body>
<body>
<h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>
</body>
</html>
"""


app.run(port=5000)
