print(f"\nPrice for an Apple is 20PHP each.")

AmountMoney = int(input("\nEnter the amount of money you have: "))
ApplePrice = 20
TotalAppleBuyable = AmountMoney // ApplePrice
Change = AmountMoney - (ApplePrice * TotalAppleBuyable)
print(f"\nYou can buy {TotalAppleBuyable} apples and your change is {Change} pesos.")