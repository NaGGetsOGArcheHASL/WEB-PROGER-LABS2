from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code = 302)
    
@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href=" """ + url_for('static', filename='lab1.css') + """ ">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <a href="/lab1">Лабораторная работа 1</a>

        <footer>
            &copy: Нагайцев Максим, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
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
        <div> Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div>
        
        <footer>
            &copy; Нагайцев Максим, ФБИ-12, 3 курс, 2023
        </footer>
    
    </body>
    </html>
"""