def importPasswords():
    passwords = open('day2Input.txt', 'r')
    return passwords

def main():
    print(importPasswords())

if __name__ == "__main__":
    main()