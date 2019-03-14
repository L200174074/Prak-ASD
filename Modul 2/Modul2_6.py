from LatOOP3 import Manusia

class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, alamat):
        self.nama = nama
        self.NIS = NIS
        self.alamat = alamat

    def __str__(self):
        s = self.nama + ', NIS'+ str(self.NIS)\
            +'. Tinggal di'+self.alamat + "."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIS(self):
        return self.NIS
    def alamat(self):
        return self.alamat
