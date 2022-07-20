class Base:
    def __init__(self):
        self.key_lst_a = []
        self.val_lst_a = []
        self.dct = {'in_dict': [1, 2, 3],
                    'after_list': {4, '5'}, 'after_set': ('hello', )}
        self.dict_keys = []
        self.dict_vals = []

    def key_in_a(self):
        key_a = input(">>>").split(" ")
        for i in key_a:
            self.key_lst_a.append(i)

    def val_in_a(self):
        val_a = input(">>>").split(" ")
        for i in val_a:
            self.val_lst_a.append(i)

    def option_input(self):
        what = input("\nChoose action (show, add, del): ")
        self.options(what)

    def help(self, what):
        if what == 'help':
            print("\nshow = show items\nadd = Add item\ndel = Delete item\nback = exit")
            self.options(what)

    def options(self, what):
        if what == "help":
            self.help_opt()

        elif what == 'show':
            self.show()

        elif what == 'add':

            var = input("\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nset = Set \nback = Back \n")

            if var == "num":
                x = int(input("\nEnter integer: "))
                self.add(x)
            elif var == "wrd":
                x = input("\nEnter string: ")
                self.add(x)
            elif var == 'lst':
                m = input("\nEnter list: ").split(' ')
                x = [i for i in m]
                self.add(x)
            elif var == 'tup':
                m = input("\nEnter tuple: ").split(' ')
                x = [i for i in m]
                x = tuple(x)
                self.add(x)
            elif var == 'set':
                x = input("\nEnter set: ").split(' ')
                x = set(x)
                self.add(x)

        elif what == "del":

            var = input("\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nset = Set \nback = Back \n")

            if var == "num":
                x = int(input("\nEnter integer: "))
                self.delete(x)
            elif var == "wrd":
                x = input("\nEnter string: ")
                self.delete(x)
            elif var == 'lst':
                x = input("\nEnter list: ").split(' ')
                x = [i for i in x]
                self.delete(x)
            elif var == 'tup':
                x = input("\nEnter tuple: ").split(' ')
                x = [i for i in x]
                x = tuple(x)
                self.delete(x)
            elif var == 'set':
                x = input("\nEnter set: ").split(' ')
                x = set(x)
                self.delete(x)

        elif what == "end":
            b.process_1()

    def help_opt(self):
        print("\nshow = show items\nadd = Add item\ndel = Delete item\nback = exit")
        self.option_input()

    def show(self):
        print(f"{self.key_lst_a}\n{self.val_lst_a}")
        self.option_input()

    def add(self, x):
        list_choose = input("Enter list to add: ")
        if list_choose == "key_lst":
            if x not in self.key_lst_a:
                self.key_lst_a.append(x)
                print(self.key_lst_a)
                self.option_input()
            elif x in self.key_lst_a:
                item = input('This item already exists! Add it anyway?\ny/n\n')
                if item == 'y':
                    self.key_lst_a.append(x)
                    print(self.key_lst_a)
                    self.option_input()
                elif item == 'n':
                    print(self.key_lst_a)
                    self.option_input()
        elif list_choose == "val_lst":
            if x not in self.val_lst_a:
                self.val_lst_a.append(x)
                print(self.val_lst_a)
                self.option_input()
            elif x in self.val_lst_a:
                item = input('This item already exists! Add it anyway?\ny/n\n')
                if item == 'y':
                    self.val_lst_a.append(x)
                    print(self.val_lst_a)
                    self.option_input()
                elif item == 'n':
                    print(self.val_lst_a)
                    self.option_input()

    def delete(self, x):
        list_choose = input("Enter list to edit: ")
        print(list_choose)
        if list_choose == "key_lst":
            if x in self.key_lst_a:
                self.key_lst_a.remove(x)
                print(self.key_lst_a)
                self.option_input()
            elif x not in self.key_lst_a:
                input('This item does not exists!')
                print(self.key_lst_a)
                self.option_input()
        elif list_choose == "val_lst":
            if x in self.val_lst_a:
                self.val_lst_a.remove(x)
                print(self.val_lst_a)
                self.option_input()
            elif x not in self.val_lst_a:
                input('This item does not exists!')
                print(self.val_lst_a)
                self.option_input()

    def process_1(self):
        self.key_lst_a = list(map(lambda i: tuple(i) if type(i) == set or type(i) == list else i, self.key_lst_a))
        self.val_lst_a = list(map(lambda i: tuple(i) if type(i) == set or type(i) == list else i, self.val_lst_a))
        c.process_2()

    def third_1(self):
        self.dict_keys = [i for i in self.dct.keys()]
        self.dict_vals = [i for i in self.dct.values()]
        self.dict_process_1()

    def dict_process_1(self):
        self.dict_keys = list(map(lambda i: tuple(i) if type(i) == set or type(i) == list else i, self.dict_keys))
        self.dict_vals = list(map(lambda i: tuple(i) if type(i) == set or type(i) == list else i, self.dict_vals))
        self.returner_1()

    def returner_1(self):
        return set(self.dict_keys), set(self.dict_vals)


class Support(Base):
    def key_in_b(self):
        key_b = input(">>>").split(" ")
        for i in key_b:
            self.key_lst_a.append(i)

    def val_in_b(self):
        val_b = input(">>>").split(" ")
        for i in val_b:
            self.val_lst_a.append(i)

    @staticmethod
    def process_2():
        res_1 = set(b.key_lst_a)
        res_2 = set(b.val_lst_a)
        print(f'{res_1}\n{res_2}')

    def third_2(self):
        self.dict_keys = [i for i in self.dct.keys()]
        self.dict_vals = [i for i in self.dct.values()]
        c.dict_process_2()

    def dict_process_2(self):
        self.dict_keys = list(map(lambda i: tuple(i) if type(i) == set or type(i) == list else i, self.dict_keys))
        self.dict_vals = list(map(lambda i: tuple(i) if type(i) == set or type(i) == list else i, self.dict_vals))
        self.returner_2()

    def returner_2(self):
        return set(self.dict_keys), set(self.dict_vals)

b = Base()
c = Support()
b.key_in_a()
b.val_in_a()
b.option_input()
b.third_1()
c.third_2()
a, b = b.returner_1()
c, d = c.returner_2()
print(f"Base Keys: {a}")
print(f"Base Values: {b}")
print(f"Support Keys: {c}")
print(f"Support Values: {d}")
