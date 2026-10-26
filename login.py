def login():
    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        try:
            with open("login.txt", "r") as f:
                for line in f:
                    fields = [field.strip() for field in line.split(",")]
                    
                    if len(fields) == 2 and fields[0] == username and fields[1] == password:
                        print("Logged in successfully\n")
                        return main()
        except FileNotFoundError:
            print("Error: 'login.txt' file not found.")
            return

        print("Username or password incorrect. Please try again.\n")

def main():
    print("Welcome to our website server.")

if __name__ == "__main__":
    login()
