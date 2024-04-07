class Solution(object):
    def twoSum(self, nums, target):
        list = []
        length = len(nums)
        for x in range(0,length):
            for y in range(length):
                if(x != y):
                    if(nums[x] + nums[y] == target):
                        list.append(x)
                        list.append(y)
        list.sort()
        new_list = []
        for x in range(len(list)):
            if(len(list) - 1 != x):
                if(list[x] == list[x+1]):
                    new_list.append(list[x])
        return new_list