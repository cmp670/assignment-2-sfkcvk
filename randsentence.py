import random

Verb = ["ate", "wanted", "kissed", "washed", "pickled"]
Det = ["the", "a", "every"]
Noun = ["president", "sandwich", "pickle", "mouse", "floor"]
Adj = ["fine", "delicious", "beatiful", "old"]
Prep = ["with", "on", "under", "in"]

class Node:
    def __init__(self, data):
        self.data = ""
        self.left = None
        self.right = None
        
        if data == "S":
            self.left = Node("NP")
            self.right = Node("VP")
        elif data == "VP":
            self.left = Node("Verb")
            self.right = Node("NP")
        elif data == "NP":
            if random.randint(0, 1) == 0:
                self.left = Node("Det")
                self.right = Node("Noun")
            else:
                self.left = Node("NP")
                self.right = Node("PP")
        elif data == "PP":
            self.left = Node("Prep")
            self.right = Node("NP")
        elif data == "Noun":
            if random.randint(0, 1) == 0:
                self.left = Node("Adj")
                self.right = Node("Noun")
            else:
                self.data = Noun[random.randint(0, len(Noun) - 1)]
        elif data == "Verb":
            self.data = Verb[random.randint(0, len(Verb) - 1)]
        elif data == "Det":
            self.data = Det[random.randint(0, len(Det) - 1)]
        elif data == "Adj":
            self.data = Adj[random.randint(0, len(Adj) - 1)]
        elif data == "Prep":
            self.data = Prep[random.randint(0, len(Prep) - 1)]

    def TraverseTree(self) -> str:
        if self.left and self.right:
            return str(self.left.TraverseTree()) + " " + self.data + " " + str(self.right.TraverseTree()) 
        elif self.left:
            return str(self.left.TraverseTree()) + " " + self.data
        elif self.right:
            return self.data + " " + str(self.right.TraverseTree())
        else:
            return self.data
        

root = Node("S")

sentence = root.TraverseTree()

print(sentence)

f = open("random-sentence.txt", "w")
f.write(sentence)
f.close()
