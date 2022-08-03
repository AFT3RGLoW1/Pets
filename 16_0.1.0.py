from datetime import datetime   # імпорт модуля для логера
import datetime as timer_timer  # імпорт модуля datetime та зміна його назви для роботи таймера
import time    # імпорт модуля для роботи таймера
import maskpass     # імпорт модуля для маскування введеного паролю в реальному часі
import base64   # імпорт модуля для шифрування паролів юзерів
import requests     # імпорт модуля для парсингу курсу валют


def start_page():
    # зайти в існуючий акаунт або створити новий
    opt = input("Select option below: \n1 - Log in\n2 - Sign in\n")
    op.sys_bal()
    if opt == "1":
        start.log_in()
    if opt == "2":
        start.sign_in()
    else:
        start_page()


class LoginPage:
    def __init__(self):
        #   Passwords:  user: HelloKitty, pokemon: 1234
        self._users_db = {"user": [b'SGVsbG9LaXR0eQ==', 5_000, {}], "pokemon": [b'MTIzNA==', 1_000_000, {}]}
        self.__system_bal = 0
        self.system_bal = self.__system_bal
        self.count = 0  # кількість виконаних спроб входу


class Start(LoginPage):
    def sign_in(self):
        print("\n========Sign in Page==========\n")
        username = input("Username: ")
        password = input("Password: ")

        # шифруємо отриманий пароль
        encoder = base64.b64encode(password.encode("utf-8"))

        # перевірка наявності юзера в словнику
        if username in login._users_db.keys():
            print("This username is already taken!")
            self.sign_in()
        # якщо юзера не існує, додаємо отримані дані в словник
        if username not in login._users_db.keys():
            # в списку створюємо дефолтні значення для балансу і зберігання валюти
            login._users_db[username] = [encoder, 0, {}]
            print("Account has been successfully created")
            # запис дії та балансу в лог
            loger.user_bal_file(username, login._users_db[username][1])
            loger.user_operations(username, operation="just created account")
            start_page()

    def log_in(self):
        # якщо було виконано 3 невдалі спроби логіну, запускаємо таймер
        if self.count == 3:
            print("Login Failed!\nTry again in:")
            countdown = 10
            if countdown > 0:
                timer = timer_timer.timedelta(seconds=countdown)
                print(timer, end="\r")

                time.sleep(1)
                countdown -= 1
            self.count -= 3
            start.log_in()

        print("\n=========Login Page===========\n")
        username = input("Username : ")
        password = maskpass.advpass("Password: ")

        # шифруємо пароль для порівняння отриманих хешів
        encoder = base64.b64encode(password.encode("utf-8"))

        if username not in login._users_db.keys():
            print("Input username again!")
            self.count += 1
            self.log_in()
        if encoder == login._users_db[username][0]:
            print("\nUser has been identified, Welcome", username)
            # запис дії та балансу в лог
            loger.user_bal_file(username, login._users_db[username][1])
            loger.user_operations(username, operation="logged in")
            user.basic_info(username)
        else:
            print("Input password again")
            self.count += 1
            self.log_in()


class UserPage(LoginPage):
    # виводимо баланс юзера на екран
    @staticmethod
    def basic_info(username):
        print(f"\nYour balance: {login._users_db[username][1]} USD")
        user.choose_operation(username)

    @staticmethod
    # пропонуємо юзеру обрати дію
    def choose_operation(username):
        operation = input("\nEnter operation number:\n1 - Withdraw\n2 - Add funds\n3 - Convert\n4 - Exchange rates\n0 - Exit\n\n").lower()
        if operation == "1":
            # обрану дію записуємо в лог операцій юзера і переходимо до виконання дії
            loger.user_operations(username, operation="Withdraw")
            op.withdraw(username)
        if operation == "2":
            loger.user_operations(username, operation="Add funds")
            op.add_funds(username)
        if operation == "3":
            loger.user_operations(username, operation="Convert")
            op.convert(username)
        if operation == "4":
            loger.user_operations(username, operation="Exchange rates")
            op.rates(username)
        if operation == "0":
            loger.user_operations(username, operation="Exit")
            op.exit_f()
        else:
            print("Try again")
            user.choose_operation(username)


class Operations(LoginPage):
    def withdraw(self, username):
        try:
            print("Enter 0 to return to menu")
            withdraw = int(input("Enter the sum to withdraw: "))
            # якщо введена сума для зняття більша від наявних коштів - відміняємо дію
            if withdraw > login._users_db[username][1]:
                print("Error! Not enough funds on your balance")
                user.choose_operation(username)
            if withdraw < login._users_db[username][1]:
                # обновлюємо баланс юзера
                login._users_db[username][1] -= withdraw
                print(f"{withdraw} USD were withdrew from your balance\n\nBalance: {login._users_db[username][1]}")
                # записуємо дані про баланс юзера в лог цього юзера
                loger.user_bal_file(username, login._users_db[username][1])
                user.choose_operation(username)
            else:
                user.choose_operation(username)
        except ValueError:
            print("Error!")
            self.withdraw(username)

    def add_funds(self, username):
        # поповнення балансу юзера
        print("Enter 0 to return to menu")
        try:
            add_sum = int(input("Enter the sum : "))
            if add_sum == 0:
                # якщо юзер передумав повертаємо його в меню
                user.choose_operation(username)
            # обновлюємо баланс юзера
            login._users_db[username][1] += add_sum
            print(f"{add_sum} USD were added to your balance\n\nBalance: {login._users_db[username][1]}")
            # записуємо дані про баланс юзера в лог цього юзера
            loger.user_bal_file(username, login._users_db[username][1])
            user.choose_operation(username)
        except ValueError:
            print("Error!")
            self.add_funds(username)

    def convert(self, username):
        # дістаємо JSON з курсами валют
        url = "https://v6.exchangerate-api.com/v6/a147f498250b82594cbbf47f/latest/USD"
        req = requests.get(url)
        src = req.json()
        # створюємо словник тільки з курсами валют
        rates = src["conversion_rates"]
        try:
            print("How much do you want to convert?\n")
            print("Enter 0 to return to menu")

            fund = int(input("Enter the sum to convert: "))
            if fund == 0:
                # якщо юзер передумав повертаємо його в меню
                user.choose_operation(username)
            currency = input("Enter currency: ").upper()
            # якщо введена сума для зняття більша від наявних коштів - відміняємо дію
            if fund > login._users_db[username][1]:
                print("You don't have enough money!")
                self.convert(username)
            # обновлюємо баланс юзера
            login._users_db[username][1] -= fund
            result = fund * rates[currency]

            print(f"You've got {result} {currency}")
            # додаємо назву валюти та її кількість в словник для валют
            login._users_db[username][2][currency] = result
            # записуємо дані про баланс юзера та його валютний баланс в відповідні логи цього юзера
            loger.user_currencies(username, result, currency)
            loger.user_bal_file(username, login._users_db[username][1])
            user.choose_operation(username)
        except ValueError:
            print("Error!")
            self.convert(username)
        except KeyError:
            print("Error!")
            self.convert(username)

    def rates(self, username):
        # дістаємо JSON з курсами валют
        url = "https://v6.exchangerate-api.com/v6/a147f498250b82594cbbf47f/latest/USD"
        req = requests.get(url)
        src = req.json()
        # створюємо словник тільки з курсами валют
        rates = src["conversion_rates"]
        # запитуємо про валюту яка цікавить юзера
        try:
            print("Enter 0 to return to menu")
            currency = input("Enter currency: ").upper()
            if currency == 0:
                # якщо юзер передумав повертаємо його в меню
                user.choose_operation(username)
            if currency in rates.keys():
                print(f"\n1 USD = {rates[currency]} {currency}\n")
                user.choose_operation(username)
                print(f"Error!")
                user.choose_operation(username)
        except KeyError:
            print("Error!")
            self.rates(username)

    @staticmethod
    def sys_bal():
        # дізнаємося баланс системи та записуємо в лог
        login.system_bal -= login.system_bal
        for bal in login._users_db.values():
            login.system_bal += bal[1]
        # записуємо дані про баланс системи
        loger.sys_bal_file(login.system_bal)

    @staticmethod
    # вихід з акаунту
    def exit_f():
        # записуємо дані про баланс системи на виході
        op.sys_bal()
        start_page()


class Loger(LoginPage):
    # клас з методами для створення і заповнення логів
    @staticmethod
    # записуємо дані про баланс юзера в лог цього юзера
    def user_bal_file(username, balance):
        now = datetime.now()
        time_st = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(f"{username}.txt", "a") as user_bal:
            user_bal.write(f"{time_st} - {balance}\n")

    @staticmethod
    # записуємо дані про валютний баланс юзера в валютний лог цього юзера
    def user_currencies(username, funds, currency):
        with open(f"{username}_currency.txt", "a") as us_cur:
            us_cur.write(f"{funds} {currency} on balance\n")

    @staticmethod
    # записуємо дані про баланс системи
    def sys_bal_file(bal):
        now = datetime.now()
        time_st = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("Sys_Balance.txt", "a",) as sys_bal:
            sys_bal.write(f"{time_st} - {bal} USD\n")

    @staticmethod
    # записуємо дані про виконані операції юзера в лог цього юзера
    def user_operations(username, operation):
        now = datetime.now()
        time_st = now.strftime("%d/%m/%Y %H:%M:%S")
        info = {}
        with open("Log.txt", "a") as log_f:
            info[time_st] = [username, operation]
            log_f.write(f"{str(info)}\n")


login = LoginPage()
start = Start()
user = UserPage()
op = Operations()
loger = Loger()

if __name__ == "__main__":
    start_page()
