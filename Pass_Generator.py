import random
import string

def generate_password(length):
    """Generates a strong random password of specified length"""
    
    # Define a list of character sets to be used in the password
    charsets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]
    
    # Use at least one character from each character set
    password = [random.choice(charset) for charset in charsets]
    
    # Fill the rest of the password with random characters from all character sets
    password += [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - len(password))]
    
    # Shuffle the password
    random.shuffle(password)
    
    # Join the password and return it as a string
    return ''.join(password)

if __name__ == '__main__':
    length = int(input("Enter the length of the password you wish to generate: "))
    password = generate_password(length)
    print("Your new password is:", password)
