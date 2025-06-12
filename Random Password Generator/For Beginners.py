import random
import string

def get_user_preferences():
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid length. Please enter a number.")
        return get_user_preferences()

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    return length, include_uppercase, include_lowercase, include_digits, include_symbols

def build_character_set(uppercase, lowercase, digits, symbols):
    character_pool = ""
    if uppercase:
        character_pool += string.ascii_uppercase
    if lowercase:
        character_pool += string.ascii_lowercase
    if digits:
        character_pool += string.digits
    if symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("You must select at least one character type!")

    return character_pool

def generate_password(length, character_pool):
    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    try:
        length, u, l, d, s = get_user_preferences()
        pool = build_character_set(u, l, d, s)
        password = generate_password(length, pool)
        print("Generated password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
