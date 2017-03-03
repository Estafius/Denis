f = open('food.txt')
print(f.read())
f.close()

f = open('food.txt')
for line in f:
     print(line, end=" ")
f.close()