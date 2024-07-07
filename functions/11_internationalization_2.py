# Write a function local_greet that takes a locale as input, and returns a greeting. 
# The locale lets us greet people from different countries appropriately, even when they share a common language


def local_greet(locale):

    def extract_language(locale):
        return locale.split('_')[0]

    def extract_region(locale):
        return locale.split('.')[0].split('_')[1]
    
    def greet(language):
        match language:
            case 'fr':
                return 'Salut!'
            case'pt':
                return 'Olá!!'
            case 'de':
                return 'Hallo!'       
            case 'sv':
                return 'Hej!'
            case 'af':
                return 'Haai!'
            case _:
                return'¯\_(ツ)_/¯'
        
    language = extract_language(locale)
    region = extract_region(locale)

    if language == 'en':
        if region == 'US':
            return 'Hey!'
        elif region == 'AU':
            return 'Howdy!'
        else:
            return 'Hello!'
    else:
        return greet(language)



print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
