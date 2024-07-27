import requests, os, time, keyboard, json, shutil, tkinter
from tkinter import filedialog

watermark = """
░██████╗██╗███╗░░░███╗██████╗░██╗░░░░░███████╗
██╔════╝██║████╗░████║██╔══██╗██║░░░░░██╔════╝
╚█████╗░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░
░╚═══██╗██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░
██████╔╝██║██║░╚═╝░██║██║░░░░░███████╗███████╗
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝
"""

# A little watermark ;)
print(watermark)

def save_data_to_file():
    # Get username
    username = input("Enter a Roblox username: ")

    # Endpoint
    url = "https://users.roblox.com/v1/usernames/users"
    payload = {
        "usernames": [username],
        "excludeBannedUsers": True
    }
    response = requests.post(url, json=payload)

    # Status
    if response.status_code == 200:
        data = response.json()

        # Extract data
        name = data.get('data')[0].get('name')
        displayName = data.get('data')[0].get('displayName')
        hasVerifiedBadge = data.get('data')[0].get('hasVerifiedBadge')
        id = data.get('data')[0].get('id')
        isBanned = data.get('data')[0].get('isBanned')
        description = data.get('data')[0].get('description')
        

        # Print data
        os.system("cls")
        print(watermark)
        print("================== User Information ==================\n")
        print(f"Name: {name}\n")
        print(f"Display Name: {displayName}\n")
        print(f"Description: {description}\n")
        print(f"Has Verified Badge: {hasVerifiedBadge}\n")
        print(f"Is Banned: {isBanned}\n")
        print(f"ID: {id}\n")

        # Ask user if they want to save data to a .txt file
        save_data = input("Do you want to save this data to a .txt file? (y/n): ")

        if save_data.lower() == "y":
            # Create a .txt file with the user data
            file_path = filedialog.asksaveasfilename(initialfile=f"{username}.txt", defaultextension=".txt")
            if file_path:
                with open(file_path, "w") as file:
                    file.write("================== User Information ==================\n")
                    file.write(f"Name: {name}\n")
                    file.write(f"Display Name: {displayName}\n")
                    file.write(f"Description: {description}\n")
                    file.write(f"Is Banned: {isBanned}\n")
                    file.write(f"Has Verified Badge: {hasVerifiedBadge}\n")
                    file.write(f"ID: {id}\n")

                print("\nData saved successfully to " + file_path + ".")
            else:
                print("\nData will not be saved to a .txt file.")
        else:
            print("\nData will not be saved to a .txt file.")
    else:
        print("\nFailed to retrieve user data.")

def main():
    root = tkinter.Tk()
    root.withdraw()
    save_data_to_file()

if __name__ == "__main__":
    main()
    time.sleep(2)