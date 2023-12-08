from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1', __name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)

@lab1.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>Нагайцев Максим, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>        

        <h1>web-сервер на flask</h1>

        <h2>Меню лабораторных работ</h1>

        <main>
            <ol>
                <li>
                    <a href="http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа №1</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab2" target="_blank">Лабораторная работа №2</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab3" target="_blank">Лабораторная работа №3</a>
                </li>
                 <li>
                    <a href="http://127.0.0.1:5000/lab4" target="_blank">Лабораторная работа №4</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab5" target="_blank">Лабораторная работа №5</a>
                </li>
            </ol>
        </main>

        <footer>
            &copy; Нагайцев Максим, ФБИ-12, 3 курс, 2023
        </footer>
    <body>
</html> 
"""

@lab1.route("/lab1/")
def lab():
    return"""
<!doctype html>
<html>
    <head>
        <title>Нагайцев Максим, Лабораторная 1</title>
    </head>
    
    <body>
        <header>
            НГТУ, ФБ, Лабораторная 1
        </header>        

        <h1>web-сервер на flask</h1>

            <h5>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </h5>
            <a href="/menu" target="_blank">меню</a>

        <h1>Реализованные роуты</h1>

        <main>
            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/oak" target="_blank">Дуб</a>
                </li>
            </ul>
        </main>

        <footer>
            &copy; Нагайцев Максим, ФБИ-12, 3 курс, 2023
        </footer>
    <body>
</html> 
"""
