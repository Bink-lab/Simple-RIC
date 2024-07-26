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
    # Get ID
    userID = input("Enter your Roblox user ID: ")

    # Enpoint
    url = f"https://users.roblox.com/v1/users/{userID}"
    response = requests.get(url)

    # Status
    if response.status_code == 200:
        data = response.json()

        # Extract data
        name = data.get('name')
        displayName = data.get('username')
        description = data.get('description')
        isBannned = data.get('isBanned')
        hasVerifiedBadge = data.get('hasVerifiedBadge')
        created = data.get('created')
        id = data.get('id')

        # Print data
        os.system("cls")
        print(watermark)
        print("================== User Information ==================\n")
        print(f"Name: {name}\n")
        print(f"Display Name: {displayName}\n")
        print(f"Description: {description}\n")
        print(f"Is Banned: {isBannned}\n")
        print(f"Has Verified Badge: {hasVerifiedBadge}\n")
        print(f"Created: {created}\n")
        print(f"ID: {id}\n")

        # Ask user if they want to save data to a .txt file
        save_data = input("Do you want to save this data to a .txt file? (y/n): ")

        if save_data.lower() == "y":
            # Create a .txt file with the user data
            file_path = filedialog.asksaveasfilename(initialfile=f"{userID}.txt",
                                                  defaultextension=".txt")
            if file_path:
                with open(file_path, "w") as file:
                    file.write("================== User Information ==================\n")
                    file.write(f"Name: {name}\n")
                    file.write(f"Display Name: {displayName}\n")
                    file.write(f"Description: {description}\n")
                    file.write(f"Is Banned: {isBannned}\n")
                    file.write(f"Has Verified Badge: {hasVerifiedBadge}\n")
                    file.write(f"Created: {created}\n")
                    file.write(f"ID: {id}")

                print("\nData saved successfully to " + file_path + ".")
            else:
                print("\nData will not be saved to a .txt file.")
        else:
            print("\nData will not be saved to a .txt file.")

# Main function
def main():
    root = tkinter.Tk()
    root.withdraw()
    save_data_to_file()

if __name__ == "__main__":
    main()
    time.sleep(2)