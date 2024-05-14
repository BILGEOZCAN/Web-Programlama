from random import randint
import time

class Arac:
    yol = []

    def __init__(self, i, xi, yi):
        self.i = i
        self.x = xi
        self.y = yi
        self.yol = []
        self.R = randint(0, 255)
        self.G = randint(0, 255)
        self.B = randint(0, 255)
        self.bitti = False

    def getRGB(self):  # Rengi döndür
        return (self.R, self.G, self.B)

    def getIzleme(self):  # İzlemeyi döndür
        return self.yol

    def getId(self):  # Kimlik için
        return self.i

    def getX(self):  # X koordinatı
        return self.x

    def getY(self):  # Y koordinatı
        return self.y

    def koordinat(self, xn, yn):  # Koordinatı güncelle
        self.yol.append([self.x, self.y])
        self.x = xn
        self.y = yn

    def yukariGit(self, bas, son):  # Yukarı yönde gitti mi?
        if len(self.yol) >= 2:
            if self.yol[-1][1] < son and self.yol[-2][1] >= son:
                return True
            else:
                return False
        else:
            return False
