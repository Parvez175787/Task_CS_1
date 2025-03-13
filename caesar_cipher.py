def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            result += char
            
    return result

def decrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            result += char
            
    return result

def main():
    choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'e':
        print("Encrypted message: " + encrypt(message, shift))
    elif choice == 'd':
        print("Decrypted message: " + decrypt(message, shift))
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
