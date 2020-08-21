from tokens import AUTH
import requests
import requests
import json
import os


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

    def save_profile(self):
        """离线个人资料，方便查找"""
        pr_dic = json.loads(self.r.text)
        data4 = json.dumps(pr_dic, sort_keys=True,
                           indent=4, separators=(',', ':'))
        try:
            with open('local\profile.json', mode='w') as ori_profile:
                ori_profile.write(data4)

        except FileNotFoundError:
            File_Path = os.getcwd()+'\\local\\'
            os.makedirs(File_Path)
            self.save_profile()


pr = get_profile()
pr.ori_profile()
pr.save_profile()
