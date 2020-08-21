import requests
from tokens import AUTH
import requests



class get_profile:
    """读取profile"""

    def __init__(self):
        self.tk = AUTH()
        print('开始刷新access token\n')
        self.tk.refresh_acc_tk()
        print('刷新完毕')

    def ori_profile(self):
        """负责获取个人信息的返回数据"""
        url = 'https://graph.microsoft.com/v1.0/me'
        headers = {
            'Authorization': 'Bearer '+self.tk.acc_tk
        }

        self.r = requests.get(url, headers=headers)
        print(self.r.text)

get_profile().ori_profile()