from collections import namedtuple

Player = namedtuple('Player', ['number', 'mark'])

Empty = Player(0, '_')
P1 = Player(1, 'O')
P2 = Player(2, 'X')

players = {0: Empty, 1: P1, 2: P2}

def oppositve(p):
    if p == P1:
        return P2
    elif p == P2:
        return P1
    else:
        return Empty
