


def show_homepage():
    print("\n")
    print("      === DonateMe Homepage ===        ")
    print("---------------------------------------")
    print("| 1. Login      | 2. Register         |")
    print("---------------------------------------")
    print("| 3. Donate     | 4. Show Donations   |")
    print("---------------------------------------")
    print("            5.   Exit                  ")
    print("---------------------------------------")
    print("\n")


def donate(username):
    donation_amt = float(input("\nEnter amount to donate: "))
    donation_string =  "{} donated ${}".format(username, donation_amt)
    print("Thank you ", username, "!!")
    return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("\nCurrently, there are NO donations")
    for donation in donations:
        print(donation)




