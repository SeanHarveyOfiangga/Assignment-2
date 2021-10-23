AppleCount = int(input("How many Apples do you want to buy? "))
OrangeCount = int(input("\nHow many Orange do you want to buy? "))

PriceApple = 25
PriceOrange = 20

TotalApple = AppleCount * PriceApple
TotalOrange = OrangeCount * PriceOrange

print(f"\nAmount due for {AppleCount} Apples:${TotalApple}")
print(f"Amount due for {OrangeCount} Oranges:${TotalOrange}")

Overalltotal = TotalApple + TotalOrange
print(f"\nThe total amount is ${Overalltotal}")