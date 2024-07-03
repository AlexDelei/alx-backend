#!/usr/bin/env python3
"""
Use user locale
"""
from flask import (
    Flask,
    render_template,
    request,
    g)
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
    Use user locale
    """
    locale = request.args.get('locale')

    # Get locale from the request header
    if not locale:
        locale = request.accept_languages.best_match(app.config['LANGUAGES'])

    if locale not in app.config['LANGUAGES']:
        locale = app.config['BABEL_DEFAULT_LOCALE']

    return locale


@app.route('/')
def home():
    """
    Display according to user's settings
    """
    return render_template('6-index.html')
