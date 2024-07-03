#!/usr/bin/env python3
"""
Infer appropriate timezone
"""
import pytz
from flask import Flask, render_template, request
from flask_babel import Babel
from pytz import UnknownTimeZoneError


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


@babel.timezoneselector
def get_timezone():
    """
    Inferring appropriate timezone
    """
    timeZone = request.args.get('timezone')
    if not timeZone:
        timeZone = app.config['BABEL_DEFAULT_TIMEZONE']
    
    try:
        pytz.timezone(timeZone)
    except UnknownTimeZoneError:
        timeZone = app.config['BABEL_DEFAULT_TIMEZONE']
    
    return timeZone


@app.route('/')
def home():
    """
    Display page according to settings
    """
    return render_template('3-index.html')

