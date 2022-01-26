class Solution(object):
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                print("first : ", num)
                first = num
            elif num <= second:
                print("second: ", num)
                second = num
            elif num > second:
                print("finish: ", num)
                return True
        return False


#print(Solution().increasingTriplet([1,2,3,4,5]))
#print(Solution().increasingTriplet([20,100,10,12,5,13]))
#print(Solution().increasingTriplet([2,1,5,0,3]))

print(Solution().increasingTriplet([1,1,-2,6]))