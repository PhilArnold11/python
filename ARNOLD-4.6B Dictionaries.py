nato_alphabet = {'A':'Alpha', " ":" ", 'B':'Bravo', 'C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'X-ray', 'Y':'Yankee', 'Z':'Zulu'}

def spell_word():
    user_word = input('Enter any word: ')
    uppercase_text = user_word.upper() #I couldn't figure this out for some reason. I googled it and used the results from this page https://flexiple.com/python/python-uppercase
    for letter in uppercase_text:
        if letter in nato_alphabet:
        print()
spell_word()

def main():
    spell_word()
main()