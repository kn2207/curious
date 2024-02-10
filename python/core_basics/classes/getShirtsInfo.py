from shirts import Shirt

new_Shirt = Shirt('Yellow','Large','Short Sleeve',35)

print("Here is the smart shirt!")
new_Shirt.print_ShirtInfo()

new_Shirt.price = new_Shirt.discount(.25)
print("Got lucky - Got a great 25% discount")

new_Shirt.print_ShirtInfo()