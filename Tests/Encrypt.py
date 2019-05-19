from cryptography.fernet import Fernet
 
#cipher_key = Fernet.generate_key()
#print(cipher_key) # 

cipher = Fernet("APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o=")


# ----------> Encryption <-------------
text = 'My super secret message'.encode('utf-8')
encrypted_text = cipher.encrypt(text)
print(encrypted_text.decode("utf-8"))

#encrypted_text = cipher.encrypt('123456'.encode('utf-8'))
#print(encrypted_text)


# ----------> Decryption (not work) <-------------
key = "gAAAAABc1Iz2lf4vN-qQKESZW9q72QEgZeFRq5_bvltHThHTAKPd7LAGKF87zvrgSejvcmAogQ2hXw2kjxRfCu9R01OsTWIIUQ=="
decrypted_text = cipher.decrypt(bytes(key).decode('utf-8'))
print(decrypted_text)




