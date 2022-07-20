from datetime import datetime


def changelog(s, what):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    txt = open("test12.txt", "a")
    txt.write(f'{time} - {s} used {what} function\n')
    txt.close()


class Main:
    def __init__(self):
        self.public = [1, 2, 3, 4]
        self.__private = [1, 12, 11, 34, 43, 65, 6554, 945, 123]
        self._secure = [5, 6, 7, 3, 4]

    @staticmethod
    def logfile(s):
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")
        txt = open("test12.txt", "a")
        txt.write(f'{time} - {s} logged in\n')
        txt.close()

    def user_option(self):
        s = input('Choose an option (user/admin/owner): ')
        a.logfile(s)
        if s == "user":
            self.user(s)
        elif s == "admin":
            self.admin(s)
        elif s == "owner":
            self.owner(s)

    def user(self, s):
        self.option_input(s)

    def admin(self, s):
        _pass = input('Enter login and password: ').split()
        if _pass[0] != 'admin' or _pass[1] != '1111':
            print('Wrong login or password. Try again\n')
            self.admin(s)
        elif _pass[0] == 'admin' and _pass[1] == '1111':
            print("Hello admin!")
            self.option_input(s)

    def owner(self, s):
        _pass = input('Enter login and password: ').split()
        if _pass[0] != 'owner' or _pass[1] != '7777':
            print('Wrong login or password. Try again\n')
            self.owner(s)
        elif _pass[0] == 'owner' and _pass[1] == '7777':
            print("Hello Boss!")
            self.option_input(s)

    def option_input(self, s):
        what = input("\nChoose action (show, add, del): ")
        changelog(s, what)
        self.options(what, s)

    def help(self, what, s):
        if what == 'help':
            print("\nshow = show items\nadd = Add item\ndel = Delete item\nback = exit")
            self.options(s, what)

    def options(self, what, s):
        if what == "back":
            self.logout()
        elif what == "help":
            self.help_opt(s)
        elif what == 'show':
            if s == "user":
                self.show(s)
                changelog(s, what)
            elif s == "admin":
                self._print_secure(s)
                changelog(s, what)
            elif s == "owner":
                self.show_private(s)
                changelog(s, what)
            else:
                self.option_input(s)

        if what == 'add':
            if s == "user":
                var = input("\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                if var == "num":
                    x = int(input("\nEnter integer: "))
                    self.add(x, s)
                elif var == "wrd":
                    x = input("\nEnter string: ")
                    self.add(x, s)
                elif var == 'lst':
                    m = input("\nEnter list: ").split(' ')
                    x = [i for i in m]
                    self.add(x, s)
                elif var == 'tup':
                    m = input("\nEnter tuple: ").split(' ')
                    x = [i for i in m]
                    x = tuple(x)
                    self.add(x, s)
            elif s == "admin":
                var = input("\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                if var == "num":
                    x = int(input("\nEnter integer: "))
                    self._add_sec(x, s)
                elif var == "wrd":
                    x = input("\nEnter string: ")
                    self._add_sec(x, s)
                elif var == 'lst':
                    m = input("\nEnter list: ").split(' ')
                    x = [i for i in m]
                    self._add_sec(x, s)
                elif var == 'tup':
                    m = input("\nEnter tuple: ").split(' ')
                    x = [i for i in m]
                    x = tuple(x)
                    self._add_sec(x, s)
            elif s == "owner":
                var = input("\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                if var == "num":
                    x = int(input("\nEnter integer: "))
                    self.add_private(x, s)
                elif var == "wrd":
                    x = input("\nEnter string: ")
                    self.add_private(x, s)
                elif var == 'lst':
                    m = input("\nEnter list: ").split(' ')
                    x = [i for i in m]
                    self.add_private(x, s)
                elif var == 'tup':
                    m = input("\nEnter tuple: ").split(' ')
                    x = [i for i in m]
                    x = tuple(x)
                    self.add_private(x, s)

        elif what == "del":
            if s == "user":
                var = input("\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                if var == "num":
                    x = int(input("\nEnter integer: "))
                    self.delete(x, s)
                elif var == "wrd":
                    x = input("\nEnter string: ")
                    self.delete(x, s)
                elif var == 'lst':
                    x = input("\nEnter list: ").split(' ')
                    x = [i for i in x]
                    self.delete(x, s)
                elif var == 'tup':
                    x = input("\nEnter tuple: ").split(' ')
                    x = [i for i in x]
                    x = tuple(x)
                    self.delete(x, s)

            elif s == "admin":
                var = input("\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                if var == "num":
                    x = int(input("\nEnter integer: "))
                    self._del_sec(x, s)
                elif var == "wrd":
                    x = input("\nEnter string: ")
                    self._del_sec(x, s)
                elif var == 'lst':
                    x = input("\nEnter list: ").split(' ')
                    x = [i for i in x]
                    self._del_sec(x, s)
                elif var == 'tup':
                    x = input("\nEnter tuple: ").split(' ')
                    x = [i for i in x]
                    x = tuple(x)
                    self._del_sec(x, s)

            elif s == "owner":
                var = input("\nObject type: \nnum = Integer \nwrd = String\nlst = List \ntup = Tuple \nback = Back \n")
                if var == "num":
                    x = int(input("\nEnter integer: "))
                    self.del_private(x, s)
                elif var == "wrd":
                    x = input("\nEnter string: ")
                    self.del_private(x, s)
                elif var == 'lst':
                    x = input("\nEnter list: ").split(' ')
                    x = [i for i in x]
                    self.del_private(x, s)
                elif var == 'tup':
                    x = input("\nEnter tuple: ").split(' ')
                    x = [i for i in x]
                    x = tuple(x)
                    self.del_private(x, s)

    def logout(self):
        self.user_option()

    def help_opt(self, s):
        print("\nshow = show items\nadd = Add item\ndel = Delete item\nback = exit")
        self.option_input(s)

    def show(self, s):
        print(self.public)
        self.option_input(s)

    def add(self, x, s):
        if x not in self.public:
            self.public.append(x)
            print(self.public)
            self.option_input(s)
        elif x in self.public:
            c = input('This item already exists! Add it anyway?\ny/n\n')
            if c == 'y':
                self.public.append(x)
                print(self.public)
                self.option_input(s)
            elif c == 'n':
                print(self.public)
                self.option_input(s)

    def delete(self, x, s):
        if x in self.public:
            self.public.remove(x)
            print(self.public)
            self.option_input(s)
        elif x not in self.public:
            input('This item does not exists!')
            print(self.public)
            self.option_input(s)

    def _print_secure(self, s):
        print(self._secure)
        self.option_input(s)

    def _add_sec(self, x, s):
        if x not in self._secure:
            self._secure.append(x)
            print(self._secure)
            self.option_input(s)
        elif x in self._secure:
            c = input('This item already exists! Add it anyway?\ny/n\n')
            if c == 'y':
                self._secure.append(x)
                print(self._secure)
                self.option_input(s)
            elif c == 'n':
                print(self._secure)
                self.option_input(s)

    def _del_sec(self, x, s):
        if x in self._secure:
            self._secure.remove(x)
            print(self._secure)
            self.option_input(s)
        elif x not in self._secure:
            input('This item does not exists!')
            print(self._secure)
            self.option_input(s)

    def show_private(self, s):
        self.__show_pr()
        self.option_input(s)

    def __show_pr(self):
        print(self.__private)

    def add_private(self, arg_data, s):
        self.__add_pr(arg_data, s)

    def __add_pr(self, x, s):
        if x not in self.__private:
            self.__private.append(x)
            print(self.__private)
            self.option_input(s)
        elif x in self.__private:
            c = input('This item already exists! Add it anyway?\ny/n\n')
            if c == 'y':
                self.__private.append(x)
                print(self.__private)
                self.option_input(s)
            elif c == 'n':
                print(self.__private)
                self.option_input(s)

    def del_private(self, arg_data, s):
        self.__del_pr(arg_data, s)
        self.option_input(s)

    def __del_pr(self, x, s):
        if x in self.__private:
            self.__private.remove(x)
            print(self.__private)
            self.option_input(s)
        elif x not in self.__private:
            input('This item does not exists!')
            print(self.__private)
            self.option_input(s)

a = Main()
a.user_option()
