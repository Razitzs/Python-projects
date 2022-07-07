# with open("dia24/Files/file.txt") as file:
#     contents=file.read()
#     print (contents)


with open("dia24/Files/file.txt",mode="r") as file:
    for a in file.readlines():
        print(a)