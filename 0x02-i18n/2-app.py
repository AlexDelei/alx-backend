#!/usr/bin/env python3
"""
Get Locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Configuration with A list of supported languages
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Get Locale from request
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    Simple HomePage
    """
    return render_template('2-index.html')
