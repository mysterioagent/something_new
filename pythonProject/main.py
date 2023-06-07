from datetime import date

from get_xml import take_price
from adder import *
from test import *


class Commodity:

    def __init__(self, name, lot):
        self.in_portfolio = 0
        self.name = name
        self.lot = lot
        self.price = 0

    def buy(self, price, count, portfolio):
        if count % self.lot != 0:
            print("You can buy only a lot")
            return None
        else:
            self.in_portfolio += count
            if self.name in portfolio.commodities:
                portfolio.commodities[self.name] += count
            else:
                portfolio.commodities[self.name] = count
            if portfolio.commodities[self.name] == 0:
                portfolio.commodities_list.remove(self)
            else:
                if self not in portfolio.commodities_list:
                    portfolio.commodities_list.append(self)
            portfolio.volume = portfolio.volume - price * count * (1 + portfolio.commision/100)
        return price * count

    def sell(self, price, count, portfolio):
        if count % self.lot != 0:
            print("You can buy only a lot")
            return None
        else:
            self.in_portfolio -= count
            if self.name in portfolio.commodities:
                portfolio.commodities[self.name] -= count
            else:
                portfolio.commodities[self.name] = -count
            if portfolio.commodities[self.name] == 0:
                portfolio.commodities_list.remove(self)
            else:
                if self not in portfolio.commodities_list:
                    portfolio.commodities_list.append(self)
            portfolio.volume = portfolio.commision + price * count * (1 - portfolio.commision/100)
        return price * count

    def get_prices(self, dt):
        a = take_price(self.name)
        insert_into_table(a)
        delete_upper_rows()
        return select_one_row_from_table(dt, self.name)


class Portfolio:
    def __init__(self, volume, name, commision):
        self.volume = volume
        self.name = name
        self.commodities = {}
        self.commision = commision
        self.commodities_list = []


my_first_portfolio = Portfolio(1100000, 'ИИС Открытие', 0.08)
my_second_portfolio = Portfolio(500000, 'Обычный Открытие', 0.08)
smlt = Commodity('SMLT', 1)
lsrg = Commodity('LSRG', 1)
mtss = Commodity('MTSS', 10)
lkoh = Commodity('LKOH', 1)

lkoh.buy(5231.5, 120, my_first_portfolio)
mtss.buy(307.45, 500, my_second_portfolio)
lsrg.buy(682.4, 200, my_first_portfolio)
smlt.buy(3024.5, 60, my_first_portfolio)

create_table()

for d in my_first_portfolio.commodities.keys() | my_second_portfolio.commodities.keys():
    a = take_price(d)
    insert_into_table(a)

for d in my_first_portfolio.commodities_list + my_second_portfolio.commodities_list:
    print(d.name, d.get_prices(date.today())[5])

delete_upper_rows()
