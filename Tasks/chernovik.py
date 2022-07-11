# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name 
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         trip_price = self.cost + self.cost_km * km
#         return f'Такси {self.name}, стоимость такси: {trip_price} сом'

# taxi1 = Taxi("Beka", 80, 10)
# taxi2 = Taxi("sema", 80, 6)
# taxi3 = Taxi("manas", 80, 12)

# print(taxi1.get_total_cost(12))
# print(taxi2.get_total_cost(10))
# print(taxi3.get_total_cost(3))

class A:
    def method1(self):
        return "Основной функционал"
    
class B(A):
    def method1(self):
        return "Основной функционал" 

    def __str__(self):
        

    
obj = A()
print(obj.method1)












