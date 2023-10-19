"""ex3-6.py."""

person = ['socrates', 'platon', 'aristoteles']

print(f"\nHello {person[0].title()}, would you like to dinner tonight?.")
print(f"Hello {person[1].title()}, would you like to dinner tonight?.")
print(f"Hello {person[2].title()}, would you like to dinner tonight?.")

print('Hey boys, I found a bigger dinner table!')

person.insert(0,'Hegel')
person.insert(3,'Schopenhauer')
person.insert(5,'Nietzsche')

print(f"\nHello {person[0].title()}, would you like to dinner tonight?.")
print(f"Hello {person[1].title()}, would you like to dinner tonight?.")
print(f"Hello {person[2].title()}, would you like to dinner tonight?.")
print(f"Hello {person[3].title()}, would you like to dinner tonight?.")
print(f"Hello {person[4].title()}, would you like to dinner tonight?.")
print(f"Hello {person[5].title()}, would you like to dinner tonight?.")
