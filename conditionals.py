# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are of age")
# else:
#     print("You are a minor")

# password = "456m789D123".lower()
# ask_password = str(input("Enter your password: ")).lower()
# if password == password1:
#     print("Valid password")
# else:
#     print("Invalid password")

# number_1 = float(input("Write a number: "))
# number_2 = float(input("Write another number: "))
# if number_2 == 0:
#     print("Error")
# else:
#     print("The result of the division is", number_1 / number_2)

# whole_number = int(input("Enter a whole number: ")) # whole: entero -> numero entero 
# if whole_number % 2 == 0:
#     print("The number " + str(whole_number) + " is even") # El numero es par
# else:
#     print("The number " + str(whole_number) + " is odd") # El numero es impar

# age = int(input("What is your age?: "))
# income = int(input("What is your income?: "))
# if age >= 16 and income >= 1000: # junto dos condiciones con and
#     print("You can to acces, welcome!")
# else:
#     print("You can't to access")

 
# name = input("What's your name? ").lower()
# gender = input("What's your gender? F or M: ").lower() # gender: female(f) or male(m)
# if name < "m" and gender == "f":
#     print("Group: A")
# elif name > "n" and gender == "m":
#     print("Group: A")
# else:
#     print("Group: B")


# annual_rent = float(input("¿What's your annual rent?: "))
# if annual_rent < 10000:
#     print("Tax rate: 5%")
# elif annual_rent >= 10000 and annual_rent < 20000:
#     print("Tax rate: 15%")
# elif annual_rent >= 20000 and annual_rent < 35000:
#     print("Tax rate: 20%") 
# elif annual_rent >= 35000 and annual_rent < 60000:
#     print("Tax rate: 30%")
# elif annual_rent >= 60000:
#     print("Tax rate: 45%")
# else:
#     print("Error")


# user_score = float(input("What's your score?: ")) # score: puntuacion

# unacceptable = 0.0 # variables que guardan un valor
# acceptable = 0.4
# meritorious = 0.6
# money = 2400

# if user_score >= unacceptable and user_score < acceptable:
#     print(f'The score is unacceptable and you salary is {money}')
# elif user_score >= acceptable and user_score < meritorious: 
#     print(f'The score is acceptable and you salary is {(money * acceptable) + money}')   
# elif user_score >= meritorious:
#     print(f'The score is meritorious and you salary is {(money * meritorious) + money}')
# else:
#     print("Error")


# age_user = int(input("What's your age?: "))

# if age_user < 4:
#     print("You can to entrance free") # Puedes entrar gratis
# elif age_user >= 4 and age_user < 18:
#     print("You must to pay 5€") # Debes pagar 5€
# else:
#     print("You must to pay 10€") # Debes pagar 10€


"""
Welcome to the pizza shop Bella Napoli!

We have two types of pizzas:
1-Vegetarian pizza
2-Non-vegetarian pizza

"""
pizza = int(input("Enter an option: ") 

if pizza == 1:
    print("You chose a vegetarian pizza")
    ingredient = input("Enter the ingredient you want")
    print("")