def has_33(nums):
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i-1] == 3:     #nums = [1, 2, 3, 3]
            return True                         #nums = [1, 3, 2, 3]
    else:                                       #nums = [1, 0, 0]
        return False