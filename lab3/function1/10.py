def unique(list):
    arr = []
    for i in list:
        if i not in arr: arr.append(i)      #s =[1, 2, 3, 1, 1, 2, 0, 5]
    print(arr)