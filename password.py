from cryptography.fernet import Fernet
import os

# Function to create and save a new key in "key.key" file
def write_key():
    key = Fernet.generate_key()       # Generate encryption key
    with open("key.key", "wb") as key_file:
        key_file.write(key)           # Store the key in a file

# Function to load the key
def load_key():
    # If key file does not exist, create it
    if not os.path.exists("key.key"):
        write_key()
    # Read and return the key
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Load (or create) the key
key = load_key()
# Create a Fernet object with this key to encrypt/decrypt passwords
fer = Fernet(key)

def view():
    # If no passwords file exists yet
    if not os.path.exists('passwords.txt'):
        print("No passwords stored yet.")
        return
    
    # Open and read all stored passwords
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()   # Remove newline characters
            
            if "|" not in data:    # Skip any invalid lines
                continue

            # Each line is saved as "Account | EncryptedPassword"
            user, passw = data.split("|", 1)
            try:
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
            except Exception as e:
                # In case the password cannot be decrypted (corrupt/mismatched key)
                print(f"Could not decrypt password for {user}: {e}")



def add():
    name = input('Account Name: ')    
    pwd = input("Password: ")        

    # Encrypt and save the password
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    
    if mode == "q":
        break       # Exit program

    if mode == "view":
        view()      # Call view function
    elif mode == "add":
        add()       # Call add function
    else:
        print("Invalid mode.")
        continue

