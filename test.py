# habit tracker

# habit list
habits = []

# indv habit ask 3 time,cont add to list
for i in range(3):
    habit = input(f"Add habit {i+1}:")
    habits.append(habit)

print(habits)

# cont list,ask indv (if y print ok,anything else print no)
for habit in habits:
    question = input(f"Have you {habit} today?")
    if question == "yes":
        print("done")
    else:
        print("not done")
