from onedrive_api import OnedriveApi
from onedrivesdk.helpers import GetAuthCodeServer


api = OnedriveApi()
api.authenticate()
api.save_session()
