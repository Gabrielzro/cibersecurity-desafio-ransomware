import os
import pyes

file_name = 'arquivo.txt.criptografado'
file = open(file_name, 'rb')
file_data = file.read()
file.close

os.remove(file_name)

key = b'arquivocriptografado'
aes = pyes.AESModeOfOperationCTR(key)

crypto_data = aes.descrypt(file_data)

new_file = file_name + '.crypto'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()