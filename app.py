from flask import Flask, request, jsonify,send_from_directory
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

app = Flask(__name__)

# Padding and unpadding functions for AES and DES
def pad(data, block_size):
    length = block_size - (len(data) % block_size)
    return data + bytes([length]) * length

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Caesar Cipher
def caesar_cipher(text, key, encrypt=True):
    shift = int(key) if encrypt else -int(key)
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Vigenere Cipher
def vigenere_cipher(text, key, encrypt=True):
    key = key.lower()
    result = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if not encrypt:
                shift = -shift
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

# AES Encryption and Decryption
def AES_encrypt(data, key):
    key = key.ljust(16, '\0')[:16]  # Ensure key is 16 bytes
    iv = get_random_bytes(16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    padded_data = pad(data.encode('utf-8'), 16)
    encrypted_data = cipher.encrypt(padded_data)
    ciphertext = iv + encrypted_data
    return b64encode(ciphertext).decode('utf-8')

def AES_decrypt(ciphertext, key):
    key = key.ljust(16, '\0')[:16]
    decoded_ciphertext = b64decode(ciphertext)
    iv = decoded_ciphertext[:16]
    encrypted_data = decoded_ciphertext[16:]
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    return unpad(decrypted_data).decode('utf-8')

# DES Encryption and Decryption
def DES_encrypt(data, key):
    key = key.ljust(8, '\0')[:8]  # Ensure key is 8 bytes
    iv = get_random_bytes(8)
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)
    padded_data = pad(data.encode('utf-8'), 8)
    encrypted_data = cipher.encrypt(padded_data)
    ciphertext = iv + encrypted_data
    return b64encode(ciphertext).decode('utf-8')

def DES_decrypt(ciphertext, key):
    key = key.ljust(8, '\0')[:8]
    decoded_ciphertext = b64decode(ciphertext)
    iv = decoded_ciphertext[:8]
    encrypted_data = decoded_ciphertext[8:]
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    return unpad(decrypted_data).decode('utf-8')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data['text']
    cipher_type = data['cipher_type']
    key = data['key']

    if cipher_type == 'caesar':
        encrypted_text = caesar_cipher(text, key, encrypt=True)
    elif cipher_type == 'AES':
        encrypted_text = AES_encrypt(text, key)
    elif cipher_type == 'DES':
        encrypted_text = DES_encrypt(text, key)
    elif cipher_type == 'vigenere':
        encrypted_text = vigenere_cipher(text, key, encrypt=True)
    else:
        return jsonify({'error': 'Unsupported cipher type'}), 400

    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    ciphertext = data['ciphertext']
    cipher_type = data['cipher_type']
    key = data['key']

    if cipher_type == 'caesar':
        decrypted_text = caesar_cipher(ciphertext, key, encrypt=False)
    elif cipher_type == 'AES':
         decrypted_text = AES_decrypt(ciphertext, key)
    elif cipher_type == 'DES':
        decrypted_text = DES_decrypt(ciphertext, key)
    elif cipher_type == 'vigenere':
        decrypted_text = vigenere_cipher(ciphertext, key, encrypt=False)
    else:
        return jsonify({'error': 'Unsupported cipher type'}), 400

    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)