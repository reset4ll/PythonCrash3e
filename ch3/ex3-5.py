"""ex3-5.py."""

"""ex3-4.py."""

person = ['socrates', 'platon', 'aristoteles']

print(f"\nHello {person[0].title()}, would you like come to dinner tonight?.")
print(f"Hello {person[1].title()}, would you like come to dinner tonight?.")
print(f"Hello {person[2].title()}, would you like come to dinner tonight?.")

print(f"\nSorry, {person[1].title()} cannot to come!.")   # (a)

person.remove('platon')   # (b)
print(person)
person.append('seneca')   # (b)
print(person)   # (b)

print(f"\nHello {person[0].title()}, would you like come to dinner tonight?.") # (c)
print(f"Hello {person[1].title()}, would you like come to dinner tonight?.") #(c)
print(f"Hello {person[2].title()}, would you like come to dinner tonight?.") # (c)
