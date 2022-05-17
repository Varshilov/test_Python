class ProductBuilder:
    def __init__(self, product):
        self.products = product.split(" - ")
        self.title = "".join(self.products[0])
        self.quantity = ", ".join(self.products[1:])

    def __str__(self):
        return "{}, {}".format(self.title.encode("utf-8"),
                               self.quantity.encode("utf-8"))
