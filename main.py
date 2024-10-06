from DES import DES

if __name__ == "__main__":
  # Membuat Pilihan apakah ingin melakukan enkripsi atau dekripsi 
    choice = input("Encrypt or Decrypt? (e/d): ")
    key = input("Enter the key: ")
    des = DES.DES(key)
    if choice == 'e':
        plaintext = input("Enter the plaintext: ")
        print("Encrypted text: ", des.encrypt(plaintext))
    elif choice == 'd':
        ciphertext = input("Enter the ciphertext: ")
        print("Decrypted text: ", des.decrypt(ciphertext))
    else:
        print("Invalid choice")