#2-3
person_name = "Eric Forman"
print(f"Hello {person_name}, would you like to learn some Python today?")

#2-4
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

#2-5/2-6
famous_person = "Thomas Cornu"
famous_quote = "Kess'ça peut t'foutre?"
print(f"{famous_person} once said: ''{famous_quote}''")

#Oui bon a déjà testé tout ça dans le pense-bête

#4-4
numbers = list(range(1, 1_000_001))
#for number in numbers:
#    print(number)

#4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))