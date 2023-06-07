from get_xml import take_price

class Commodity:

    def __init__(self, name, lot):
        self.in_portfolio = 0
        self.name = name
        self.lot = lot

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
            portfolio.volume -= price * count
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
            portfolio.volume += price * count
        return price * count


class Portfolio:
    def __init__(self, volume, name):
        self.volume = volume
        self.name = name
        self.commodities = {}


my_first_portfolio = Portfolio(1100000, 'ИИС Открытие')
my_second_portfolio = Portfolio(500000, 'Обычный Открытие')
smlt = Commodity('SMLT', 1)
lsrg = Commodity('LSRG', 1)
mtss = Commodity('MTSS', 10)
lkoh = Commodity('LKOH', 1)

lkoh.buy(5231.5, 120, my_first_portfolio)
mtss.buy(307.45, 500, my_second_portfolio)
lsrg.buy(682.4, 200, my_first_portfolio)
smlt.buy(3024.5, 60, my_first_portfolio)

print(my_first_portfolio.__dict__)
print(my_second_portfolio.__dict__)

for d in my_first_portfolio.commodities.keys():
    print(take_price(d))

