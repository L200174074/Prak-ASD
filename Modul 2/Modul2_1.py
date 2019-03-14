class Pesan (object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
        
    def apakahTerkandung(self, text):
        if text in self.teks:
            return True
        else:
            return False
            
    def hitungKonsonan(self):
        con = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        jCon = 0
        for i in self.teks :
            if i in con:
                jCon +=1
        return jCon
            
    def hitungVokal(self):
        voc = 'aiueoAIUEO'
        jVoc = 0
        for i in self.teks :
            if i in voc:
                jVoc +=1
        return jVoc
    
    
        