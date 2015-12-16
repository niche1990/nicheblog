from flask import Blueprint
blue = Blueprint('home', __name__)
from . import view
__all__ = ['blue']
