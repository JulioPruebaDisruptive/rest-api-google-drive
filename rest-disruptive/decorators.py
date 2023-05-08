from functools import wraps
from flask import session, redirect, request, abort
from auth import GoogleAuth

#Google authentication required
def google_auth_requiered(function): 
    @wraps(function)
    def wrapper(*args, **kwargs):
        if request.args["state"] not in session["state"]:
            abort(500)
        return function(*args, **kwargs)
    return wrapper