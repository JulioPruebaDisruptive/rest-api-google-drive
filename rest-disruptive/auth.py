# auth.py
from google.oauth2 import id_token
from google.oauth2.id_token import verify_oauth2_token
from google.auth.exceptions import GoogleAuthError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google, cachecontrol, requests
from helpers import Logger


from config import GOOGLE_CLIENT_ID, CLIENT_SECRETS_FILE, flow



class GoogleAuth:

    def get_auth_url():
        try:
            authorization_url, state = flow.authorization_url()
            return authorization_url, state
        except Exception as e:
            return e

    def fetch_token(authorization_response, state):
        try:
            flow.fetch_token(authorization_response=authorization_response, state=state)
            credentials = flow.credentials
            return credentials
        except Exception as e:
            return "Error en GoogleAuth.fetch_token"

    def verify_id_token(credentials):
        try:
            token_request = google.auth.transport.requests.Request(session=cachecontrol.CacheControl(requests.session()))
            id_info = id_token.verify_oauth2_token(id_token=credentials._id_token, request=token_request, audience=GOOGLE_CLIENT_ID)
            return id_info
        except GoogleAuthError as e:
            print("Error de autenticación:", e)
            return None


    def refresh_token(credentials):
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            Logger.log.warning("credentials haven't refresh")
        return credentials


    def get_drive_service(credentials):
        try:
            service = build('drive', 'v3', credentials=credentials)
        except HttpError as e:
            return  f"Callback HttpError: {error_message}"
        return service