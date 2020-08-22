from .tokens import AUTH
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
        self.tk.save_tokens('old')
        self.tk.load_tokens()
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
        """离线个人资料，方便查找,使用前，先ori_profile()"""
        pr_dic = json.loads(self.r.text)
        data4 = json.dumps(pr_dic, sort_keys=True,
                           indent=4, separators=(',', ':'))
        try:
            with open('local\\profile.json', mode='w') as ori_profile:
                ori_profile.write(data4)

        except FileNotFoundError:
            File_Path = os.getcwd()+'\\local\\'
            if os.path.isdir(File_Path) != True:
                os.makedirs(File_Path)
            self.save_profile()

    def load_profile(self):
        """从文件加载配置信息，注意，以unicode返回"""
        try:
            with open('local\\profile.json', mode='r') as prof:
                all_pf = json.load(prof)
                self.businessPhones = all_pf['businessPhones']
                self.displayName = all_pf['displayName']
                self.givenName = all_pf['givenName']
                self.mail = all_pf['mail']
                self.mobilePhone = all_pf['mobilePhone']
                self.preferredLanguage = all_pf['preferredLanguage']
                self.surname = all_pf['surname']
                self.userPrincipalName = all_pf['userPrincipalName']
        except FileNotFoundError:
            File_Path = os.getcwd()+'\\local\\'
            if os.path.isdir(File_Path) != True:
                os.makedirs(File_Path)
            self.ori_profile()
            self.save_profile()
            self.load_profile()
        except KeyError:
            File_Path = os.getcwd()+'\\local\\'
            if os.path.isdir(File_Path) != True:
                os.makedirs(File_Path)
            self.ori_profile()
            self.save_profile()
            self.load_profile()

    def back_info(self, info_name):
        """使用前，请load_profile"""

        try:
            if info_name == '1':  # 工作电话
                return self.businessPhones
            elif info_name == '2':  # 全名
                return self.displayName
            elif info_name == '3':  # 名
                return self.givenName
            elif info_name == '4':  # 姓
                return self.surname
            elif info_name == '5':  # 邮箱
                return self.mail
            elif info_name == '6':  # 语言
                return self.preferredLanguage
            elif info_name == '7':  # 手机号
                return self.mobilePhone
            elif info_name == '8':  # 登录名(主要邮箱/手机号)
                return self.userPrincipalName
            elif info_name == '9':
                self.ori_profile()
                self.save_profile()
                self.load_profile()
                self.back_info(info_name)
            elif info_name == '10':
                os.system('pause')
            else:
                return '未找到结果'
        except AttributeError:
            self.load_profile()
