password_vault = {"kevin" : "peanuts",
                         "amyke" : "camera",
                         "deyna" : "lamp",
                         "dad" : "telefone"
                         }

username = input("What is your username...: ")
password = input("Password...:")

if username in password_vault and password == password_vault.get(username):
    print("Welcome, enjoy your stay!")
else:
    print("Sorry your credentials were not recognised, please try again.")

