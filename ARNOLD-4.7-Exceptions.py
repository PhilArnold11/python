nato_alphabet = {'A':'Alpha', " ":" ", 'B':'Bravo', 'C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'X-ray', 'Y':'Yankee', 'Z':'Zulu'}
#created dictionary using NATO alphabet
def spell_word():#define function
    user_word = input('Enter any word: ')#ask user for input
    for letter in user_word:
        letter = letter.upper()#convert string to uppercase
        if letter in nato_alphabet:
            print(nato_alphabet[letter])#if the letter is found the NATO definition is printed out

def main():#encapsulate in main function and call spell word
    spell_word()
main()
