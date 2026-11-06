# comprehension: a more concise and efficient way of transforming a container
# to transform is to create a new version of an existing object 

nums = [1, 2, 3]

# old-school
cubes = []
for num in nums:
    cubes.append(num ** 3)

print(nums)
print(cubes)

# modern (with comprehension)
cubes = [num ** 3 for num in nums]

print(nums)
print(cubes)

# we can filter too
odd_cubes = [num ** 3 for num in nums if num % 2]