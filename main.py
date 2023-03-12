import os
from datetime import datetime
import csv

#Pizza superclass
class Pizza:

    def __init__(self, descp, costp, namep) -> None:
        super().__init__()
        self.description = descp
        self.cost = costp
        self.name = namep

    # Getters to get values from encapsulated variables
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

    def get_name(self):
        return self.name

class Klasik(Pizza):
    # Pizza subclass
    pizza_desc = "Herkesin begendigi klasik pizza."
    pizza_price = 80
    pizza_name = 'Klasik'

    def __init__(self) -> None:
        super().__init__(self.pizza_desc, self.pizza_price, self.pizza_name)


class Margarita(Pizza):
    # Pizza subclass
    pizza_desc = "Gurme Margarita pizza."
    pizza_price = 55
    pizza_name = 'Margarita'

    def __init__(self) -> None:
        super().__init__(self.pizza_desc, self.pizza_price, self.pizza_name)


class TurkPizza(Pizza):
    # Pizza subclass
    pizza_desc = "Damak tadimiza uygun Turk usulu pizza."
    pizza_price = 75
    pizza_name = 'TurkPizza'

    def __init__(self) -> None:
        super().__init__(self.pizza_desc, self.pizza_price, self.pizza_name)


class SadePizza(Pizza):
    # Pizza subclass
    pizza_desc = "Malzemesiz, sade pizza."
    pizza_price = 40
    pizza_name = 'SadePizza'

    def __init__(self) -> None:
        super().__init__(self.pizza_desc, self.pizza_price, self.pizza_name)


class Decorator(Pizza):
    # Decorator super class

    def __init__(self, descp, costp, namep, aa) -> None:
        # super().__init__()
        self.decorator_description = descp
        self.decorator_cost = costp
        self.decorator_name = namep
        Pizza = aa
        super().__init__(aa.description, aa.cost, aa.name)

    #Getter functions for encapsulation principle of OOP.
    def get_cost(self):
        return self.decorator_cost + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.decorator_description + \
            '\nPizzanız: ' + Pizza.get_description(self)

    def get_name(self):
        return self.decorator_name


class Zeytin(Decorator):
    # Decorator subclass
    decorator_desc = "Siyah ve yesil zeytin ile susleyin."
    decorator_cost = 5
    decorator_name = 'Zeytin'

    def __init__(self, aa) -> None:
        super().__init__(self.decorator_desc, self.decorator_cost, self.decorator_name, aa)


class Mantar(Decorator):
    # Decorator subclass
    decorator_desc = "Cesit cesit mantarlar ile pizzaniza renk katin."
    decorator_cost = 20
    decorator_name = 'Mantar'

    def __init__(self, aa) -> None:
        super().__init__(self.decorator_desc, self.decorator_cost, self.decorator_name, aa)


class KeciPeyniri(Decorator):
    # Decorator subclass
    decorator_desc = "Dogal Keci peyniri ile zengin lezzet."
    decorator_cost = 25
    decorator_name = 'KeciPeyniri'

    def __init__(self, aa) -> None:
        super().__init__(self.decorator_desc, self.decorator_cost, self.decorator_name, aa)


class Et(Decorator):
    # Decorator subclass
    decorator_desc = "Pizzaninizi et ile zenginlestirin."
    decorator_cost = 40
    decorator_name = 'Et'

    def __init__(self, aa) -> None:
        super().__init__(self.decorator_desc, self.decorator_cost, self.decorator_name, aa)


class Sogan(Decorator):
    # Decorator subclass
    decorator_desc = "Karamelize ozel sogan."
    decorator_cost = 7
    decorator_name = 'Sogan'

    def __init__(self, aa) -> None:
        super().__init__(self.decorator_desc, self.decorator_cost, self.decorator_name, aa)


class Misir(Decorator):
    # Decorator subclass
    decorator_desc = "Bol misir ile pizzanizin tadini ikiye katlayin"
    decorator_cost = 5
    decorator_name = 'Misir'

    def __init__(self, aa) -> None:
        super().__init__(self.decorator_desc, self.decorator_cost, self.decorator_name, aa)


class Main:

    def writeToCsv(self, name, tcid, cc_no, cc_pswd, items, cost):
        #The function to write output to a CSV database

        fileExists = False
        # If database file does not exist before we access it, we will write header first, hence we check it before accessing.
        if os.path.exists('Orders_Database.csv'):
            fileExists = True

        #Get a datetime string
        now = datetime.now()  # get the current date and time
        dateStr = now.strftime('%H:%M %d/%m/%Y')

        #Prepare data to write
        header = ['Isim Soyisim', 'TC Kimlik no', 'Kredi Karti numarasi', 'Kredi Karti sifresi', 'Alinan urunler',
                  'Siparis tutari', 'Siparis Tarihi']
        data = [name, tcid, cc_no, cc_pswd, items, (str(cost) + ' TL'), dateStr]

        #Open database in append mode and write data
        with open('Orders_Database.csv', 'a', encoding='UTF8') as cs:
            # create the csv writer
            writer = csv.writer(cs)

            if not fileExists:
                writer.writerow(header)

            # write the data
            writer.writerow(data)


    def main():
        print('Menu:')

        file = open("menu.txt", "r", encoding="utf-8")
        menu = file.read()
        file.close()
        print(menu)

        isPizzaSelected = False
        isDecorationSelected = False
        customerName = None
        TC_ID = None
        creditCardNum = None
        creditCardPswd = None

        while not isPizzaSelected or not isDecorationSelected:
            user_input = int(input("Menuden Pizza turunu secerek karsilik gelen sayiyi giriniz: " if not isPizzaSelected else "Menuden ek malzeme turunu secerek karsilik gelen sayiyi giriniz: "))
            if not isPizzaSelected and user_input > 10:
                print('Please select a pizza first.')
                continue

            if user_input == 1:
                pizza = Klasik()
                print("Secilen Pizza: Klasik")
                print(pizza.get_description())
                isPizzaSelected = True
                continue
            elif user_input == 2:
                pizza = Margarita()
                print("Secilen Pizza: Margarita")
                print(pizza.get_description())
                isPizzaSelected = True
                continue
            elif user_input == 3:
                pizza = TurkPizza()
                print("Secilen Pizza: Türk Pizza")
                print(pizza.get_description())
                isPizzaSelected = True
                continue
            elif user_input == 4:
                pizza = SadePizza()
                print("Secilen Pizza: Sade Pizza")
                print(pizza.get_description())
                isPizzaSelected = True
                continue
            elif user_input == 11:
                decoration = Zeytin(pizza)
                print("Secilen ek malzeme: Zeytin")
                isDecorationSelected = True
                continue
            elif user_input == 12:
                decoration = Mantar(pizza)
                print("Secilen ek malzeme: Mantar")
                isDecorationSelected = True
                continue
            elif user_input == 13:
                decoration = KeciPeyniri(pizza)
                print("Secilen ek malzeme: Keçi Peyniri")
                isDecorationSelected = True
                continue
            elif user_input == 14:
                decoration = Et(pizza)
                print("Secilen ek malzeme: Et")
                isDecorationSelected = True
                continue
            elif user_input == 15:
                decoration = Sogan(pizza)
                print("Secilen ek malzeme: Soğan")
                isDecorationSelected = True
                continue
            elif user_input == 16:
                decoration = Misir(pizza)
                print("Secilen ek malzeme: Mısır")
                isDecorationSelected = True
                continue
            else:
                print("Gecersiz giris!")

        print(decoration.get_description())
        total = decoration.get_cost()
        print('Sectiginiz urunlerin toplam fiyati: ', total, " TL")
        print('Lutfen bilgilerinizi giriniz')
        print('Isim soyisim: ')
        customerName = input()

        print('TC Kimlik no: ')
        TC_ID = input()

        print('Kredi karti numarasi: ')
        creditCardNum = input()

        print('Kredi karti sifresi: ')
        creditCardPswd = input()

        Main.writeToCsv(None, customerName, TC_ID, creditCardNum, creditCardPswd, (pizza.get_name() + ', ' + decoration.get_name()), total)

        print('Siparisiniz icin tesekkurler.')



Main.main()

