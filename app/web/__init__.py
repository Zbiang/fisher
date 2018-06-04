from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user
from app.web import auth
from app.web import drift
from app.web import wish
from app.web import gift
from app.web import main
# 这里web和from位置为什么不能颠倒？？？,我觉得ok