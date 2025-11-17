def generate_profile(age):
    if age > 19:
        return "Adult"
    elif age >12:
        return "Teenager"
    else:
        return "Child"

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")

birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []

life_stage = generate_profile(current_age)

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    else:
        hobbies.append(hobby)

user_profile = {'name': user_name, 'age': current_age, 'stage': life_stage, 'hobbies': hobbies}

print(f"\n---\nProfile Summary:\nName: {user_profile['name']}\nAge: {user_profile['age']}\nLife Stage: {user_profile['stage']}")
if len(hobbies) == 0:
    print("You didn't mention any hobbies.\n---")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for i in hobbies:
        print(f"- {i}")
    print("---")