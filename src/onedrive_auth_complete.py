from onedrive_api import OnedriveApi


api = OnedriveApi()

api.process_auth_code("M6ed15bd0-5c25-14e8-979b-0e9631725af3")
api.save_session()
