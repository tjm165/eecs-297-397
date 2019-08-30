print("{} World".format("Hello"))

print("{} {} {} {} {} {}".format("This", "is", "silly", "but", "will", "work"))


first_name = "matt"
last_name = "sargent"

print("{} {}".format(first_name.capitalize(), last_name.capitalize()))

# f-strings
print(f"{first_name.capitalize()} {last_name.capitalize()}")

full_name = f"{first_name} {last_name}"
print(f"{full_name.title()}")

# Cannot have empty expression in f-string. This will fail.
# print(f"Hello {full_name.title()}! It's {} to meet you!".format("great"))
