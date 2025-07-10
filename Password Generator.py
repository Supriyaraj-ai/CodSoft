import random
import string

def create_random_password(size):
    if size < 4:
        return "The password length must be at least 4 characters!"

    # Define character sets
    alpha_chars = string.ascii_letters
    digit_chars = string.digits
    special_chars = string.punctuation
    
    # Ensure the password contains at least one character from each category
    password = [
        random.choice(alpha_chars),
        random.choice(digit_chars),
        random.choice(special_chars)
    ]

    # Fill the remaining length with random choices from all character sets
    all_chars = alpha_chars + digit_chars + special_chars
    password += random.choices(all_chars, k=size - 3)

    # Shuffle the created password to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def run_password_generator():
    print("🔒 Secure Password Generator")
    try:
        desired_length = int(input("Specify the length of the password: "))
        generated_password = create_random_password(desired_length)
        print("Your Generated Password:", generated_password)
    except ValueError:
        print("Invalid input! Please enter a numerical value.")

if __name__ == "__main__":
    run_password_generator()