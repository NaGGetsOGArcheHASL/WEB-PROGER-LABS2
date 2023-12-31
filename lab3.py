from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)



@lab3.route('/lab3/order')
def order():
    return render_template('order.html')



@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')

@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    type = request.args.get('type')  
    shelf = request.args.get('shelf') 
    bag = request.args.get('bag')
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    departure = request.args.get('departure')
    if departure == '':
        errors['departure'] = 'Заполните поле!'
    entry = request.args.get('entry')
    if  entry == '':
        errors['entry'] = 'Заполните поле!'
    date = request.args.get('date')
    if  date == '':
        errors['date'] = 'Заполните поле!'
    return render_template('ticket.html', user=user, errors=errors, type=type, shelf=shelf, bag=bag, age=age, departure=departure,entry=entry, date=date)

