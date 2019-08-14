import sys
n = int(input('enter n : '))
sum = 0
a = n
while a > 0 :
    sum += 1
    a //= 10
print(sum)
