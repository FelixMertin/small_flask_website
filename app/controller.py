import os
from flask import render_template, render_template_string
from flask_mail import Message, BadHeaderError
from . import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def construct_payload_email(text, mail):
    text_body = render_template_string("mail.txt", text=text, mail=mail)

    html_body = render_template("mail.html", text=text, mail=mail)

    subject = 'Inquiry via YOURWEBSITE'

    return text_body, html_body, subject