from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin":"123"}
donations = []
authorized_user = ""

print(database)

if authorized_user == "":
    print("You must be logged in to donate")
else:
    print("Logged in as:", authorized_user)


while True:
    show_homepage()
    option = int(input("\nChoose an option: "))


    if option == 1:
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        authorized_user = login(database, username, password)
        continue
    elif option == 2:
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
            continue
        continue
    elif option == 3:
        if authorized_user == "":
            print("\nYou are not logged in. Returning to main menu")
            continue
        donation_string = donate(authorized_user)
        donations.append(donation_string)
    elif option == 4:
        show_donations(donations)
        continue
    else:   
        print("Goodbye!")
        break



