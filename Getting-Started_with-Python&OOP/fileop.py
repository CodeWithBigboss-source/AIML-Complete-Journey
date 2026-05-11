# f=open("myfile.txt","a")
# f.write("\nwe have learned how to create a file in python and how to read write data in it.")
# print(f)
# text=f.read()
# print(text)
# f.close()

# print("now if we use append then f.write() will be added")
# with open("myfile4.txt","a") as f:
#     f.write("this is a new file")
    
# f=open("myfile.txt","r")
# while True:
#     line=f.readline()
#     print(line)
#     if not(line):
#         print(line,type(line))
#         break

# with open("myfile.txt","r")as f:
#     while True:
#         line=f.readline()
#         print(line)
#         if not line:
#             break
#     print(type(line))
# with open("myfile.txt","r")as f:
#     while True:
#         line=f.readline()
#         if not line:
#             break
        
#         i=0
#         marks=line.split()
#         print(f"marks of student 1 in english {marks[i]}")
#         print(f"marks of student 2 in Urdu {marks[i]}")
#         print(f"marks of student 3 in Math {marks[i]}")
#         i+=1

# f=open("myfile.txt","r")
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"Marks of student{i} in English: {m1}")
#     print(f"Marks of student{i} in Urdu: {m2}")
#     print(f"Marks of student{i} in Maths: {m3}")
#     print(line)
# f=open("myfile3.txt","w")
# lines=["we printed line 1\n","we printed line 2\n","we printed line 3\n"]
# f.writelines(lines)
# print(lines)

f=open("myfile3.txt","r")
print(type(f))
f.seek(5)
print(f.tell())
data=f.read(2)
print(data)
