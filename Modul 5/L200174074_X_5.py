def swap (A, p, q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini            #-> anggap ini yang terkecil
    for i in range(dariSini+1, sampaiSini):  #-> cari di sisa list
        if A[i] < A[posisiYangTerkecil]:     #-> kalau menemukan yang lebih keil,
            posisiYangTerkecil = i           #-> anggap dirubah
    return posisiYangTerkecil

# Buble Sort

def bubleSort(A):
    n = len(A)
    for i in range (n-1):       #-> Lakukan operasi gelembung sebanyak n-1
        for j in range(n-i-1):  #-> Dorong elemen terbesar ke ujung kanan
            if A[j] > A[j+1]:   #-> Jika di kiri lebih besar dari di kanannya,
                swap(A,j,j+1)   #-> tukar posisi elemen ke j dengan ke j+1

# Selection Sort

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

# Insertion Sort

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:   #-> Cari posisi yang tepat
            A[pos] = A[pos -1]                 #-> dan geser ke kanan terus
            pos = pos - 1                       #-> nilai-nilai yang lebih besar
        A[pos] = nilai                          #-> Pada posisi ini tempat nilai elemen ke i.

# No 1

class MhsTIF(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x=str(self.NIM)+" "+self.nama+" "+self.kotaTinggal+" "+str(self.uangSaku)
        return x
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.NIM
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chandra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 245000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c8, c9, c10]

def sortNIM(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.NIM < A[pos - 1].NIM:   #-> Cari posisi yang tepat
            A[pos] = A[pos -1]                 #-> dan geser ke kanan terus
            pos = pos - 1                       #-> nilai-nilai yang lebih besar
        A[pos] = nilai                          #-> Pada posisi ini tempat nilai elemen ke i.

sortNIM(Daftar)
print('\n'.join(map(str, Daftar)))

# No 2

A = [1, 2, 3, 4, 5]
B = [6, 8, 10]

def satukanArray(x, y):
    C = x + y
    n = len(C)
    for i in range(1, n):
        nilai = C[i]
        pos = i
        while pos > 0 and nilai < C[pos - 1]:   #-> Cari posisi yang tepat
            C[pos] = C[pos -1]                  #-> dan geser ke kanan terus
            pos = pos - 1                       #-> nilai-nilai yang lebih besar
        C[pos] = nilai                          #-> Pada posisi ini tempat nilai elemen ke i.
    print(C)


from time import time as detak
from random import shuffle as kocok
k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubleSort(u_bub);ak=detak();print('buble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));

