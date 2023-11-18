import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AUNYNZqkxMxam3ykGnx65K53e4FlWj4rcCJGOQDxv032GrEwTgO04jB9-La7sEgaissoZaOcOC6tus4i"
        self.client_secret = "EIxNsK2sJwNluZ5qv8O93i2fuxL6Fdt704LCLxlVVhJyPK2AtQzOFSl5SnjcRZ_wyhNvxjQYwxGlDuc6"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
