abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
censored = ['news', 'stupid']
print('censored:', censored)

news_title = 'Breaking news! This stupid president does unthinkable!'

split_title_special_chars = news_title.split()
print('split_title_special_chars:', split_title_special_chars)
split_title_no_chars = [j.strip('.,!?:;').lower() for j in split_title_special_chars]
print('no special chars split:', split_title_no_chars)
# split_title_comprehension2 = [[j.strip('.,').lower() for j in i] for i in news_title]
# print('list comprehension: ', news_title)
# print(type(split_title_comprehension2))
# print(split_title_comprehension[0])

# print('this is split_title: ', split_title)
i = 0
for word in split_title_no_chars:
    if word in censored:
        list_word = list(word)
        print('list_word:', list_word)
        censored_word = []
        for letter in word:
            letter = '*'
            censored_word.append(letter)
        result = "".join(censored_word)
        print('censored result in for loop:', result)
        split_title_no_chars[i] = result
    i += 1

# for word in split_title_no_chars:
#     if word in censored:
#         list_word = list(word)
#         print('list_word:', list_word)
#         censored_list_word = '*' * len(list_word)
#         # word = '*' * len(list_word)
#         word = censored_list_word
#         print(word)
        
# censored_title = [list(word) for word in split_title_no_chars]
print('this is censored:', split_title_no_chars)

# How to change the original list after censoring with *?


# name = 'Ben'
# word = list(name)
# print(word)
# word = '*' * len(name)
# print(word)


# l = [ ['Hello.', 'My', 'World,'] ]
# res = [[j.strip('.,').lower() for j in i] for i in l]
# print(res)

# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print('-'*20)
# check_word = 'news'
# if check_word in censored:
#     censored_word = []
#     for letter in check_word:
#         letter = '*'
#         censored_word.append(letter)
#     result = "".join(censored_word)
#     print('censored result:', result)
