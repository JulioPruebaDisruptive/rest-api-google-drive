from flask import Flask, session, redirect, request, render_template, url_for
from googleapiclient.errors import HttpError
import google
import cachecontrol
import requests
import os
import pathlib

from config import app
from auth import GoogleAuth
from helpers import Logger, Tools
from decorators import google_auth_requiered


@app.route('/login')
def login():
    authorization_url, session["state"] = GoogleAuth.get_auth_url()
    return redirect(authorization_url)
    
@app.route('/callback')
@google_auth_requiered
def callback():
    items = []
    credentials = GoogleAuth.fetch_token(request.url, session["state"])        
    id_info = GoogleAuth.verify_id_token(credentials)
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")

    if not credentials:
        credentials = GoogleAuth.refresh_token(credentials)

    service = GoogleAuth.get_drive_service(credentials)
    response = Tools.get_files_from_folder(service, 'carpeta 2')           

    return f"<a href='/logout'><button>Logout</button></a><br><br><br>Files in your Google Drive:\n{response}"

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.route('/')
def index():
    return "Press the button if you want to list the files in a google drive folder <br><br> <a href='/login'><button>Login</button></a>"

@app.route('/not_found')
def not_found():
    return "You must give permission to use google drive before using this service"



