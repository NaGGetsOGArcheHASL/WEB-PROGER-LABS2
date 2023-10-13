from flask import Flask, redirect, url_for, render_template
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
        <link rel="stylesheet" href=" """ + url_for('static', filename='lab1.css') + """ ">
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

@app.route('/lab1/oak')
def oak():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href=" ''' + url_for('static', filename='lab1.css') + ''' ">
    <title>Dub</title>
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <h1>Дуб</h1>
    <img src=" ''' + url_for('static', filename='oak.jpg') + ''' ">
    
</body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Нагайцев Максим'
    groupe = 'ФБИ-12'
    course = '3 курс'
    number = '2'
    fruits = [
        {'name':'яблоки','price':'99₽'},
        {'name':'груши','price':'139₽'},
        {'name':'апельсины','price':'79₽'},
        {'name':'мандарины','price':'259₽'},
        {'name':'манго','price':'199₽'}
        ]
    books = [
        {'name': '1984', 'name_author': 'Джордж Оруэлл', 'zanr': 'Антиутопия', 'kol_stranits': '328'},
        {'name': 'Преступление и наказание', 'name_author': 'Федор Достоевский', 'zanr': 'Роман', 'kol_stranits': '592'},
        {'name': 'Гарри Поттер и философский камень', 'name_author': 'Дж. К. Роулинг', 'zanr': 'Фэнтези', 'kol_stranits': '320'},
        {'name': 'Война и мир', 'name_author': 'Лев Толстой', 'zanr': 'Роман', 'kol_stranits': '1225'},
        {'name': 'Убийство в Восточном экспрессе', 'name_author': 'Агата Кристи', 'zanr': 'Детектив', 'kol_stranits': '256'},
        {'name': 'Алиса в Стране чудес', 'name_author': 'Льюис Кэрролл', 'zanr': 'Приключения', 'kol_stranits': '240'},
        {'name': 'Мастер и Маргарита', 'name_author': 'Михаил Булгаков', 'zanr': 'Роман', 'kol_stranits': '448'},
        {'name': 'Три товарища', 'name_author': 'Эрих Мария Ремарк', 'zanr': 'Роман', 'kol_stranits': '416'},
        {'name': 'Самый богаты человек в вавилоне', 'name_author': 'Джордж Оруэлл', 'zanr': 'Антиутопия', 'kol_stranits': '156'},
        {'name': 'Анна Каренина', 'name_author': 'Лев Толстой', 'zanr': 'Роман', 'kol_stranits': '864'}
    ]
    return render_template('example.html', name=name, number=number, groupe=groupe,course=course, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template ('lab2.html')