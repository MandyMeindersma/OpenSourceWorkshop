def containsDuplicate(nums) -> bool:
    if len(set(nums)) == len(nums):
        return False
    return True

# Test Cases:

### Example 1:
print(containsDuplicate([1,2,3,1]))
print("Expected: True")
print("")

### Example 2:
print(containsDuplicate([1,2,3,4]))
print("Expected: False")
print("")

### Example 3:
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print("Expected: True")
print("")