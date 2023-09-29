from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Нагайцев Максим Алексеевич, Лабораторная работа 1</title>
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>

    <h1> WEB-сервер на Flask</h1>

    <footer>
        &copy; Нагайцев Максим, ФБИ-12, 3 курс, 2023
    </footer>
    
</body>
</html>
"""