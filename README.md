# Coded-Correspondence


## Project Overview

Welcome to "Coded Correspondence," a project designed to test and improve your cryptography skills. This project is an excellent foray into the world of secret messages and historical ciphers. You will find Python implementations for the famous Caesar and Vigenère ciphers, which you can use to encode and decode messages.

## Project Goals

As a passionate educator and cryptography enthusiast, this project's goal is to provide you with tools that can help decipher coded messages and also to craft your own. The project allows you to put your Python skills to the test with exciting and engaging puzzles.

## How to Use

1. The `caesar_decode` function allows you to decode messages that were encoded using the Caesar Cipher, given the original offset.
2. The `caesar_encode` function lets you encode your own messages using the Caesar Cipher with any offset you choose.
3. The `vigenere_decode` function decodes messages that were encoded with the Vigenère Cipher using a specific keyword.

To run the provided functions, simply call them with the required parameters.

Example:

```python
decoded_message = caesar_decode(encoded_message, offset)
print(decoded_message)

encoded_message = caesar_encode(your_message, offset)
print(encoded_message)

print(vigenere_decode(vishal_message, keyword))
