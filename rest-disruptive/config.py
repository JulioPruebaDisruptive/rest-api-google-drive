from flask import Flask
import os, pathlib
from google_auth_oauthlib.flow import Flow
from constants import SECRET_KEY, GOOGLE_CLIENT_ID

CLIENT_SECRETS_FILE = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SERVER_PROTOCOL'] = 'HTTP/1.1'

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes = ["https://www.googleapis.com/auth/drive","openid"],
    redirect_uri="https://127.0.0.1:5000/callback"
)