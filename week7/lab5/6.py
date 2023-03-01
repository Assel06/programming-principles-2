import re
s = input()
t = re.sub("[\s,.]", ":", s)
print(t)