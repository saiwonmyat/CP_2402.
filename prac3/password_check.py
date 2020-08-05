def password_check(password):
    necessaryword = ['#', '%' , '$', '@']
    value = True

    if len(password) <8 or len(password) >20:
        print('length should be at least 8 and between 20')
        value = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        value = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        value = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        value = False

    if not any(char in necessaryword for char in password):
        print('Password should have at least one of the symbols %$@#')
        val = False
    if value:
        return value


def main():
    password =input("Enter the password: ")

    if (password_check(password)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
main()