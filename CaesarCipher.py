def caesar_cipher(text, shift, encrypt=True):
    result = ""
    
    # Adjust shift for decryption
    if not encrypt:
        shift = -shift
    
    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are not changed
            
    return result

def main():
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? (or 'q' to quit): ").lower()
        if choice == 'q':
            break
        
        if choice not in ('e', 'd'):
            print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter shift value (0-25): "))
        
        if choice == 'e':
            encrypted_message = caesar_cipher(message, shift, encrypt=True)
            print(f"Encrypted Message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher(message, shift, encrypt=False)
            print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
