string = input()
lower = 0
upper = 0
for i in string:
    if(i.islower()):
        lower += 1
    else:
        upper += 1

print(lower)
print(upper)