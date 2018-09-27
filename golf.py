class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return self.rank + self.suit

class Deck:

    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['h','c','d','s']
    cards = []

    def shuffle(self):
        # probably not random

        import random
        random.shuffle(self.cards)

    def pickup(self):
        return self.cards.pop()

    def __init__(self, rand=False):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))
        if rand:
            self.shuffle()

    def __str__(self):
         return ','.join([str(card) for card in self.cards])

class Golf:

    deck = False
    board = []
    stack = []
    width = 7
    depth = 5
    
    def __init__(self, custdeck=False):
        if custdeck:
            self.deck = custdeck
        else:
            self.deck = Deck(True)

        for x in range(self.width):
            self.board.append([])

        for x in range(self.depth):
            for col in self.board:
                col.append(self.deck.pickup())

    def __str__(self):
        retstr = "\n\n\nOn Deck: " + str(self.stack[0]) + "\n" 
        retstr = retstr + "Rest of stack:" + ' '.join([ str(x) for x in self.stack[1:]]) + "\n"
        retstr = retstr + "remaining cards in deck:" + str(len(self.deck.cards)) + "\n"
        retstr = retstr + "-------------------------------------------------\n"
        retstr = retstr + "\t".join([str(x + 1) for x in range(self.width)]) + "\n"

        for y in range(self.depth):
            for x in range(self.width):
                try:
                    retstr = retstr + str(self.board[x][y]) + "\t"
                except:
                    retstr = retstr + "  \t"
            retstr = retstr + "\n"
        return retstr
            
    def empty(self):
        for col in self.board:
            if len(col) != 0:
                return False
        return True

    def valid(self, card1, card2):
        
        rank1 = card1.rank
        rank2 = card2.rank

        id1 = self.deck.ranks.index(card1.rank)
        id2 = self.deck.ranks.index(card2.rank)
        if rank1 == 'A':
            if rank2 == '2' or rank2 == "K":
                return True
        if rank2 == 'A':
            if rank1 == '2' or rank1 == "K":
                return True

        if abs(id1 - id2) == 1:
            return True


    def move(self, num):
        col = self.board[num]

        if len(col) == 0:
            return False
        if num > self.width:
            return False
        
        if not self.valid(self.stack[0], self.board[num][-1]):
            return False

        card = self.board[num].pop()
        self.stack.insert(0, card)

        return True

        

    def play(self):

        self.stack.insert(0, self.deck.pickup())

        while self.empty() != True:
            print self
            input = raw_input("Input Col # or h to Hit: ");

            if input == "p":
                for col in self.board:
                    for card in col:
                        print card
                    print "---" 

            elif input == "h":
                if len(self.deck.cards):
                    self.stack.insert(0, self.deck.pickup())
                else:
                    print "Deck empty!"
            elif input.isdigit() and int(input) in range(1, self.width + 1):
                if self.move(int(input) - 1):
                    print "OK!"
                else:
                    print "Invalid Move!"
            else:
                print "?"

        print "Good Game!"



g = Golf()
g.play()
