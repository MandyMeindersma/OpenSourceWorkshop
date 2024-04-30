def containsDuplicate(nums) -> bool:
        for i in range(len(nums)):
            numbers = set()
            if i in numbers:
                  print(numbers)
                  return True
            else:
                  numbers.add(i)
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