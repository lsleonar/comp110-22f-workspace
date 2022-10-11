# Example of tuple no aliasing
goat: tuple [str, int] = ("MJ" , 23)

# Tuples are sequences, so theyre 0-indexed
print(goat[0])
print(goat[1])

# Sequences have lengths
print(len(goat))

# Sequences are iterable with for in loops
# MEaning you can loop over them with for in
for item in goat:
    print(item)

# Tuples unlike lists are immutable
# cannot reassign items no append no pop etc
# goat[0] = "LBJ"

# We can invent our own type with a type allias
Player = tuple[str, int]

# Once weve aliased a type we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# In a strange world where jersey number changes
unc_poy = (unc_poy[0], unc_poy[1] + 1)



# A range is another common sequence type
zero_to_nine: range = range(0, 10, 1)

print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

# We can have different steps for more control 
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)

names: list[str] = ["kris", "alyssa", "Michael", "lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")
