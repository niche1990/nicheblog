from flask import Blueprint
blue = Blueprint('about', __name__)
from . import view
__all__ = ['blue']
