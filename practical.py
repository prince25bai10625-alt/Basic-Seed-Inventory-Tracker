
import os

FILENAME = "users_data.txt"

# Initial users (will be added if file doesn't exist)
default_users = {
    "dhananjay": "1234",
    "rahul": "2222",
    "ajay": "3333",
    "rakesh": "4444",
    "suresh": "5555",
    "mahesh": "6666",
    "amit": "7777",
    "rohit": "8888",
    "vijay": "9999",
    "arjun": "0000",
    "virat": "1010"
}

# Create file if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as file:
        for user, pwd in default_users.items():
            file.write(f"{user},{pwd}\n")

# Load users from file
def load_users():
    users = {}
    with open(FILENAME, "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password
    return users

# Save new user to file
def save_user(username, password):
    with open(FILENAME, "a") as file:
        file.write(f"{username},{password}\n")

while True:
    users = load_users()

    username = input("\nEnter username: ").lower()
    password = input("Enter password: ").lower()

    if username in users:

        if password == users[username]:
            print(f"\n✅ Welcome sir {username}")

        else:
            attempts = 2
            while attempts > 0:
                print(f"❌ Wrong password. Attempts left: {attempts}")
                password = input("Re-enter password: ").lower()
                if password == users[username]:
                    print(f"\n✅ Welcome sir {username}")
                    break
                attempts -= 1
            else:
                print("⏳ Try again after some time.")
                break
    else:
        print("User not found.")
        choice = input("Do you want to create account? (1 = Yes, 0 = No): ")

        if choice == "1":
            new_user = input("Create username: ").lower()
            new_pass = input("Create password: ").lower()
            save_user(new_user, new_pass)
            print("\n✅ Account created successfully!")

            # Check login immediately
            users = load_users()
            if new_user in users and users[new_user] == new_pass:
                print(f"\n✅ Welcome sir {new_user}")

        else:
            print("🙏 Thank you.")
            break

    # Repeat section
    while True:
        repeat = input("\nEnter 1 to continue or 0 to exit: ")
        if repeat == "1":
            break
        elif repeat == "0":
            print("🙏 Program terminated.")
            exit()
        else:
            print("⚠ Please enter only 1 or 0.")