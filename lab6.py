from flask import Blueprint, render_template, request, make_response, redirect, session
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6 = Blueprint('lab6', __name__) 


@lab6.route("/lab6/check")
 def main():
     my_users = users.query.all()
     print(my_users)
     return "result in console!"

 @lab6.route("/lab6/checkarticles")
 def check_articles():
     my_articles = articles.query.all()
     print(my_articles)
     return "result in console!"

 @lab6.route("/lab6/register", methods=["GET", "POST"])
 def register():

     errors = ''

     if request.method == "GET":
         return render_template("register.html")

     username_form = request.form.get("username")
     password_form = request.form.get("password")

     isUserExist = users.query.filter_by(username=username_form).first()

     if username_form == '':
         errors='Пустое имя'
         return render_template("register.html", errors=errors)
     else:
         if isUserExist is not None:
             errors='Пользователь с тамим именем уже существует'
             return render_template("register.html")
         else:
             if len(password_form) <5:
                 errors='Пароль меньше 5-ти сиволов'
                 return render_template("register.html")
             else:
                 hashedPswd = generate_password_hash(password_form, method='pbkdf2')
                 newUser = users(username=username_form, password=hashedPswd)

                 db.session.add(newUser)
                 db.session.commit()

     return redirect("/lab6/login")

 @lab6.route("/lab6/login", methods=["GET", "POST"])
 def login():
     errors = ''
     if request.method == "GET":
         return render_template("login.html")

     username_form = request.form.get("username")
     password_form = request.form.get("password")

     my_user = users.query.filter_by(username=username_form).first()

     if username_form == '' or password_form == '':
         errors='Заполните поле пользователь и пароль'
         return render_template("login.html", errors=errors)
     else:
         if my_user is not None:
             if check_password_hash(my_user.password, password_form):
                 login_user(my_user, remember=False)
                 return redirect("/lab6/articles")
             else:
                 errors='Введен не верный пароль'
                 return render_template("login.html", errors=errors)
         else:
             errors='Пользователя с таким именем не существует'
             return render_template("login.html", errors=errors)