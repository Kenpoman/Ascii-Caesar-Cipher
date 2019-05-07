import socket

knownStrings = ['I|am|serious|and|don\'t|call|me|Shirley.', 'Gentlemen,|you|can\'t|fight|in|here!|This|is|the|War|Room!',
        'Attica.|Attica.', 'Plastics', 'You|can\'t|handle|the|truth.', 'You\'re|gonna|need|a|bigger|boat.',
        'One|morning|I|shot|an|elephant|in|my|pajamas.|How|he|got|in|my|pajamas,|I|don\'t|know.',
        'Nobody|puts|Baby|in|a|corner.', 'Rosebud', 'Forget|it,|Jake,|it\'s|Chinatown.',
        'I|love|the|smell|of|napalm|in|the|morning.', 'I|am|big.|It\'s|the|pictures|that|got|small.',
        'Here\'s|looking|at|you,|kid.', 'Listen|to|them.|Children|of|the|night.|What|music|they|make.',
        'A|boy\'s|best|friend|is|his|mother.', 'brothers|don\'t|shake|hands,|brothers|gotta|hug']
ipTuple = ('10.0.1.17', 5252)
sock = socket.socket()
def connect():
    sock.connect(ipTuple)
    sock.recv(1024)
    sock.recv(1024)
    sock.send('PineApple')
    cipherText = sock.recv(1024)
    cipherText = cipherText[:-1]
    return cipherText
def grabNewQuote():
    newQuote = sock.recv(1024)
    newQuote = newQuote[:-1:]
    print(newQuote)
    return newQuote
    #theString = theString[:-1:]
def shift(ct):
    for i in range(1,92):
        encoded = []
        for x in ct:
            if (ord(x) + i > 124):
                encoded.append(chr(ord(x)+i-92))
            else:
                encoded.append(chr(ord(x)+i))
        myString = ''.join(encoded)
        error = False
        for x in knownStrings:
            if(myString == x):
                myString = myString.replace('|',' ')
                sock.send(myString)
                print(myString)
                print('Sent')
                error = True
            else:
                print(myString)
    return encoded
def main():
    cipherText = connect()
    shift(cipherText)
    for i in range(1):
        shift(grabNewQuote())
main()
