# Use Python's control structures to create a function that takes an ISO 639-1 language code 
# and returns a greeting in that language. 
# You can take the examples below or add whatever languages you like.

def greet(language):
    if language == 'en':
        return "Hi!"
    elif language == 'fr':
        return 'Salut!'
    elif language == 'pt':
        return 'Olá!!'
    elif language == 'de':
        return 'Hallo!'       
    elif language == 'sv':
        return 'Hej!'
    elif language == 'af':
        return 'Haai!'
    else:
        return'¯\_(ツ)_/¯'


print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
