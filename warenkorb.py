"""
Hier wird die Klasse Warenkorb mit ihren Methoden implementiert
"""

# pylint: disable = missing-function-docstring, missing-class-docstring

class Warenkorb():
    preise = {"shirt": 20, "hose": 35, "jacke": 50}
    shirts = 0
    pants = 0
    jackets = 0
    def __init__(self):
        self.__artikel = []
        self.__price = 0


    def increseprice(self, incr):
        self.__price = self.__price + incr

    def addartikel(self, artikel):
        self.__artikel.append(artikel)
        self.increseprice(int(self.preise[artikel]))
        if artikel == "shirt":
            self.shirts += 1
        elif artikel == "hose":
            self.pants += 1
        elif artikel == "jacke":
            self.jackets += 1

    def getartikel(self):
        return self.__artikel

    def getprice(self):
        return self.__price

    def calcdiscount(self):
        disc = 0
        if self.shirts >= 5:
            self.__price -= 20
        if self.pants > 2:
            disc = self.pants * 3
            self.__price -= disc
        return self.__price

