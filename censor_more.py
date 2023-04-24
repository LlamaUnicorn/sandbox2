abc = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
profanity = ['cunt', 'fag']
print('profanity:', profanity)

check = 'You fag! Stupid Cunt! \nEdge case: Fag\'s voice'
print('check text:', check)

check_list = check.split()
print('check_list:', check_list)
check_list_no_sp_chars = [j.strip('.,!?:;').lower() for j in check_list]
print('check_list_no_sp_chars:', check_list_no_sp_chars)

i = 0
print('loops are next')

for word in check_list_no_sp_chars:
    print('word:', word)
    if word in profanity:
        print('this is profanity')
        x = list(check_list[i])
        print('x:', x)
        censored_word = []
        for char in x:
            if char in abc:
                char = '*'
                censored_word.append(char)
            else:
                censored_word.append(char)
        print('censored_list', censored_word)
        result = ''.join(censored_word)
        print('result after censoring:', result)
        check_list[i] = result
    i += 1
    print('i', i)

print('check_list:', check_list)
censored_text = ' '.join(check_list)
print('final censored text:', censored_text)
