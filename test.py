# habit tracker
from datetime import date

# user come in
print("Hi,Welcome Back! Would you like to track your habits?")
answer_1 = input()
if answer_1 == "yes":
    # habit list
    habits = []

    # date
    today = date.today()
    print(today)

    # ask 3 habit
    for i in range(3):
        habit = input(f"Habit {i+1}:")
        habits.append(habit)
    print(habits)

    # cont list,ask indv (if yes print ok,anything else print no)
    for habit in habits:
        answer_2 = input(f"Have you {habit} on {today}?:\n")
        if answer_2 == "yes":
            print("done")
        else:
            print("not done")

    # motivation popup streak?


# anything else then bye
else:
    print("Goodbye!")
