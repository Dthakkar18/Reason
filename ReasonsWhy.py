
#line = int(input("Choose a number between 1 - 365: "))
line = 3


file = open('Reasons.txt', 'r')
x = file.readlines()[0]
print(x)