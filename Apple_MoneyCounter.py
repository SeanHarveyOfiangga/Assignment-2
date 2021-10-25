AmountMoney = int(input("\nEnter the amount of money you have: "))
ApplePrice = int(input("\nEnter how much you will buy the apple: "))
TotalAppleBuyable = AmountMoney // ApplePrice
Change = AmountMoney - (ApplePrice * TotalAppleBuyable)
print(f"\nYou can buy {TotalAppleBuyable} apples and your change is {Change} pesos.")