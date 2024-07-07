# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.

s = 'launch school tech & talk'

def capitalize(sentence):
    words = sentence.split(' ')
    capitalized = []
    for word in words:
        capitalized.append(word.capitalize())

    return ' '.join(capitalized)


print(capitalize(s))
