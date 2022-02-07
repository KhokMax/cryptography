letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def coder(phrase, A, B, C):
    coder_phrase = []
    for i in range(0,len(phrase)):
        if phrase[i] == ' ':
            coder_phrase.append(' ')
        else:
            coder_phrase.append(
                letter_list[((letter_list.index(phrase[i]) + A * i * i + B * i + C) % 26)])
    print("".join(coder_phrase).upper())

def decoder(phrase, A, B, C):
    coder_phrase = []
    for i in range(0,len(phrase)):
        if phrase[i] == ' ':
            coder_phrase.append(' ')
        else:
            coder_phrase.append(
                letter_list[
                    ((letter_list.index(phrase[i]) - (A * i * i + B * i + C)) % 26)])
    print(str(A) + ' ' + str(B) + ' ' + str(C) + ' ' + "".join(coder_phrase).upper())

def main():

    phrase = str(input())
    phrase = phrase.lower()
    '''
    A = int(input())
    B = int(input())
    C = int(input())
    coder(phrase, A, B, C)
    '''
    for i in range(0,6):
        for j in range(0,6):
            for k in range(0, 6):
                decoder(phrase, i, j, k)


main()