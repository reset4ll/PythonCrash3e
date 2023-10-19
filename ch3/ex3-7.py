"""ex3-7.py."""

person = ['socrates', 'platon', 'aristoteles']

print(f"\nHello {person[0].title()}, would you like to dinner tonight?.")
print(f"Hello {person[1].title()}, would you like to dinner tonight?.")
print(f"Hello {person[2].title()}, would you like to dinner tonight?.")

print('Hey boys, I found a bigger dinner table!')

# Inserting guests...
person.insert(0,'hegel')
person.insert(3,'schopenhauer')
person.insert(5,'nietzsche')

print(f"\nHello {person[0].title()}, would you like to dinner tonight?.")
print(f"Hello {person[1].title()}, would you like to dinner tonight?.")
print(f"Hello {person[2].title()}, would you like to dinner tonight?.")
print(f"Hello {person[3].title()}, would you like to dinner tonight?.")
print(f"Hello {person[4].title()}, would you like to dinner tonight?.")
print(f"Hello {person[5].title()}, would you like to dinner tonight?.\n")

print(person)

# Leaving guests...
print("\nSorry socrates, you're still invited!")
person.pop(1)   # socrates
print(person)   # group
print("Sorry platon, you're still invited!")
person.pop(1)   # platon
print(person)   # group
print("Sorry aristoteles, you're still invited!")
person.pop(2)   # aristoteles
print(person)   # group
print("Sorry nietzsche, you're still invited!\n")
person.pop(2)   # nietzsche
print(person)   # group: hegel & schopenhauer

del person[0]   # hegel
del person[0]   # schopenhauer
print(person)   # empty list



