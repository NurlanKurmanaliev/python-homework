foods=("Apple", "Banana", "Orange", "Mango", "Strawberry", "Grape", "Mandarin", "Strawberry")
calories=(52, 96, 62, 605, 33, 68, 50, 33)

foods=list(foods)
calories=list(calories)

print(foods, calories)
print(foods[4], calories[4])
print(foods[-2], calories[-2])

unique_foods=list(set(foods))
print(unique_foods)

dict_foods={"Apple" : 52, "Banana" : 96, "Orange" : 62, "Mango" : 605, "Strawberry" : 33, "Grape" : 68, "Mandarin" : 50, "Strawberry" : 33}
print(dict_foods)
print(dict_foods["Mango"])
print(dict_foods["Apple"])
print(dict_foods["Grape"])

