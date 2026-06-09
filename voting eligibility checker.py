age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")

if age >= 18 and citizen == "yes":
    print("You can vote!")
else:
    print("You cannot vote.")