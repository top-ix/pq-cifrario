#!/usr/bin/python
import sys,string

def cipher(text,k):
    try:
        k = int(k)
        if k<=0 or k%1 != 0:
            print "error, key must be an integer number greater than 0."
            return
        else:
            n = (k%26)
    except:
        print "error, key must be an integer number greater than 0."
        return
    text = list(text)
    dec = []
    ret = ''
    for a in text:
        if a.isalpha():
            c = ord(a)
            if c>= 65 and c<=90:
                #MAIUSCOLA
                c += n
                if c>90: #sforato
                    c = 65 + (c-91)
                d = chr(c)
                ret += d
            elif c>=97 and c<=122:
                #MINUSCOLA
                c += n
                if c>122: #sforato
                    c = 97 + (c-123)
                d = chr(c)
                ret += d
            else:
                print "errore, carattere non riconosciuto: ", c
                ret += d
        else:
            ret += a
    print "result-> \n", ret
    myFile = open("result.txt", "w")
    myFile.write(ret)
    myFile.close()



def decipher(text,k):
    try:
        k = int(k)
        if k<=0 or k%1 != 0:
            print "error, key must be an integer number greater than 0."
            return
        else:
            n = (k%26)
    except:
        print "error, key must be an integer number greater than 0."
        return
    text = list(text)
    dec = []
    ret = ''
    for a in text:
        if a.isalpha():
            c = ord(a)
            if c>= 65 and c<=90:
                #MAIUSCOLA
                c -= n
                if c<65: #sforato
                    c = 90 -(64-c)
                d = chr(c)
                ret += d
            elif c>=97 and c<=122:
                #MINUSCOLA
                c -= n
                if c<97: #sforato
                    c = 122 -(96-c)
                d = chr(c)
                ret += d
            else:
                print "errore, carattere non riconosciuto: ", c
                ret += d
        else:
            ret += a
    print "result-> \n", ret
    myFile = open("result.txt", "w")
    myFile.write(ret)
    myFile.close()




def main():
    if len(sys.argv) != 4:
        print 'usage: ./processing {-c,-d} INPUT_FILE KEY'
        sys.exit(1)

    INPUT_STRING = sys.argv[2]
    KEY = sys.argv[3]
    myFile = open(sys.argv[2], "r")
    INPUT_STRING = myFile.read()
    myFile.close()
    if sys.argv[1] == '-c':
        return cipher(INPUT_STRING, KEY)
    elif sys.argv[1] == '-d':
        return decipher(INPUT_STRING, KEY)
    else:
        print "Errore in input"


if __name__ == '__main__':
    main()

