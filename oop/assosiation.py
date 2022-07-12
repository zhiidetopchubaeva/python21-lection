"=================== Ассоциация ==========================="
# Ассоциация - принцип ООП, в котором два класса друг с другом связаны 
# Ассоциация делится на 2 принципа:
# 1 агрегация (более слабая связь)
# 2 композиция (болеее сильная связь)


class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100


class Iphone:
    def __init__(self, color:str):
        self.color = color
        self.battery = Battery()
        # когда мы создаем объект от другого класса прям внутри другого - тесная связь(композиция)
        

class Nokia:
    def __init__(self, color:str, battery:Battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный вне класса объект - агрегация


iphone = Iphone("gold")

del iphone # Объект батарейки удаляется вместе с объектом iphone
"композиция"

battery = Battery()
nokia = Nokia("white", battery)

del nokia # удаляется только объект nokia, объект батарейки сохраняется
"агрегация"


