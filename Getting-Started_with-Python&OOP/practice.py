# # inputt=input("enter:")
# # print(inputt[::-1])
# # print(inputt[-1::])
# # print(inputt[:-1:])
# # print(inputt[:1:])
# print("Press 1 to code and press 2 to decode:")
# choice = input()   # safer than int(input())

# user_input = input("Enter text: ")
# words = user_input.split()

# new_words = []

# for word in words:
#     if len(word) >= 3:
#         if choice == "1":
#             new_word = "hjk" + word[1:] + word[0] + "yui"
#         elif choice == "2":
#             temp = word[3:-3]
#             new_word = temp[-1] + temp[:-1]
#         else:
#             print("Invalid choice")
#             break
#     else:
#         new_word = word[::-1]

#     new_words.append(new_word)

# print("Result:", " ".join(new_words))

# problem 1
nums = [10, 20, 30, 40, 50]
# create a newe list where each value is divided by ten
num = []
for i in nums:
    num.append(i / 10)
    # print(i / 10)
    # print(num)
# print(nums)
print(num)
# problem 2
# Remove all even numbers from a list.
for i in num:

    if(i % 2 == 0):
        num.remove(i)
    else:
        print(num)