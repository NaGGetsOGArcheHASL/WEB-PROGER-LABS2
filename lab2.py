from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/example')
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

@lab2.route('/lab2/')
def lab():
    return render_template ('lab2.html')