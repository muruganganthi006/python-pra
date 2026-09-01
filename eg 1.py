age = int(input("Enter your age: "))
citizen = input("Are you a citizen of India? (yes/no): ")

if age >= 18 and citizen == "yes":
    print("you are eligible to vote.")
else:
    print("you are not eligible to vote.")
    