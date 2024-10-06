from DES import DES

if __name__ == "__main__":
  # Membuat Pilihan apakah ingin melakukan enkripsi atau dekripsi 
    choice = input("Encrypt or Decrypt? (e/d): ")
    des = DES("")
    if choice == 'e':
        plaintext = input("Enter the plaintext: ")
        print("Encrypted text: ", des.encrypt(plaintext))
    elif choice == 'd':
        # get file encrypted.txt
        with open('encrypted.txt', 'r', encoding='utf-8') as f:
            ciphertext = f.read()
        print("Decrypted text: ", des.decrypt(ciphertext))
    else:
        print("Invalid choice")