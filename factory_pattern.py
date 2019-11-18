class Button(object):
    html = ""

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img></img>"


class Input(Button):
    html = "<input></input>"


class Flash(Button):
    html = "<obj></obj>"


class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()


button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(button_obj.create_button(b).get_html())

z="sdfsf"
print(z.capitalize())

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'''"""

#
# class PizzaShop:
#
#     def __init__(self, product):
#         self.product = product
#
#     def showProducts(self):
#         p = self.product.get_products(self)
#         print(p)
#
#
# class Pepsi:
#
#     def __init__(self):
#         self.price = 20
#         self.name = "pepsi"
#
#     def __str__(self):
#         x=self.name+ " "+str(self.price)
#         return x
#
# class PepsiFactory:
#
#     def get_products(self):
#         return Pepsi()
#
# c=PizzaShop(PepsiFactory)
# c.showProducts()
# # z=Pepsi()
# # print(z)
