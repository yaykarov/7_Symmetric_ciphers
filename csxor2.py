def mycrypt(k, m):
    return ''.join(map(chr, (x ^ k for x in map(ord, m))))

code = input("Введите текст: ")
key = int(input("Введите смещение: "))
codecs = mycrypt(key, code)
decodecs = mycrypt(key, codecs)

print(code)
print(codecs)
print(decodecs)


