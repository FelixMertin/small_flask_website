from flask import Flask
from flask_mail import Mail, Message
import os
import platform


app = Flask(__name__)


if platform.system() == "Windows":
    """
    For local Development on Windows 10
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = True
    PORT = 5000
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")


else:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = True
    PORT = 5000
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")

"""
TODO: You will need to configure your Mail Provider.
The current setup is for gmail.
"""
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
mail = Mail(app)


from . import view