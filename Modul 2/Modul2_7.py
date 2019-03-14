from LatOOP4 import Mahasiswa #Atau apapun file-nya yang kamu buat tadi

class MhsTIF(Mahasiswa): # Perhatikan class induknya : Mahasiswa
    """ Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool')
        
"""
Metode yang berasal dari class Manusia :

nama
NIM
uangSaku
ambilNama
ambilNIM
ambilUangSaku
makan
kotaTinggal

Metode yang berasal dari class Mahasiswa :

ucapkanSalam
olahraga
mengalikanDenganDua
keadaan

Metode yang berasal dari class MhsTIF :

katakanPy

"""
