import time
import threading
import random

PRICE_TICKET = 100
DRIVER_SALARY = 30000
BUS_PRICE = 200000
EXPENSES_BUS = 400
SEATS = 42
MONTH = 30
PETROL_PRICE_DAY = 80


class BusStation:
    def __init__(self):
        self.__balance = 1000000
        self.__num_buses = 0
        self.__num_drivers = 0

    def getBalance(self):
        return self.__balance

    def addDriver(self):
        if self.__num_drivers < self.__num_buses * 2:
            self.__num_drivers += 1
        else:
            print('У вас недостаточно автобусов для найма водителя')

    def buyBus(self):
        if self.__balance >= BUS_PRICE:
            self.__num_buses += 1
            self.__balance -= BUS_PRICE
        else:
            print('У вас не хватает денег на покупку автобуса')

    def getNumBuses(self):
        return self.__num_buses

    def getNumDrivers(self):
        return self.__num_drivers

    def calcExpenses(self):
        expenses = self.__num_buses*EXPENSES_BUS + self.__num_drivers*DRIVER_SALARY + PETROL_PRICE_DAY * MONTH * self.__num_buses
        self.__balance -= expenses

        return expenses

    def calcIncome(self):
        clients = random.randint(self.__num_buses * self.__num_drivers * MONTH, self.__num_buses * self.__num_drivers * MONTH * SEATS)
        income = clients * PRICE_TICKET
        self.__balance += income

        return income

    def addInvestments(self, investments):
        self.__balance += investments

        return self.__balance

def calcMonthExpenses(bus_station):
    count_month = 0
    while True:
        time.sleep(MONTH)

        expenses = bus_station.calcExpenses()
        income = bus_station.calcIncome()

        print('Месячные затраты автовокзала: ', expenses)
        print('Месячный доход автовокзала: ', income)
        print('Месячная прибыль автовокзала: ', income - expenses)
        print('Текущий баланс автовокзала - ', bus_station.getBalance())

        if bus_station.getBalance() < 0:
            print("Моделирование системы закончено. Ваш конечный баланс - ", bus_station.getBalance())
            exit()

        count_month += 1
        if count_month == 3 and bus_station.getBalance() > 1000000:
            investments = random.randint(10000, 1000000)
            bus_station.addInvestments(investments)
            print('Ваше предприятие работает успешно! К вам пришел инвестор! Его вложения составили: ', investments)
            print('Текущий баланс автовокзала - ', bus_station.getBalance())
            count_month = 0


if __name__ == '__main__':
    bus_station = BusStation()
    isStart = True
    current_day = 0

    t = threading.Thread(target = calcMonthExpenses, args=(bus_station, ))
    t.start()

    while isStart:
        print('Текущий баланс автовокзала - ', bus_station.getBalance())
        act = input('\n 1. Купить автобус\n 2. Нанять водителя\n 3. Узнать количество водителей\n 4. Узнать количество автобусов\n 5. Выйти\n')

        if act == '1':
            bus_station.buyBus()
        elif act == '2':
            bus_station.addDriver()
        elif act == '3':
            print('Количество водителей: ', bus_station.getNumDrivers())
        elif act == '4':
            print('Количество автобусов: ', bus_station.getNumBuses())
        elif bus_station.getBalance() < 0 or act == '5':
            print("Моделирование системы закончено. Ваш конечный баланс - ", bus_station.getBalance())
            isStart = False
            raise SystemExit
            t.join()
