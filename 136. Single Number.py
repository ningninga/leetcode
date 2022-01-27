# At the first time I read this problem, 'set' occured in my mind due to only one single number.
# The elements in set are non-repeating, so when a duplicate element is found, it can be kicked out with remove();

# Create a set named hashset by set(),
# So first iterate through nums, if num is already in hashset, remove it from the hashset; else add num into the hashset.
# At the end, the only one number left in hashset is the answer.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)
        return list(hashset)[0]  # This is not perfect. But I wrote this at the first time.
      	# return hashset.pop() This one might be more better.