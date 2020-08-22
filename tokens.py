from urllib.parse import parse_qsl, urlsplit
import requests
import json


class AUTH:
    """获取令牌,并刷新

    :param acc_tk: access token
    :param ref_tk: refresh token
    """

    def __init__(self):
        self.cliend_id = 'c7400ddc-07f0-45e5-866b-e40a57a5831e'
        self.scope = 'user.read mail.read offline_access'
        try:
            with open('token.json', mode='r') as ori_token:
                all_date = json.load(ori_token)
                self.acc_tk = all_date['access_token']
                self.ref_tk = all_date['refresh_token']
        except FileNotFoundError:
            print('未登录！\n')
            self.get_code()
            self.qsl_code()
            self.access_token()
            self.save_tokens('new')

    def get_code(self):
        """获取长地址"""
        global backsite
        backsite = input("""
go to this site:
https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=c7400ddc-07f0-45e5-866b-e40a57a5831e&response_type=code&redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient&response_mode=query&scope=offline_access%20user.read%20mail.read&state=200

Paste the authenticated url here:
""")

    def access_token(self):
        """发送请求"""
        global code
        global r
        url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'client_id': self.cliend_id,
            'scope': self.scope,
            'code': code,
            'redirect_uri': 'https://login.microsoftonline.com/common/oauth2/nativeclient',
            'grant_type': 'authorization_code',
        }
        r = requests.post(url, data=data, headers=headers)

    def qsl_code(self):
        """提取code"""
        global backsite
        global code
        code = dict(parse_qsl(urlsplit(backsite).query)).get('code')

    def save_tokens(self, noro):
        """将access_token和refresh_token写入文件"""
        global r
        if noro == 'new':
            with open('token.json', mode='w') as token_recorder:
                data2 = json.loads(r.text)
                data3 = json.dumps(data2, sort_keys=True,
                                   indent=4, separators=(',', ':'))
                token_recorder.write(data3)

        elif noro == 'old':
            with open('token.json', mode='w') as token_recorder:
                data2 = json.loads(self.s.text)
                data3 = json.dumps(data2, sort_keys=True,
                                   indent=4, separators=(',', ':'))
                token_recorder.write(data3)

    def load_tokens(self):
        """加载获取的access_token和refresh_token"""
        with open('token.json', mode='r') as ori_token:
            all_date = json.load(ori_token)
            self.acc_tk = all_date['access_token']
            self.ref_tk = all_date['refresh_token']

    def refresh_acc_tk(self):
        """刷新访问令牌"""
        url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        try:
            data = {
                'client_id': self.cliend_id,
                'scope': self.scope,
                'refresh_token': self.ref_tk,
                'redirect_uri': 'https://login.microsoftonline.com/common/oauth2/nativeclient',
                'grant_type': 'refresh_token',
            }
            self.s = requests.post(url, data=data, headers=headers)
            self.save_tokens('old')
        except AttributeError:
            self.load_tokens()
            self.refresh_acc_tk()
