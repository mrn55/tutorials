def largest_sallary(salaries):
    return max(salaries)

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
else:
    print('He is not a male')

salaries = []
salaries.append(int(input("Enter sallary for 1: ")))
salaries.append(int(input("Enter sallary for 2: ")))

print(salaries)

print(f"The largest sallary is {largest_sallary(salaries)}")

if largest_sallary(salaries) > 1000000:
    print("You are rich")
elif largest_sallary(salaries) > 500000 and largest_sallary(salaries) < 1000000:
    print('You are middle class')
elif largest_sallary(salaries) < 500000:
    print("You are poor")
else:
    print("Invalid sallary")
