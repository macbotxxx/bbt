# Windows: C:/Users/<PC Name>/AppData/Roaming/Mozilla/Firefox/Profiles
# Mac: ~/Library/Application Support/Firefox/Profiles
# Linux: ~/.mozilla/firefox/Profiles

#step 1: convert data (i.e. usernames/password)from base64 to string 
data = b64decode(data64)
#step 2: pass the string data into the SECItem object as input data
input = SECItem(0, data, len(data))
#step 3: create a SECItem object to store the decrypted output data
create a output = SECItem(0, None, 0)
#step 4: perform PK11 decryption
PK11SDR_Decrypt(inp, out, None)