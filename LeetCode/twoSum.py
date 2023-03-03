# This Function returns indexes of the elements
def twoSum(nums, target):
        cache = set()
        correct_nums = []
        for i in nums:
            if target - i in cache:
                correct_nums += [target - i, i]    
            cache.add(i)
            
        index = []
        for j, values in enumerate(nums):
             if values in correct_nums:
                  index.append(j)
        return index

print(twoSum([2,7,11,15], 9))