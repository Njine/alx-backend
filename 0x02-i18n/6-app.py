#!/usr/bin/env python3
"""Flask app with internationalization support."""
from flask_babel import Babel, _
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Represents a Flask Babel config."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieve a user based on a user ID."""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Perform routines before request's resolution."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Retrieve the locale for a web page."""
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    # Locale from user settings
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    # Locale from request header
    header_locale = request.headers.get('locale')
    if header_locale and header_locale in app.config["LANGUAGES"]:
        return header_locale
    # Default locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Render the home/index page."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
