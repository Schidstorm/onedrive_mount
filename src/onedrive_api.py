import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

redirect_uri = "https://login.live.com/oauth20_desktop.srf"
client_secret = '-3JRaoNZh-KunZr7Fty=zSYjWvdH:v38'
client_id = 'ab0c1161-3935-472e-869f-4eaeef55fa73'
api_base_url = 'https://api.onedrive.com/v1.0/'

scopes = ['onedrive.readwrite']


class OnedriveApi:
    def __init__(self):
        self.http_provider = onedrivesdk.HttpProvider()
        self.auth_provider = onedrivesdk.AuthProvider(
            http_provider=self.http_provider,
            client_id=client_id,
            scopes=scopes)

    def load_session(self):
        self.auth_provider.load_session()
        self.auth_provider.refresh_token()
        self.client = onedrivesdk.OneDriveClient(
            api_base_url, self.auth_provider, self.http_provider)

    def save_session(self):
        self.client.auth_provider.save_session()

    def generate_auth_url(self):
        self.client = onedrivesdk.OneDriveClient(
            api_base_url, self.auth_provider, self.http_provider)
        return self.client.auth_provider.get_auth_url(redirect_uri)

    def authenticate(self):
        url = self.generate_auth_url()
        print(url)
        code = GetAuthCodeServer.get_auth_code(
            url, redirect_uri)
        client.auth_provider.authenticate(code, redirect_uri, client_secret)

    def process_auth_code(self, code):
        self.client = onedrivesdk.OneDriveClient(
            api_base_url, self.auth_provider, self.http_provider)

        self.client.auth_provider.authenticate(
            code, redirect_uri, client_secret)
        self.auth_provider
        self.auth_provider.refresh_token()
