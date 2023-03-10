import time
import math
num = float(input())
ms = int(input())
time.sleep(ms/1000)
print(f"Square root of {num} after {ms} miliseconds is {math.sqrt(num)}")