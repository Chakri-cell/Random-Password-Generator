import random
import string
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Combine the character sets based on user preferences
    characters = []
    if use_uppercase:
        characters.append(uppercase)
    if use_numbers:
        characters.append(numbers)
    if use_symbols:
        characters.append(symbols)

    # Ensure at least one character from each set is included
    password = [random.choice(lowercase)]
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password with random characters
    for _ in range(length - 3):
        password.append(random.choice(''.join(characters)))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the password list to a string
    password = ''.join(password)

    return password

def main():
    # Get user input for password length and character types
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    # Validate user input
    if length < 1:
        print("Password length must be at least 1 character.")
        return

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)

    # Print the generated password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()