import os
from tokens import *
from profiles import *

"""应用入口"""

tk = AUTH()
pf = get_profile()


class enter:
    """应用入口"""

    def __init__(self):
        pass

    def first_choose(self):
        print('请问您要进行什么操作？\n')
        print('[1]查看个人信息\n')
        print('[2]登录\n')
        self.status = input('请输入序号:')

        if self.status == '1':
            print('对接中..')

        elif self.status == '2':
            self.token_exists = os.path.isfile("token.json")
            if self.token_exists == True:
                tk.load_tokens()
                tk.refresh_acc_tk()
                tk.save_tokens('old')

            else:
                tk.get_code()
                tk.qsl_code()
                tk.access_token()
                tk.save_tokens('new')
