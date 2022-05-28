# import math
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
# class Koło(Figura):
#     def __init__(self,r):
#         self.r=r
#     def obwod(self):
#         return math.pi*2*self.r
#     def pole(self):
#         return math.pi*self.r**2
# f1=Koło(5)
# print(f1.obwod())
# print(f1.pole())
#
# class Trójkąt(Figura):
#     def __init__(self,a):
#         self.a=a
#     def obwod(self):
#         return 3*self.a
#     def pole(self):
#         return (self.a**2*math.sqrt(3))/4
# f2=Trójkąt(6)
# print(f2.obwod())
# print(f2.pole())
#
# class Prostokąt(Figura):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def obwod(self):
#         return 2*self.a+2*self.b
#     def pole(self):
#         return self.a*self.b
# #
# # f3=Prostokąt(5,8)
# # print(f3.obwod())
# # print(f3.pole())
# #
# # class Kwadrat(Prostokąt):
# #     def __init__(self):
# #         self.a=a
# #         self.b=a
# #
# # k1=Kwadrat(5)
# # print(k1.obwod())
# # print(k1.pole())
# #
# # class Równoległobok(Prostokąt):
# #     def __init__(self,a,b,h):
# #         self.a=a
# #         self.b=b
# #         self.h=h
# #     def pole(self):
# #         return self.a*self.h
# #
# # f5 = Rownoleglobok(2, 4, 3)
# # print(f5.pole())
# # print(f5.obwod())
#
# class Vehicle:
#     color = "Biały"
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity=50):
#         return   f"Liczba miejsc siedzących w {self.name} to {capacity} pasażerów"
# class Bus(Vehicle):
#     def seating_capacity(self,capacity=50):
#         return Vehicle.seating_capacity(self,capacity)
#
# bus1 = Bus("szkolne volvo", 180, 12)
# print("Nazwa pojazdu:", bus1.name, "Maks prędkość:", bus1.max_speed, "Odległość:", bus1.mileage)
# print(bus1.seating_capacity())
#
#
# bus1 = Bus("Szkolne Volvo", 180, 12)
# print(bus1.color, bus1.name, "Prędkość:", bus1.max_speed, "Przebieg:", bus1.mileage)
#
# class Car(Vehicle):
#     pass
# car = Car("Audi Q5", 240, 18)
# print(car.color, car.name, "Prędkość:", car.max_speed, "Przebieg:", car.mileage)




class Rectangle:
    def __init__(self, lenght, width):
        self.lenght=lenght
        self.width=width
    def perimeter (self):
        return 2*(self.lenght+self.width)
    def area (self):
        return self.lenght*self.width

    def display(self):
        print("Długośc to " + str(self.lenght) + " szerokość to " + str(self.width) + " obwód to " + str(
            self.perimeter()) + " pole to " + str(self.area()))


obj1 = Rectangle(5, 7)
obj1.display()


class Parallelepipede(Rectangle):
    def __init__(self, lenght, width, height):
        Rectangle.__init__(self, lenght, width)
        self.height = height
        super().__init__(lenght,width)

    def volume(self):
        return self.length * self.width * self.height
