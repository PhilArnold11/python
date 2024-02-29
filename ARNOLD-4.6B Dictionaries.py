nato_alphabet = {'A':'Alpha', " ":" ", 'B':'Bravo', 'C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Fox-trot', 'G':'Golf', 'H':'Hotel', 'I':'Indigo', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'X-ray', 'Y':'Yankee', 'Z':'Zulu'}

def spell_word():
    user_word = input('Enter any word: ')
    user_word=user_word.capitalize()
    print(user_word)
spell_word()