def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
        if choice not in ["encrypt", "decrypt"]:
            print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
            continue
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (a number between 1 and 25): "))
        if not 1 <= shift <= 25:
            print("Shift value must be between 1 and 25.")
            continue

        if choice == "encrypt":
            result = encrypt(message, shift)
            print("Encrypted message:", result)
        else:
            result = decrypt(message, shift)
            print("Decrypted message:", result)

        another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if another != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
