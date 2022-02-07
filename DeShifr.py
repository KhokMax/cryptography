letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def coder(phrase, key):
    coder_phrase = []
    for i in phrase:
        if i == " ":
            coder_phrase.append(" ")
        else:
            if((letter_list.index(i) + key) <  25):
                coder_phrase.append(letter_list[letter_list.index(i) + key])
            else:
                coder_phrase.append(letter_list[(letter_list.index(i) + key) -
                                                len(letter_list)])
    print("".join(coder_phrase).upper())

def decoder(phrase, key):
    coder_phrase = []
    for i in phrase:
        if i == " ":
            coder_phrase.append(" ")
        else:
            if ((letter_list.index(i) - key) >= 0):
                coder_phrase.append(letter_list[letter_list.index(i) - key])
            else:
                coder_phrase.append(letter_list[(letter_list.index(i) - key) +
                                                len(letter_list)])
    print( str(key) +". "+ "".join(coder_phrase).upper())

def main():
    phrase = str(input())
    phrase = phrase.lower()
    '''
    key = int(input())
    print(coder(phrase, key))
    '''
    for i in range(0, len(letter_list)):
        decoder(phrase, i)
main()