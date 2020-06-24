

#encryption
from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)
ciphertext

#decryption
bj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
obj2.decrypt(ciphertext)
'The answer is no'

import datetime
from Crypto.Cipher import AES
# Crypto.Cipher.AES.new(key, mode, *args, **kwargs)
try:
    dosya = open("Log.txt","w")
    dosya.write("Bu dosya hata kontrolü için açılmıştır\n")
    dosya.write("--------------------------------------\n")
    try:
        a = int(input("Lütfen bir sayı giriniz: "))
    except ValueError:
        obj = AES.new('This is a key128', AES.MODE_CBC, 'This is an IV456')
        message = "ValueErrorHappen"
        ciphertext = obj.encrypt(message)
        dosya.write(str(ciphertext))
        dosya.write("||")
        dosya.write("Hatanın alındığı zaman: {}".format(datetime.datetime.now()))
except IOError:
    print("Dosya bulunamadı..!")

    # Python Crypography Toolkit => Bu module hem güvenli karma fonksiyonların hemde çeşitli şifreleme algoritmalarının (AES,DES
    # RAS vb) koleksiyonudur. En önemli özelliği yeni modüller eklemeyi kolylaştıracak şekilde yapılandırılmıştır. Aşağıdaki
    # linkten detaya erişebilirsiniz.

    # https://pypi.org/project/pycrypto/
    # https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

