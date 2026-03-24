# habit tracker
from datetime import date
import json
import os
file = "habits.json"

# user come in
print("Hi,Welcome Back! Would you like to track your habits?")
answer_1 = input()
if answer_1 == "yes":

    # check file exist and got save
    if os.path.exists(file) and os.path.getsize(file) > 0:

        # read file as convention,load json string to python list,close
        with open(file, "r") as f:
            habits = json.load(f)

    # no file exists so no save
    else:
        habits = []

        # date
    today = date.today()

    # if nothing in habits list,cont / if got data ,cont to step2
    print("Would you like to restart or continue")
    answer_0 = input()
    if answer_0 == "restart":
        for i in range(3):
            habit = input(f"Habit {i+1}:")
            habits.append(habit)

        # overwrite file as convention,convert python list to json string,close
        with open(file, "w") as f:
            json.dump(habits, f)

        # cont list,ask indv (if yes print ok,anything else print no) step2
    else:
        for habit in habits:
            answer_2 = input(f"Have you {habit} on {today}?:\n")
        if answer_2 == "yes":
            print("done")
        else:
            print("not done")

    # anything else then bye
else:
    print("Goodbye!")

    # motivation popup streak?
