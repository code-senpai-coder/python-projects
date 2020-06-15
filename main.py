import shlex

def register(name, password):
    file = open(f"userdata{name}.txt", "w")
    file.write(name + " ")
    file.write(password)
    print("Account has been sucesfully created")

def login(name, password):
     try:
        file = open(f"userdata{name}.txt", "r")
        #print(file.readline())
        data = file.readline()
        data_arr = shlex.split(data)
        if name != data_arr[0] or password != data_arr[1]:
            print("Invalid password")
        else:
            print("Succesfull")

     except FileNotFoundError:
        print("Not an account with such a name.")


while True:
    operation = input("What do you want to do: ")
    if operation == "register":
        name = input("Enter name: ")
        password = input("Enter password: ")
        register(name, password)
    elif operation == "login":
        name = input("Enter name: ")
        password = input("Enter password: ")
        login(name, password)
    else:
        print("Invalid answer")


