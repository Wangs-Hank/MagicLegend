class Bag:
    def __init__(self):
        self.hand_right = ['MagicWand']
        self.hand_left = ['worldMap','lamp']
        self.case = [None]

        self.bag_set_list = ['rep']

    def bag_shell(self):
        print(f'''
{self.hand_right}
{self.hand_left}
{self.case}
''')
        while True:
            ins = input('<bag> ')
            if ins in self.bag_set_list:
                new = input('')

