from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import Caesar
from cipher.vigenere.vigenere_cipher import Vigenere
from cipher.railfence.railfence_cipher import RailFence
from cipher.playfair.playfair_cipher import Playfair
from cipher.transposition.transposition_cipher import TranspositionCipher


app = Flask(__name__)

caesar_cipher = Caesar()
vigenere_cipher = Vigenere()
railfence_cipher = RailFence()
playfair_cipher = Playfair()
transposition_cipher = TranspositionCipher()


#caesar cipher
@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key =int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
    
#vigenere cipher
@app.route("/api/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#railfence cipher
@app.route("/api/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.railfence_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.railfence_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#playfair cipher
@app.route("/api/playfair/create_matrix", methods=['POST'])
def create_matrix():
    data = request.get_json()
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'matrix': matrix})

@app.route("/api/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return jsonify({'decrypted_message': decrypted_text})

#transposition
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = transposition_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = transposition_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})










    #main function
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)