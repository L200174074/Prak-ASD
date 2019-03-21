#Nomor 1
m1 = [[3,2],[5,7]]
m2 = [[15,30],[9,5]]

def cekMatrix(matrix):
    jum = len(matrix)
    hasil = ""
    for x in matrix:
        for i in x:
            assert isinstance(i, int), "Harus Integer"
        return True
    
def ukuran(matrix):
    return("Ukuran Matrix = "+str(len(matrix))+" x "+str(len(matrix[0])))

def jumlah(matrix1, matrix2):
    if ukuran(matrix1) == ukuran(matrix2):
        for x in range(0, len(matrix1[0])):
            print(matrix1[x][y] + matrix2[x][y], end=' '),
        print()
    else:
        print("Matrix Tidak Sesuai")
        
def mengalikanMatrix(matrix1,matrix2):
    mat3 =[]
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            row = []
            for y in range(0, len(matrix1[0])):
                total = 0
                for z in range(0, len(matrix)):
                    total = total + (matrix1[x][z]* martix2[z][y])
                row.append(total)
            mat3.append(row)
            
        for x in range(0, len(mat3)):
            for y in range(0, len(mat3[0])):
                print(mat3[x][y], end = ' ')
            print()
    else :
        print("Matrix tidak sesuai")
        
def determinan(matrix):
    if len(matrix) == len(matrix[0]):
        bil = [x for x in range(len(matrix))]
        jum = 0
        for i in range(len(matrix)):
            total = 1
            for x in range(len(matrix)):
                total *= matrix[x][bil[x]]
            bil += [bil2.pop()]
            jum += total
        bil2 = [x for x in range(len(matrix))]
        bil.reverse()
        jum2 = 0
        for i in range(len(matrix)):
            total2 = 1
            for x in range(len(matrix)):
                total2 *= matrix[x][bil2[x]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total-total2)
        return ""
    else:
        print("Matrix Harus Bujursangkar")
    
        
    
    
#Nomor 2
def buatNol(m,n) :
    matrix : [[0 for j in range(m)]for i in range(n)]
    print(matrix)
    
def buatNol2(m) :
    n = m
    matrix : [[0 for j in range(m)]for i in range(n)]
    print(matrix)
    
def buatIdentitas(m):
    identitas = [[1 if j==i else 0 for j in range(m)]for i in range(m)]
    print(identitas)
    
#Nomor 3
    
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def kunjungi(head):
        curNode = head
        while curNode is not None :
            print(curNode.data)
            curNode = curNode.next
            
    def cari(head, yang_dicari):
        curNode = head
        while curNode is not None :
            if curNode.data == cari:
                print("Data berhasil ditemukan")
            else :
                print("Data tidak ditemukan, periksa kembali data anda !")
            cureNode = cureNode.next
            
    def tambahDepan(head):
        newNode = Node(1)
        newNode.next = head
        head = newNode
        return head
    
    def tambahAkhir(head):
        curNode = head
        while curNode is not None :
            if curNode.next == None :
                newNode = Node(25)
                curNode.next = newNode
                return curNode
            else :
                pass
            curNode = curNode.next
        return curNode
    
    def tambah(head, posisi):
        newNode = Node(8)
        newnNode.next = posisi.next
        posisi.next = newNode
        head.head = posisi
        return head
    
    def hapus(posisi):
        curNode = head
        while curNode is not None :
            if curNode.next.data == posisi :
                curNode.next = curNode.next.next
                return curNode
            else:
                pass
            curNode = curNode.next
        return curNode
    
#Nomor 4
    
class doubly_linked():
    def __init__(self, data):
        self.data = data
        self.next = None
        delf.prev = None
        
    def cetakData():
        curNode = head
        while curNode is not None :
            print(curNode.data)
            if curNode.next == None:
                curNode = curNode
                break
            else:
                curNode = curNode.next
        print("\n")
        while curNode is not None :
            print(curNode.data)
            curNode = curNode.prev
            
    def simpulAwal(head):
        newNode = doubly_linked(25)
        newNode.next = head
        head.prev = newNode
        head = newNode
        return head
        
    def simpulAkhir(head):
        curNode = head
        while curNode is not None:
            if curNode.next == None:
                newNode = double_linked(365)
                curNode.next = newNode
                newNpde.prev = curNode
                return curNode
            else:
                pass
            curNode = curNode.next
        return curNode
    
            
    