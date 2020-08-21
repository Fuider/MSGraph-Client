from tokens import AUTH
token = AUTH()
token.get_code()
token.qsl_code()
token.access_token()
token.save_tokens('new')
token.load_tokens()
token.refresh_acc_tk()
token.save_tokens('old')


