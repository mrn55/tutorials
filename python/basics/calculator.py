import functools

print("What kind of operation do you want to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
operator = int(input())

if operator == 5:
    print("Goodbye!")
elif operator != 4:
    number_of_numbers_to_operate_on = int(input("How many numbers do you want to operate on?"))
    numbers = []
    for i in range (number_of_numbers_to_operate_on):
        numbers.append(int(input()))
    set_of_numbers = set(numbers)
    if operator == 1:
        print("The sum of the numbers is", sum(set_of_numbers))
    elif operator == 2:
        print("The difference between the numbers is", max(set_of_numbers)-min(set_of_numbers))
    elif operator == 3:
        print("The product of the numbers is", functools.reduce(lambda x,y:x*y, set_of_numbers))
elif operator == 4:
    numerator = float(input("Numerator: "))
    denominator = float(input("Denominator: "))
    print(numerator / denominator)

