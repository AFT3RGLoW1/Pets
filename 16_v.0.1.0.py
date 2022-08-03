from datetime import datetime
import datetime as timer_timer
import time
import maskpass
import base64
import requests


def start_page():
    opt = input("Select option below: \nLog in/Sign in\n").lower()
    op.sys_bal()
    if opt == "log in":
        login.log_in()
    if opt == "sign in":
        login.sign_in()
    else:
        start_page()


class LoginPage:
    def __init__(self):
        #   Passwords:  user: HelloKitty, pokemon: 1234
        self._users_db = {"user": [b'SGVsbG9LaXR0eQ==', 5_000, {}], "pokemon": [b'MTIzNA==', 1_000_000, {}]}
        self.__system_bal = 0
        self.system_bal = self.__system_bal
        self.count = 0

    def sign_in(self):
        username = input("Username: ")
        password = input("Password: ")

        encoder = base64.b64encode(password.encode("utf-8"))

        if username in self._users_db.keys():
            print("This username is already taken!")
            self.sign_in()
        if username not in self._users_db.keys():
            self._users_db[username] = [encoder, 0, {}]
            print("Account has been successfully created")
            loger.user_bal_file(username, self._users_db[username][1])
            loger.user_operations(username, operation="just created account")
            start_page()

    def log_in(self):
        if self.count == 3:
            print("Login Failed!\nTry again in:")
            countdown = 10
            if countdown > 0:
                timer = timer_timer.timedelta(seconds=countdown)
                print(timer, end="\r")

                time.sleep(1)
                countdown -= 1
            self.count -= 3
            login.log_in()

        print("\n=========Login Page===========\n")
        username = input("Username : ")
        password = maskpass.advpass("Password: ")

        encoder = base64.b64encode(password.encode("utf-8"))

        if username not in self._users_db.keys():
            print("Input username again!")
            self.count += 1
            self.log_in()
        if encoder == self._users_db[username][0]:
            print("User has been identified, Welcome", username)
            loger.user_bal_file(username, self._users_db[username][1])
            loger.user_operations(username, operation="logged in")
            user.basic_info(username)
        else:
            print("Input password again")
            self.count += 1
            self.log_in()


class UserPage(LoginPage):
    def basic_info(self, username):
        print(f"Your balance: {self._users_db[username][1]} USD")
        self.choose_operation(username)

    @staticmethod
    def choose_operation(username):
        operation = input("Select operation:\nWithdraw\nAdd funds\nConvert\nExchange rates\nExit\n\n").lower()
        if operation == "withdraw":
            loger.user_operations(username, operation)
            op.withdraw(username)
        if operation == "add funds":
            loger.user_operations(username, operation)
            op.add_funds(username)
        if operation == "convert":
            loger.user_operations(username, operation)
            op.convert(username)
        if operation == "exchange rates":
            loger.user_operations(username, operation)
            op.rates(username)
        if operation == "exit":
            loger.user_operations(username, operation)
            op.exit_f()
        else:
            print("Try again")
            user.choose_operation(username)


class Operations(LoginPage):
    def withdraw(self, username):
        withdraw = int(input("Enter the sum to withdraw: "))
        if withdraw > self._users_db[username][1]:
            print("Error! Not enough funds on your balance")
            user.choose_operation(username)
        if withdraw < self._users_db[username][1]:
            self._users_db[username][1] -= withdraw
            print(f"{withdraw} USD were withdrew from your balance\n\nBalance: {self._users_db[username][1]}")
            print(self._users_db)
            loger.user_bal_file(username, self._users_db[username][1])
            user.choose_operation(username)
        else:
            user.choose_operation(username)

    def add_funds(self, username):
        add_sum = int(input("Enter the sum : "))
        self._users_db[username][1] += add_sum
        print(f"{add_sum} USD were added to your balance\n\nBalance: {self._users_db[username][1]}")
        loger.user_bal_file(username, self._users_db[username][1])
        user.choose_operation(username)

    def convert(self, username):
        url = "https://v6.exchangerate-api.com/v6/a147f498250b82594cbbf47f/latest/USD"
        req = requests.get(url)
        src = req.json()
        rates = src["conversion_rates"]
        try:
            print("How much do you want to convert?\n")

            fund = int(input("Enter the sum to convert: "))
            currency = input("Enter currency: ").upper()
            if fund > self._users_db[username][1]:
                print("You don't have enough money!")
                self.convert(username)

            self._users_db[username][1] -= fund
            result = fund * rates[currency]

            print(f"You've got {result} {currency}")

            self._users_db[username][2][currency] = result

            print(self._users_db.values())

            loger.user_currencies(username, result, currency)
            loger.user_bal_file(username, self._users_db[username][1])
            user.choose_operation(username)
        except ValueError:
            self.convert(username)
        except KeyError:
            self.convert(username)

    def rates(self, username):
        url = "https://v6.exchangerate-api.com/v6/a147f498250b82594cbbf47f/latest/USD"
        req = requests.get(url)
        src = req.json()
        rates = src["conversion_rates"]

        currency = input("Enter currency: ").upper()
        if currency in rates.keys():
            print(f"\n1 USD = {rates[currency]} {currency}\n")
            user.choose_operation(username)
        else:
            print("Error!")
            self.rates(username)

    def sys_bal(self):
        self.system_bal -= self.system_bal
        for bal in self._users_db.values():
            self.system_bal += bal[1]
        loger.sys_bal_file(self.system_bal)

    @staticmethod
    def exit_f():
        op.sys_bal()
        start_page()


class Loger(LoginPage):
    @staticmethod
    def user_bal_file(username, balance):
        now = datetime.now()
        time_st = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(f"{username}.txt", "a") as user_bal:
            user_bal.write(f"{time_st} - {balance}\n")

    @staticmethod
    def user_currencies(username, funds, currency):
        with open(f"{username}_currency.txt", "a") as us_cur:
            us_cur.write(f"{funds} {currency} on balance\n")

    @staticmethod
    def sys_bal_file(bal):
        now = datetime.now()
        time_st = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("Sys_Balance.txt", "a",) as sys_bal:
            sys_bal.write(f"{time_st} - {bal} USD\n")

    @staticmethod
    def user_operations(username, operation):
        now = datetime.now()
        time_st = now.strftime("%d/%m/%Y %H:%M:%S")
        info = {}
        with open("Log.txt", "a") as log_f:
            info[time_st] = [username, operation]
            log_f.write(f"{str(info)}\n")


login = LoginPage()
user = UserPage()
op = Operations()
loger = Loger()
if __name__ == "__main__":
    start_page()
