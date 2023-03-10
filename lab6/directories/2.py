import os

name = input()
print1 = print("Existence -", os.access(name, os.F_OK))
print2 = print("Readability -", os.access(name, os.R_OK))
print3 = print("Writability -", os.access(name, os.W_OK))
print4 = print("Executability -", os.access(name, os.X_OK))
