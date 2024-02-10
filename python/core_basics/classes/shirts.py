class Shirt:
    def __init__(self, s_color, s_size, s_style, s_price):
        self.color = s_color
        self.size  = s_size
        self.style = s_style
        self.price = s_price
    
    def change_price(self,new_price):
        self.price = new_price
    
    def discount(self, discount):
        # 100 - (100 * 0.1) = 100 - 10 = 90
        # return (self.price - (self.price * discount))
        return self.price * (1 - discount)
    
    def print_ShirtInfo(self):
        print("#####################################")
        print("Color is: " + self.color)
        print("Size  is: " + self.size)
        print("Style is: " + self.style)
        print("Price is:--> $" + str(self.price))
        print("#####################################")