import time
print("1: If by Rudyard Kipling")
choice = int(input("2: Ma'am by J.P. McEvoy"))

if choice == 1:
    with open("rudyard.txt", "r") as whole_file:
        for line in whole_file:
            time.sleep(3)
            print(line, end="")
elif choice == 2:
    with open("Ma'am", "r") as whole_file:
        for line in whole_file:
            time.sleep(3)
            print(line, end="")
