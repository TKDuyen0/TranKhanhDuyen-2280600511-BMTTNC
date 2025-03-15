from flask import Flask, render_template, request, json
from cipher.caesar.caesar_cipher import Caesar

app = Flask(__name__)

caesar_cipher = Caesar()

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/caesar")
def caesar():
    return render_template('caesar.html')


@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    encrypted_text = caesar_cipher.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"


@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    decrypted_text = caesar_cipher.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
