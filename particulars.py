name = input("What is your name? ")
age = int(input("How old are you? "))
birth_year = 2015 - age
state = True
while state:
    if age<0:
        age = int(input('''Sorry, please enter a number more than 0.\nHow old are you? '''))
        birth_year = 2015 - age
    else:
        print("Hello " + str(name) + ". You were born in " + str(birth_year) + ".")
        state = False
        if age<18:
            print("You are a student!")


