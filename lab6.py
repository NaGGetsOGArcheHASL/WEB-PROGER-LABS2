from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2
from Db import db
from Db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('lab6', __name__) 