# Caesar Cipher
A simple command-line implementation of the Caesar cipher encryption technique in Python.

## Description
This program implements the classic Caesar cipher, one of the earliest and simplest encryption techniques. The cipher works by shifting each letter in a message by a fixed number of positions down or up the alphabet.

For example, with a shift of 3:
```
'a' becomes 'd'
'b' becomes 'e'
'z' becomes 'c' (wrapping around to the beginning)
The program allows for both encryption ("encode") and decryption ("decode") operations.
```

## Features
- Encrypt messages using the Caesar cipher technique
- Decrypt messages encrypted with Caesar cipher
- Handles wraparound from 'z' to 'a' automatically
- Simple command-line interface

## How to Use
- Run the script: caesar_cipher.py
- Follow the prompts:
- Type 'encode' to encrypt a message or 'decode' to decrypt
- Enter the message you want to process
- Enter the shift number (how many positions to shift the alphabet)
- The program will output your encrypted or decrypted message

## Example
```Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
Here is the encoded result: mjqqt

To decrypt:

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt
Type the shift number:
5
Here is the decoded message: hello
```
## Technical Details
The program uses:

- A list to represent the alphabet
- Modulo arithmetic to handle wrapping around the alphabet
- Separate functions for encryption and decryption
- A combined function that calls the appropriate operation based on user input

## Limitations
- Currently only works with lowercase letters
- Does not preserve spaces or special characters
- Limited to the 26 English alphabet letters

## Future Improvements
- Add support for uppercase letters
- Preserve spaces and special characters
- Implement brute force decryption for unknown shift values
- Add a graphical user interface



