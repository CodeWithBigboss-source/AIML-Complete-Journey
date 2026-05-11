# st = input("enter code:")
# words = st.split()
# print(words)

# coding = True

# if(coding):
#     nwords = []
#     for word in words:
#         if(len(word) >= 3):
#             r1 = "dsf"
#             r2 = "jkr"
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])

#     print("".join(nwords))

# else:
#     nwords = []
#     for word in words:
#         if(len(word) >= 3):
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])

#     print("".join(nwords))
# user_input=input("enter code:")
# words=user_input.split()
# new_words=[]
# for word in words:

    
#     if(len(word)>=3):
#         random1="hjk"
#         random2="yui"
#         code1=random1+word[1:]+word[0]+random2
#         new_words.append(code1)
#     else:
#         code2=word[::-1]
#         new_words.append(code2)

# print("".join(new_words))

print("Press 1 to code and press 2 to decode:")
choice = input()   # safer than int(input())

user_input = input("Enter text: ")
words = user_input.split()

new_words = []

for word in words:
    if len(word) >= 3:
        if choice == "1":
            new_word = "hjk" + word[1:] + word[0] + "yui"
        elif choice == "2":
            temp = word[3:-3]
            new_word = temp[-1] + temp[:-1]
        else:
            print("Invalid choice")
            break
    else:
        new_word = word[::-1]

    new_words.append(new_word)

print("Result:", " ".join(new_words))

  