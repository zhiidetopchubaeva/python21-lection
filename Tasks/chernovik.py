class Terminal:

    def _check_card_num(self, card_num):
        if len(card_num) == 16 and card_num.isdigit():
            return True
        else:
            print("Неправильный номер карты, введите цифры!")

    def _check_pin(self, pin):
        if len(pin) == 4 and pin.isdigit():
            return True
        else:
            print("Неправильный пин, введите цифры!")
            
    def __init__(self, card_num, pin):
        if self._check_card_num(card_num=card_num) and self._check_pin(pin=pin):
            self.__card_num = card_num
            self.__pin = pin
            self.balance = 0
        else:
            print("Ваша карта не найдена!")

    def _validate_put(self, pin):
        if self.__pin == pin:
            return True
        else:
            return False

    def put(self, pin, balance):
        if self._validate_put(pin=pin):
            self.balance += balance
            print(f"Ваш баланс составляет {self.balance} сом после пополнения")
        else:
            print("Неправильно ввели пин код!!!")

    def _check_balance(self, balance):
        if balance % 10 == 0:
            return True
        else:
            print("Введите правильную сумму денег(10, 100, 200, 5000): ")
            return False

    def _validate_balance(self, balance):
        if self.balance < balance:
            print("Недостаточно денег на балансе!")
            return False
        else:
            return True
    
    def get_money(self, pin, balance):
        if self._validate_put(pin=pin):
            if self._check_balance(balance=balance) and self._validate_balance(balance=balance):
                self.balance -= balance
                print(f"Ваш баланс составляет {self.balance} сом после вывода средств")
        else:
            print("Неправильный пин код!!!")


card = Terminal(card_num="1234567891011121", pin="1234")
card.put(pin="1234", balance=1000)
card.get_money(pin="1234", balance=800)
card.put(pin="1234", balance=210)
print(f'Баланс карты составляет {card.balance} сом')


        
        












