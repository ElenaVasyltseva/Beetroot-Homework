#  Task 2
#  Create a function which takes as input two dicts with structure mentioned above,
#  then computes and returns the total price of stock.
# Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = 0

for k, v in stock.items():
    total_price += stock[k]*prices[k]
    print(f'{k}: {stock[k]*prices[k]}')
print(f'Total price is: {total_price} $')
