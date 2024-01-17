import json
from bag import Bag
from settings import Settings
import time
import os
from tutorial import Tutorial

class MagicLengin():
    def __init__(self):
        # 存储用户的列表
        self.users = []

        self.settings = Settings()
        self.bag = Bag()

    '''注册方法'''

    def register(self, cd=1):
        print('register...')
        username = input('  username:')
        password = input('  password:')
        self.users.append(username)
        self.users.append(password)
        if cd == 0:
            os.makedirs('package')
            f = open('./package/user.txt','w')
            f.write(f'{username}\n{password}')

    '''登录方法'''

    def login(self):
        print('login...')
        self.username = input('  username:')
        self.password = input('  password:')
        f = open('./package/user.txt')
        res = f.readlines()
        # res = ['1\n','2']
        if res[0][0:list(res[0]).index('\n')] == self.username\
                and res[1] == self.password:
            return True
        else:
            return False

    '''寝室'''

    def bedroom_shell(self):
        bedroom_msgs_list = list('寝室。温暖的壁炉旁。')
        for i in bedroom_msgs_list:
            print(i, end='')
            time.sleep(self.settings.stop_time)
        print()
        while self.settings._bedroom:
            ins = input(f'() ')
            if ins not in self.settings.bedroom_set_list:
                print('输入‘help’以获取帮助。')

            else:
                # 获取帮助
                if ins == 'help':
                    print(f'寝室指令集：{game.settings.bedroom_set_list}')
                # 退出
                elif ins == 'finish':
                    break
                    # fshell._finish(self)
                # 退出寝室
                elif ins == 'outdoor':
                    game.settings._bedroom = False
                # 查看背包
                elif ins == '@bag':
                    game.bag.bag_shell()

                # 用户设置
                elif ins == '@me':
                    print('MagicLengin 魔法传说 v.1.0.0')
                    print('@Pioneer 2024')
                    print(f'用户名{game.users[0]}')
                    print(f'用户密码{game.users[1]}')

    '''运行命令行方法'''

    def run_shell(self, cd):
        print('Welcome to MagicLengin.')
        self.settings._println()
        MagicLengin.bedroom_shell(self)
        if cd == 0:
            Tutorial.tu_shell()



    def _dir(self):
        dirs = os.listdir(os.getcwd())
        if 'package' not in dirs:
            return False
        else:
            return True


if __name__ == '__main__':
    game = MagicLengin()
    if game._dir():
        if game.login():
            game.run_shell(cd=1)
    else:
        game.register(cd=0)
        if game.login():
            game.run_shell(cd=0)