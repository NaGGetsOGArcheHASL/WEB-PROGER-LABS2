from flask import Blueprint, render_template, request, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login4', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login4.html")
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not username:
        error = 'Не введен логин'
        return render_template('login4.html', error=error)
    elif not password:
        error = 'Не введен пароль'
        return render_template('login4.html', error=error)

    if username == 'alex' and password == '123':
        return render_template('success_for_lab4.html')
    else:
        error = 'Неверный логин и/или пароль'
        return render_template('login4.html', error=error, username=username, password=password)

##Холодильник        

@lab4.route('/lab4/fridge',methods = ['GET','POST'])
def fridge():
    return render_template('fridge.html')

@lab4.route('/lab4/success_fridge',methods = ['GET','POST'])
def fridge1():
    temperature = request.form.get('temperature') 
    temperature = int(temperature)
    if not temperature:
        message = 'Ошибка: не задана температура'
        return render_template('success_fridge.html', message=message)

    if temperature < -12:
        message = 'Не удалось установить температуру — слишком низкое значение'
        return render_template('success_fridge.html', message=message)
    elif temperature > -1:
        message = 'Не удалось установить температуру — слишком высокое значение'
        return render_template('success_fridge.html', message=message)
    elif -12 <= temperature <= -9:
        snowflakes = 'три синих снежинки'
    elif -8 <= temperature <= -5:
        snowflakes = 'две синих снежинки'
    elif -4 <= temperature <= -1:
        snowflakes = 'одна синяя снежинка'
    else:
        snowflakes = ''
    message = f'Установлена температура: {temperature}°С'
    return render_template('success_fridge.html', message=message, snowflakes=snowflakes)

@lab4.route('/lab4/corn',methods = ['GET','POST'])
def corn():
    return render_template('corn.html')


@lab4.route('/lab4/success_corn',methods = ['GET','POST'])
def corn1():
    corn = request.form.get('corn') 
    weight = request.form.get('weight') 
    weight = int(weight)
    
    if weight > 500:
        error = 'Такого объёма сейчас нет в наличии'
        return render_template('corn.html', weight=weight, error=error)
    if weight <=0:
        error = 'Неверное значение веса'
        return render_template('corn.html', weight=weight, error=error)
    
    if corn == 'Ячмень':
        corn = 'Ячмень'
        money = 12000 * weight
        discount = ''
        if weight >50:
            discount = 'Применена скидка за большой объём'
            money = money * 0.9
        return render_template('success_corn.html', weight=weight, money=money, discount=discount,corn=corn)
    
    if corn == 'Овёс':
        corn = 'Овёс'
        money = 8500 * weight
        discount = ''
        if weight >50:
            discount = 'Применена скидка за большой объём'
            money = money * 0.9
        return render_template('success_corn.html', weight=weight, money=money, discount=discount,corn=corn)
    
    if corn == 'Пшеница':
        corn = 'Пшеница'
        money = 8700 * weight
        discount = ''
        if weight >50:
            discount = 'Применена скидка за большой объём'
            money = money * 0.9
        return render_template('success_corn.html', weight=weight, money=money, discount=discount,corn=corn)
    
    if corn == 'Рожь':
        corn = 'Рожь'
        money = 14000 * weight
        discount = ''
        if weight >50:
            discount = 'Применена скидка за большой объём'
            money = money * 0.9
        return render_template('success_corn.html', weight=weight, money=money, discount=discount,corn=corn)
    return render_template('success_corn.html', corn=corn, weight=weight)
