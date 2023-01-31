message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг для шифрования: '))
new_message = ''

for ch in message:
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        # print(pos)
        pos = (pos + shift) % 26
        # print(pos)
        new_char = chr(pos + ord('a'))
        # print(new_char)
        new_message = new_message + new_char
    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        pos = (pos + shift) % 26
        new_char = chr(pos + ord('A'))
        new_message = new_message + new_char
    else:
        new_message = new_message + ch
print(new_message)
