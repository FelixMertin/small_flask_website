import flask
from flask import render_template, request
import uuid
import datetime
from .controller import send_email, construct_payload_email
from . import app, mail



"""
This is the main route which serves: yourdomain.com
"""
@app.route("/")
def index():

    return render_template("index.html")

"""
This is the imprint route which serves: yourdomain.com/imprint
"""
@app.route("/imprint")
def imprint():

    return render_template("imprint.html")

"""
This is the imprint route which serves: yourdomain.com/privacy_policy
"""
@app.route("/privacy_policy")
def privacyPolicy():

    return render_template("privacy_policy.html")


@app.route("/send", methods=["POST"])
def sendMail():
    if request.method == "POST":
        inquiry_text = request.form.get("inquiry_text")
        print(inquiry_text)
        inquiry_mailadress = request.form.get("inquiry_mailadress")
        print(inquiry_mailadress)
        text_body, html_body, subject = construct_payload_email(inquiry_text, inquiry_mailadress)


        try:
            """
            TODO: Add sender mail and recipient
            """
            send_email(subject=subject, sender='sender@gmail.com',
                       recipients=['recipient@gmail.com'],
                       text_body=text_body, html_body=html_body)
            return render_template("success.html")

        except Exception as e:
            print("Mail could not be sent!")
            print(e)
            return render_template("error.html", inquiry_text=inquiry_text)




