print("Welcome to KBC")
print("Winning amout is 300,000,000")
Questions=[["What is the capital of Japan?","(a)Seoul","(b)Pyongyang","(c)Beijing","(d)Tokyo"],
           ["What is capital of Pakistan?","(a)Isb","(b)Khi","(c)Lhr","(d)Rwp"],
           ["What is capital of India?","(a)Isb","(b)New Delhi","(c)Kanpu","(d)Up"],
           ["What is capital of Canada?","(a)Ottawa","(b)Toronto","(c)Myanmar","(d)Rwp"],
           ["What is capital of USA?","(a)New York","(b)LV","(c)LA","(d)Washington DC"],
           ["What is capital of UK?","(a)London","(b)Khi","(c)Lisbon","(d)Rwp"],
           ["What is capital of UAE?","(a)Malta","(b)Riyadh","(c)Abu Dhabi","(d)Dubai"],
           ["What is capital of KSA?","(a)Madinah","(b)Riyadh","(c)Jeddah","(d)Makkah"],
           ["What is capital of Iran?","(a)Tokyo","(b)Faris","(c)Baghdad","(d)Tehran"],
           ["What is capital of Iraq?","(a)Baghdad","(b)Busra","(c)Kashmir","(d)Mp"]]
answers=["d","a","b","a","d","a","c","b","d","a"]
prize=[1000,3000,10000,20000,40000,100000,1000000,5000000,10000000,30000000]
for i in range(len(Questions)):
    print(f"Question{i+1}:{Questions[i][0]}")
    for option in Questions[i][1:]:
        print(option)
    answer=input("Enter option:")
    if(answer==answers[i]):
        prizes=prize[i]
        print("Correct answer! You have won ",prizes)
    else:
        print("Wrong answer. Better luck next time.")
        break