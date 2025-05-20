# Define the alphabet list that will be used for encryption/decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user input for operation type, message, and shift value
direction = input("Please type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()  # Convert to lowercase for case-insensitive comparison
text = input("Type your message:\n").lower()  # Convert message to lowercase
shift = int(input("Type the shift number:\n"))  # Convert shift to integer


# Function to encrypt a message using the Caesar cipher
def encrypt(original_text, shift_amount):
    cipher_text = ""  # Initialize empty string to store the encrypted message
    for letter in original_text:  # Loop through each letter in the original text
        shifted_position = alphabet.index(letter) + shift_amount  # Find the new position by adding the shift
        shifted_position %= len(alphabet)  # Use modulo to handle wrap-around (e.g., 'z' + 1 = 'a')
        cipher_text += alphabet[shifted_position]  # Add the shifted letter to the cipher text
    print(f"Here is the encoded result: {cipher_text}")  # Display the encrypted message



# Function to decrypt a message using the Caesar cipher
def decrypt(original_text, shift_amount):
    decoded_message = ""  # Initialize empty string to store the decrypted message
    for letter in original_text.lower():  # Loop through each letter, ensuring lowercase
        shifted_position = alphabet.index(letter) - shift_amount  # Find the original position by subtracting the shift
        shifted_position %= len(alphabet)  # Use modulo to handle wrap-around (e.g., 'a' - 1 = 'z')
        decoded_message += alphabet[shifted_position]  # Add the unshifted letter to the decoded message

    print(f"Here is the decoded message: {decoded_message}")  # Display the decrypted message



# Combined function that handles both encryption and decryption
def caesar(original_text, shift_amount):
    if direction.lower() == "encode":  # If user wants to encrypt
        encrypt(original_text, shift_amount)  # Call the encrypt function
    elif direction.lower() == "decode":  # If user wants to decrypt
        decrypt(original_text, shift_amount)  # Call the decrypt function
    else:
        print("You chose wrong action")  # Error message for invalid input

# Call the main caesar function with user inputs
caesar(text, shift)
