import socket

def check_domain(domain):
    try:
        # Try to resolve the domain using DNS
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False

def main():
    file_path = input("Enter the path to the file containing base domain names: ")

    try:
        with open(file_path, "r") as file:
            base_domains = [line.strip() for line in file.readlines()]

        # List of common domain extensions
        extensions = [".com", ".net", ".org", ".edu", ".gov", ".co", ".io", ".in"]

        exists_domains = []

        print("Checking domain availability:")
        for base_domain in base_domains:
            for extension in extensions:
                full_domain = base_domain + extension
                if check_domain(full_domain):
                    exists_domains.append(full_domain)
                    print(f"{full_domain} exists.")
                else:
                    print(f"{full_domain} does not exist.")

        # Save existing domains to a file
        with open("Exists.txt", "w") as exists_file:
            for domain in exists_domains:
                exists_file.write(domain + "\n")

        print("Existing domains saved to 'Exists.txt'.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    main()
                          
