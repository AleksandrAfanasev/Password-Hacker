# the following line creates a list from the input, do not modify it, please
prices = [float(price) for price in input().split()]
prices = sorted(prices, reverse=True)
print(prices)
