from onedrive_api import OnedriveApi
from onedrivesdk.helpers import GetAuthCodeServer


api = OnedriveApi()
print(api.generate_auth_url())
code = input("Code: ")
api.process_auth_code(code)
api.save_session()
