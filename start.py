# from main import Human
#
#
# c = Human("Valera", 22, 1000, "House")
# c.earn_money()
# c.info()

def digitize(n):
    return [int(i) for i in str(n)[::-1]]

s = 35231
print(digitize(s))
print()

