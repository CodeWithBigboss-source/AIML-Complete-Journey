# Problem#1 
# nums = [1, 2, 3, 4, 5, 6]
# # find how many even and odd numbers are in the list
# odd = []
# even = []
# for i in nums:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# Problem#2
# From 1 to 50: find sum of numbers divisible by 3
# total = 0
# for i in range(1,51):
#     if(i%3==0):
#         total = total + i
#         print(total)
# print(total)

# Problem#3 
# Problem 3: Reverse a number (logic builder)
# num = input("enter number ")
# reversed_num = num[::-1]
# print("reversed number: ",reversed_num)


# Problem#4 
# Problem 4: Find largest number WITHOUT using max()
# nums = [10, 45, 2, 99, 23]
# largest = nums[0]
# for num in nums:
#     if num > largest:
#         largest=num
# print("numbers:",nums)
# print("Largest:",largest)

# Problem#5 
# count digits in a number
# num = 987654
# print(len(str(num)))

# Problem#6
# Check palindrome number
# num = input("enter number:")
# if(num == num[::-1]):
#     print("number is palindrome")
#     print("original number:",num)
#     print("palindrome number:",num[::-1])
# else:
#     print("it is not palindrome")

# Problem#6
# From 1 to 30:
# divisible by 3 → print "Fizz"
# divisible by 5 → print "Buzz"
# both → "FizzBuzz"
# else → number
# num = int(input("enter number:"))
# if(num%3==0 and num%5==0):
#     print("fizzbuzz")
# elif(num%3==0):
#     print("fizz")
# elif(num%5==0):
#     print("buzz")
# else:
#     print(num)

# problem#8
# *
# **
# ***
# ****
# *****
# for i in range (1,6):
#     for j in range (i): 
#         print("*" ,end="")
#     print()

# problem#9
# Find second largest number
numbers = [23, 45, 12, 67, 89, 34, 56, 78, 90, 21]
numbers.sort()  # Sort in ascending order
second_largest = numbers[-2]  # Second last element
print(f"Second largest: {second_largest}")  # 89
        