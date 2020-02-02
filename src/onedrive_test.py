from onedrive_api import OnedriveApi
from onedrive_io import OnedriveIO


api = OnedriveApi()
api.load_session()


io = OnedriveIO(api)

print(io.fromPath("/Autostart.bat").read(1, 2))
