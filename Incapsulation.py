class Main:
    def __init__(self):
        self.public = [1, 2, 3, 4]
        self.__private = [1, 12, 11, 34, 43, 65, 6554, 945, 123]
        self._secure = [5, 6, 7, 3, 4]

    def show(self):
        print(self.public)

    def add(self, x):
        if x not in a.public:
            self.public.append(x)
            print(a.public)
        elif x in a.public:
            c = input('This item already exists! Add it anyway?\ny/n\n')
            if c == 'y':
                self.public.append(x)
                print(a.public)
            elif c == 'n':
                print(a.public)

    def delete(self, x):
        if x in a.public:
            self.public.remove(x)
            print(a.public)
        elif x not in a.public:
            input('This item does not exists!')
            print(a.public)

    def _print_secure(self):
        print(self._secure)

    def _add_sec(self, x):
        if x not in a._secure:
            self._secure.append(x)
            print(a._secure)
        elif x in a._secure:
            c = input('This item already exists! Add it anyway?\ny/n\n')
            if c == 'y':
                self._secure.append(x)
                print(a._secure)
            elif c == 'n':
                print(a._secure)

    def _del_sec(self, x):
        if x in a._secure:
            self._secure.remove(x)
            print(a._secure)
        elif x not in a._secure:
            input('This item does not exists!')
            print(a._secure)

    def show_private(self):
        self.__show_pr()

    def __show_pr(self):
        print(self.__private)

    def add_private(self, arg_data):
        self.__add_pr(arg_data)

    def __add_pr(self, x):
        if x not in a.__private:
            self.__private.append(x)
            print(a.__private)
        elif x in a.__private:
            c = input('This item already exists! Add it anyway?\ny/n\n')
            if c == 'y':
                self.__private.append(x)
                print(a.__private)
            elif c == 'n':
                print(a.__private)

    def del_private(self, arg_data):
        self.__del_pr(arg_data)

    def __del_pr(self, x):
        if x in a.__private:
            self.__private.remove(x)
            print(a.__private)
        elif x not in a.__private:
            input('This item does not exists!')
            print(a.__private)

a = Main()

while True:
    while True:
        s = input('Choose an option (user/admin/owner): ')
        if s == "user":
            while True:
                what = input("\nChoose action (show, add, del): ")

                if what == 'help':
                    print("\nshow = show items"
                          "\nadd = Add item"
                          "\ndel = Delete item"
                          "\nback = exit")
                    continue
                elif what == 'back':
                    break

                if what == 'show':
                    a.show()
                elif what == 'add':
                    var = input(
                        "\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                    if var == "num":
                        x = int(input("\nEnter integer: "))
                    elif var == "wrd":
                        x = input("\nEnter string: ")
                    elif var == 'lst':
                        m = input("\nEnter list: ").split(' ')
                        x = [i for i in m]
                    elif var == 'tup':
                        m = input("\nEnter tuple: ").split(' ')
                        x = [i for i in m]
                        x = tuple(x)
                    else:
                        continue
                    a.add(x)
                elif what == 'del':
                    var = input(
                        "\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                    if var == "num":
                        x = int(input("\nEnter integer: "))
                    elif var == "wrd":
                        x = input("\nEnter string: ")
                    elif var == 'lst':
                        x = input("\nEnter list: ").split(' ')
                        x = [i for i in x]
                    elif var == 'tup':
                        x = input("\nEnter tuple: ").split(' ')
                        x = [i for i in x]
                        x = tuple(x)
                    else:
                        continue
                    a.delete(x)

        elif s == "admin":
            _pass = input('Enter login and password: ').split()
            if _pass[0] != 'admin' or _pass[1] != '1111':
                print('Wrong login or password. Try again\n')
                continue
            elif _pass[0] == 'admin' and _pass[1] == '1111':
                print("Hello admin!")
                while True:
                    what = input("\nChoose action (show, add, del): ")

                    if what == 'help':
                        print("\nshow = show items"
                              "\nadd = Add item"
                              "\ndel = Delete item"
                              "\nback = exit")
                        continue
                    elif what == 'back':
                        break

                    if what == 'show':
                        a._print_secure()
                    elif what == 'add':
                        var = input(
                            "\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                        if var == "num":
                            x = int(input("\nEnter integer: "))
                        elif var == "wrd":
                            x = input("\nEnter string: ")
                        elif var == 'lst':
                            m = input("\nEnter list: ").split(' ')
                            x = [i for i in m]
                        elif var == 'tup':
                            m = input("\nEnter tuple: ").split(' ')
                            x = [i for i in m]
                            x = tuple(x)
                        else:
                            continue
                        a._add_sec(x)
                    elif what == 'del':
                        var = input(
                            "\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                        if var == "num":
                            x = int(input("\nEnter integer: "))
                        elif var == "wrd":
                            x = input("\nEnter string: ")
                        elif var == 'lst':
                            x = input("\nEnter list: ").split(' ')
                            x = [i for i in x]
                        elif var == 'tup':
                            x = input("\nEnter tuple: ").split(' ')
                            x = [i for i in x]
                            x = tuple(x)
                        else:
                            continue
                        a._del_sec(x)

        elif s == "owner":
            _pass = input('Enter login and password: ').split()
            if _pass[0] != 'owner' or _pass[1] != '7777':
                print('Wrong login or password. Try again\n')
                continue
            elif _pass[0] == 'owner' and _pass[1] == '7777':
                print("Hello Boss!")
                while True:
                    what = input("\nChoose action (show, add, del): ")

                    if what == 'help':
                        print("\nshow = show items"
                              "\nadd = Add item"
                              "\ndel = Delete item"
                              "\nback = exit")
                        continue
                    elif what == 'back':
                        break

                    if what == 'show':
                        a.show_private()
                    elif what == 'add':
                        var = input(
                            "\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                        if var == "num":
                            x = int(input("\nEnter integer: "))
                        elif var == "wrd":
                            x = input("\nEnter string: ")
                        elif var == 'lst':
                            m = input("\nEnter list: ").split(' ')
                            x = [i for i in m]
                        elif var == 'tup':
                            m = input("\nEnter tuple: ").split(' ')
                            x = [i for i in m]
                            x = tuple(x)
                        else:
                            continue
                        a.add_private(x)
                    elif what == 'del':
                        var = input(
                            "\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                        if var == "num":
                            x = int(input("\nEnter integer: "))
                        elif var == "wrd":
                            x = input("\nEnter string: ")
                        elif var == 'lst':
                            x = input("\nEnter list: ").split(' ')
                            x = [i for i in x]
                        elif var == 'tup':
                            x = input("\nEnter tuple: ").split(' ')
                            x = [i for i in x]
                            x = tuple(x)
                        else:
                            continue
                        a.del_private(x)
