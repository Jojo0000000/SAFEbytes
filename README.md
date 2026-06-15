 # SAFEbytes

SAFEbytes is a web-based application that provides encryption and decryption services using various ciphers, including Caesar, Vigenère, AES, and DES. 
The application is built using Flask for the backend and HTML/CSS for the frontend.

# Features

- **Caesar Cipher**: Simple substitution cipher where each letter is shifted by a fixed number of positions.
- **Vigenère Cipher**: Polyalphabetic substitution cipher using a keyword to shift letters.
- **AES (Advanced Encryption Standard)**: Symmetric encryption algorithm that encrypts data in fixed-size blocks.
- **DES (Data Encryption Standard)**: Symmetric encryption algorithm that encrypts data in 64-bit blocks.
- **User-Friendly Interface**: Interactive web interface to easily input text and select encryption/decryption techniques.

# Requirements

- Python 3.x
- Flask
- PyCryptodome

 # Installations

1. Clone the repository:
    ```bash
    git clone https://github.com/Alisba04/SAFEbytes.git
    cd SAFEbytes
    ```
2. Install the required dependencies:
    ```bash
    pip install Flask pycryptodome
    ```

- Usage

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Access the web application:
    Open your browser and navigate to `http://127.0.0.1:5000/`

3. Interface Overview:
    - **Enter Text**: Input the plain text you want to encrypt or decrypt.
    - **Choose Encryption Technique**: Select one of the available encryption techniques (Caesar, AES, DES, Vigenère).
    - **Enter Key**: Provide the key for the chosen encryption technique.
    - **Encrypt/Decrypt**: Click the "Encrypt" or "Decrypt" button to perform the operation and view the result.

#  API Endpoints

- **Encrypt**: `/encrypt`
    - Method: `POST`
    - Payload:
        ```json
        {
            "text": "Your text here",
            "cipher_type": "caesar/aes/des/vigenere",
            "key": "your-key"
        }
        ```
    - Response:
        ```json
        {
            "encrypted_text": "encrypted text"
        }
        ```

- **Decrypt**: `/decrypt`
    - Method: `POST`
    - Payload:
        ```json
        {
            "ciphertext": "Your encrypted text here",
            "cipher_type": "caesar/aes/des/vigenere",
            "key": "your-key"
        }
        ```
    - Response:
        ```json
        {
            "decrypted_text": "decrypted text"
        }
        ```

# Example

Here is an example of how to use the API with the `curl` command.

- Encrypting text:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"text": "hello world", "cipher_type": "caesar", "key": "3"}' http://127.0.0.1:5000/encrypt
    ```

- Decrypting text:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"ciphertext": "khoor zruog", "cipher_type": "caesar", "key": "3"}' http://127.0.0.1:5000/decrypt
    ```

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

# Contributing

Feel free to submit issues, fork the repository, and send pull requests!

---

Feel free to customize it further to better suit your project's needs! 
