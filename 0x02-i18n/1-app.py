#!/usr/bin/env python3
"""A Flask app with Flask Babel integration.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Defines Flask Babel config settings.
    """
    LANGUAGES = ["en", "fr"]  # Available languages for translation
    BABEL_DEFAULT_LOCALE = "en"  # Default language/locale
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)  # Initialize Flask app
app.config.from_object(Config)  # Configure Flask app with custom settings
app.url_map.strict_slashes = False  # Disable strict slashes in routes
babel = Babel(app)  # Initialize Babel extension for language localization


@app.route('/')
def get_index() -> str:
    """Render the index page with Flask Babel.
    """
    return render_template('1-index.html')  # Render the index HTML template


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run app on specified host and port
