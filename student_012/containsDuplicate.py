def containsDuplicate(nums) -> bool:
        hashBrowns = {}
        for i in range(len(nums)):
                if nums[i] not in hashBrowns:
                       hashBrowns[nums[i]]= 1
                else:
                        return True
        return False

# Test Cases:

### Example 1:
print(containsDuplicate([1,2,3,1]))
print("Expected: true")
print("")

### Example 2:
print(containsDuplicate([1,2,3,4]))
print("Expected: false")
print("")

### Example 3:
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print("Expected: true")
print("")