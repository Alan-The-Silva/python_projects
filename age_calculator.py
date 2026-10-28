full_name = input("what's your name: ")
birth_year = input("In which year were your born: ")

current_year = 2026
age = current_year - int(birth_year)

print(f"Hello {full_name}, you are {age} years old in {current_year}.")
