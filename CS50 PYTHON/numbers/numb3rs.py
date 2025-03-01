import re


def main():
    ip_address = input("What is the IP address: ")
    print(validate(ip_address))


def validate(ip_address):
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if re.match(pattern, ip_address):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
