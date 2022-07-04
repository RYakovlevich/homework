class Price:
    def __init__(self, article, brand, cost, quantity):
        self.article = article
        self.brand = brand
        self.coast = cost
        self.quantity = quantity

    @staticmethod
    def quality():
        print('Отличное предложение')

    @classmethod
    def delivery(cls, article, brand, quantity, delivery):
        return cls(article, brand, quantity, delivery)

Price.quality()
v = Price('op525', 'filtron', 25, 10)

a=Price.delivery('02222', 'bosch', 3, 4)
print(a.article, a.quantity)
print(v.article, v.coast)