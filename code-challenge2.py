amount = eval(input("Enter the total amount: ₱"))

b1000 = int(amount // 1000)
amount = amount - (b1000 * 1000)

b500 = int(amount // 500)
amount = amount - (b500 * 500)

b200 = int(amount // 200)
amount = amount - (b200 * 200)

b100 = int(amount // 100)
amount = amount - (b100 * 100)

b50 = int(amount // 50)
amount = amount - (b50 * 50)

b20 = int(amount // 20)
amount = amount - (b20 * 20)

c10 = int(amount // 10)
amount = amount - (c10 * 10)

c5 = int(amount // 5)
amount = amount - (c5 * 5)

c1 = int(amount // 1)
amount = amount - (c1 * 1)

c025 = int(amount // 0.25)
amount = amount - (c025 * 0.25)

print("₱1000 x ", str(b1000))
print("₱500  x ", str(b500))
print("₱200  x ", str(b200))
print("₱100  x ", str(b100))
print("₱50   x ", str(b50))
print("₱20   x ", str(b20))
print("₱10   x ", str(c10))
print("₱5    x ", str(c5))
print("₱1    x ", str(c1))
print("₱0.25 x ", str(c025))
