import base64

def main():
    input_string = input("Nhập thông tin cần mã hoá: ")
    encoded_byte = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_byte.decode("utf-8") 

    with open("data.txt", 'w') as file:
        file.write(encoded_string)

    print("Đã mã hoá và ghi vao file data.txt")

if __name__ == "__main__":
    main()
