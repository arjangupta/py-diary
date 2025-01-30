def create_staircase_B(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

def create_staircase_A(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets

def main():
    nums = [1, 2, 3, 4, 5, 6]
    print(create_staircase_A(nums))
    print(create_staircase_B(nums))
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(create_staircase_A(nums))
    print(create_staircase_B(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(create_staircase_A(nums))
    print(create_staircase_B(nums))

if __name__ == "__main__":
  main()