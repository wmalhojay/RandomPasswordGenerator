import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

randPass = "";
def randGenerator(a, b):
    global randPass
    for i in range(1, a+1):
        randPass = randPass + str(b[random.randint(0, len(b)-1)])
    return

def shuffle(randPass):
    randPass = list(randPass)
    for index in range(len(randPass)):
        i = random.randint(0, len(randPass)-1)
        randPass[i], randPass[index] = randPass[index], randPass[i]
    return ''.join(randPass)

randGenerator(nr_letters, letters)
randGenerator(nr_symbols, symbols)
randGenerator(nr_numbers, numbers)

print("Generated password is : "+ shuffle(randPass))
