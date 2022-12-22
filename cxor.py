def xorcrypt(k, m):
    crypt = ''
    for i in m:
        crypt += chr(ord(i)^k)
    data  = crypt
    return data

code = input("Введите текст: ")
key = int(input("Введите ключ: "))
codecs = xorcrypt(key, code)
decodecs = xorcrypt(key, codecs)

print(code)
print(codecs)
print(decodecs)

