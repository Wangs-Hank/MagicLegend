import time
from settings import Settings


class Tutorial:
    def __init__(self):
        self.setting = Settings()

    def tu_shell(self):
        self.setting._println()
        ins = input('或许你要去对角巷? (y/n) ')
        if ins == 'y':
            while True:
                set = input('(shopStreet) ')
                if set in '1':
                    self._print(l=list(f'进入对角巷521号 - 咿啦猫头鹰商店\n'))
                    self._print(l=list(f'Eeylops Owl Emporium是一家位于伦敦对角巷北侧的商店，'
                                       '出售猫头鹰以及猫头鹰所需的各种食物和用具。'
                                       '这里显得有些黑洞洞，可能是因为猫头鹰喜爱这种环境。'))
                    print('\n')
                    while True:
                        owlsList = [{'草枭': 10, '褐枭': 10, "鸣角枭": 15, "雪枭": 15, "灰林枭": 10},
                                    {'猫头鹰罐头': 2, '猫头鹰坚果': 2}]
                        owlsShopNotice = '''
                        售卖商品：
                        猫头鹰
                            1.草枭 - 10
                            2.褐枭 - 10
                            3.鸣角枭 - 15
                            4.雪枭 - 15
                            5.灰林枭 - 10
                        猫头鹰食
                            6.猫头鹰罐头 - 2
                            7.猫头鹰坚果 - 2                        
                        '''
                        print(owlsShopNotice)
                        owl = input("(Owl) ")
                        if owl in '01234567' and 0 <= int(owl) < 8:
                            if int(owl) == 1:
                                print(f'购买成功，花费{owlsList[0]["草枭"]}加隆')
                            if int(owl) == 2:
                                print(f'购买成功，花费{owlsList[0]["褐枭"]}加隆')
                            if int(owl) == 3:
                                print(f'购买成功，花费{owlsList[0]["鸣角枭"]}加隆')
                            if int(owl) == 4:
                                print(f'购买成功，花费{owlsList[0]["鸣角枭"]}加隆')
                            if int(owl) == 5:
                                print(f'购买成功，花费{owlsList[0]["灰林枭"]}加隆')
                            if int(owl) == 6:
                                print(f'购买成功，花费{owlsList[1]["猫头鹰罐头"]}加隆')
                            if int(owl) == 7:
                                print(f'购买成功，花费{owlsList[1]["猫头鹰坚果"]}加隆')
                        elif owl == 'finish':
                            print('------------------退出猫头鹰商店------------------------')
                            break
                        else:
                            print('编号不正确.')

                elif set in '2':
                    self._print(l=list(f'进入对角巷 - 丽痕书店\n'))
                    self._print(l=list(f'Flourish and Blotts是一家位于对角巷北侧的书店，'
                                       f'霍格沃茨的大多数学生都会在这里购买他们所需的课本。'))
                    print('\n')
                    while True:
                        booksDic = {1: 1,
                                    2: 1,
                                    3: 1,
                                    4: 1,
                                    5: 1,
                                    6: 2,
                                    7: 1,
                                    8: 2,
                                    9: 2,
                                    10: 2,
                                    11: 2,
                                    12: 5,
                                    13: 4,
                                    14: 2,
                                    15: 2,
                                    16: 3,
                                    17: 2,
                                    18: 4,
                                    19: 3,
                                    20: 3,
                                    21: 3,
                                    22: 7,
                                    23: 10,
                                    24: 5,
                                    25: 39}
                        bookShopNotice = '''
课本
    1.《标准咒语，初级》 (1加隆)
    2.《标准咒语，二级》 (1加隆)
    3.《标准咒语，三级》 (1加隆)
    4.《标准咒语，四级》 (1加隆)
    5.《初学变形指南》 (1加隆)
    6.《魔法药剂与药水》 (2加隆)
    7.《黑暗力量：自卫指南》 (1加隆)
    8.《魔法史》 (2加隆)
    9.《千种神奇草药及蕈类》 (2加隆)
    10.《魔法理论》 (2加隆)
    11.《怪兽及其产地》 (2加隆)
    12.《与西藏雪人在一起的一年》 (5加隆)
    13.《妖怪们的妖怪书》 (4加隆)
    14.《拨开迷雾看未来》 (2加隆)
    15.《中级变形术》 (2加隆)
    16.《高级魔药制作》 (3加隆)
热销书
    17.《诅咒与反诅咒》 (2加隆)
    18.《会魔法的我》 (4加隆)
    /.《隐形术的隐形书》 (进货后再也找不到，因此没有出售)
    19.《预言无法预言的：使自己免受惊吓》 (3加隆)
    20.《死亡预兆：当你知道厄运即将到来时该怎么办》 (3加隆)
    21.《破碎的球：当厄运来临时》 (3加隆)
    22.《阿不思·邓布利多的生平和谎言》 (7加隆)
    23.《邓布利多军：退伍者的阴暗面》 (10加隆)
    24.《我的哑炮生活》 (5加隆)
    25.《魁地奇世界杯官方指南》 (39加隆)
 '''
                        print(bookShopNotice)
                        book = input('(books) ')
                        if int(book) <= 25:
                            print(f'已购买，花费{booksDic[int(book)]}')
                        else:
                            print('输入书本对应编号以购买该书本.')
                elif set == 'help':
                    print('输入商店对应编号以进入该商店.')

                else:
                    print('输入help以获取帮助.')
        else:
            pass

    def _print(self, l):
        for i in l:
            print(i, end='')
            time.sleep(0.1)


if __name__ == '__main__':
    tutorial = Tutorial()
    tutorial.tu_shell()
