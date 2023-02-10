def spy_game(nums):
    for i in nums: 
        if i == 7: 
          num = nums[:nums.index(i)]    #nums = [1, 0, 2, 7, 0, 1]           
    if len(num) == len(nums):           #nums = [0, 0, 0, 7, 0, 1]           
        return False                    #nums = [0, 0, 2, 7, 0, 1]           
    cnt = 0
    for j in num:
        if j == 0: cnt += 1
    if cnt >= 2: 
        return True
    else: 
        return False