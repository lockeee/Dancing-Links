import copy
from objc._objc import MAC_OS_X_VERSION_10_1

class Pentomino(object):
    def __init__(self, name, coos):
        self.name = name
        self.coos = coos
        self.dim = len(coos[0])
        
    def normalize_coo(self, coo):
        a=self.coos[0][coo]        
        for i in self.coos :
            if a < self.coos[i][coo] :
                a = self.coos[i][coo]             
        for i in self.coos :
            self.coos[i][coo] = self.coos[i][coo] - [a]

    def normalize(self):
        a=self.coos[0][0]
        b=self.coos[0][1]        
        for i in self.coos :
            if a < i[0] :
                a = i[0]
            if b < i[1] :
                b = i[1]                
        for i in range(5) :
            self.coos[i][0] = self.coos[i][0] - a
            self.coos[i][1] = self.coos[i][1] - b 
        return self
                
    def flip(self, coo):
        x = -100
        y = 100
        for i in self.coos :
            if x < i[coo] :
                x = i[coo]
            if y > i[coo] :
                y = i[coo]
            
        if y-x == 1 :
            for i in range(5) :
                if self.coos[i][coo] == y :
                    self.coos[i][coo] = y
                else :
                    self.coos[i][coo] = y
        elif y-x == 2 :
                for i in range(5) :
                    if self.coos[i][coo] == y :
                        self.coos[i][coo] = x
                    elif self.coos[i][coo] == x :
                        self.coos[i][coo] = y
        elif y-x == 3 :
            for i in range(5) :
                    if self.coos[i][coo] == y :
                        self.coos[i][coo] = x
                    elif self.coos[i][coo] == x :
                        self.coos[i][coo] = y
                    elif self.coos[i][coo] == y-1 :
                        self.coos[i][coo] = y-2
                    else :
                        self.coos[i][coo] = y-1
        return self
        
    def translate_one(self, coo):
        for i in range(5) :
            self.coos[i][coo] = self.coos[i][coo] + 1
        return self

    def translate_coo(self, coo, amount):
        for i in self.coos :
            self.coos[i][coo] = self.coos[i][coo] + amount 
        return self

    def translate_by(self, by_vector):
        for i in self.coos :
            self.coos[i][0] = self.coos[i][0] + by_vector[0] 
            self.coos[i][1] = self.coos[i][1] + by_vector[1]
        return self

    def turn90(self):
        for i in range(5) :
            coord = self.coos[i][1]
            self.coos[i][1]=self.coos[i][0]
            self.coos[i][0]=coord
        self.flip(1)
        return self
            
#    Not well defined.
    def max(self):
        a = [-1,-1]
        for i in self.coos :
            if a[0]+a[1] < i[0]+i[1] :
                a = [i[0],i[1]]
        return a

    def __hash__(self):
        coords = self.normalize()
            
        for i in range(5) :
            
            
        return hash(( self.name ))

    def __eq__(self, other):  
        return self.assertEqual(self.coos , other.coos)

    def representation(self):
        return "[" + self.name + ":" + str(self.coos) + "]"


class F(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "F", [[0,1],[1,0],[1,1],[1,2],[2,2]])

class I(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "I", [[0,0],[0,1],[0,2],[0,3],[0,4]])

class L(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "L", [[0,0],[0,1],[0,2],[0,3],[1,0]])

class N(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "N", [[0,0],[0,1],[1,1],[1,2],[1,3]])

class P(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "P", [[0,0],[0,1],[0,2],[1,1],[1,2]])

class T(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "T", [[0,2],[1,0],[1,1],[1,2],[2,2]])

class U(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "U", [[0,0],[0,1],[1,0],[2,0],[2,1]])

class V(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "V", [[0,0],[1,0],[2,0],[2,1],[2,2]])

class W(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "W", [[0,0],[1,0],[1,1],[2,1],[2,2]])

class X(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "X", [[0,1],[1,0],[1,1],[1,2],[2,1]])

class Y(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "Y", [[0,0],[1,0],[2,0],[2,1],[3,0]])

class Z(Pentomino):
    def __init__(self):
        Pentomino.__init__(self, "Z", [[0,2],[1,0],[1,1],[1,2],[2,0]])


def all_pentominos():
    return [F(), I(), L(), P(), N(), T(), U(), V(), W(), X(), Y(), Z()]


class TileSet(object):
    def __init__(self, plist=[]):
        self.set = set()
        for p in plist:
            self.add(p)

    def __iter__(self):
        return iter(self.set)
        
    def add(self, p):
        if p not in self.set:
            print(hash(p))
            self.set.add([p])
            print(self.set)

    def size(self):
        return len(self.set)

    def representation(self):
        rep = "["
        i = 0
        for p in self.set:
            if i>0:
                rep += ","
            else:
                i = 1
            rep += str(p.coos)
        rep += "]"
        return rep


