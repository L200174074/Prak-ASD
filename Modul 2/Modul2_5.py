from LatOOP3 import Manusia

class Mahasiswa(Manusia):
    List = []
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM'+ str(self.NIM)\
            +'. Tinggal di'+self.kotaTinggal\
            +'.Uang Saku Rp ' + str(self.uangSaku)\
            +' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan ",s," sambil belajar.")
        self.keadaan = 'kenyang'
        
    def listKuliah(self):
        return self.List
    def ambilKuliah(self, ambil):
        self.List.append(ambil)
        
    def hapusKuliah(self, hapus):
        self.List.remove(hapus)

        
        
        
