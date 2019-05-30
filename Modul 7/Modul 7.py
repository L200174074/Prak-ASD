import re

s = 'sebuah contoh kata:teh!!'
cocok = re.findall(r'kata:\w\w\w', s)
if cocok:
    print('menemukan', cocok)
else :
    print('tidak menemukan')

# Contoh 7.2
cocok = re.findall(r'eee', 'teeeh')
print(cocok)
cocok = re.findall(r'ehs', 'teeeh')
print(cocok)

cocok = re.findall(r'..h', 'teeeh')
print(cocok)

cocok = re.findall(r'\d\d\d', 't123h di 2019 bulan 02')
print(cocok)
cocok = re.findall(r'\w\w\w', '@@a*bc#def*tghh!!')
print(cocok)


#Contoh Pengulangan 7.3.1
cocok = re.findall(r'te+', 'ghdteeeh')
print(cocok)

polanya = r'\d\s*\d\s*\d'
cocok = re.findall(polanya, 'xx1 2   3xx')
print(cocok)
cocok = re.findall(polanya, 'xx12   3xx')
print(cocok)
cocok = re.findall(polanya, 'xx123xx')
print(cocok)

cocok = re.findall(r'^k\w+', 'mejakursi')
print(cocok)
cocok = re.findall(r'k[\w\s]+', 'mejakursi tamu saya')
print(cocok)

s ='Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'\w+@\w+',s)
print(cocok[0])

#Kurung Siku 7.3.2
cocok = re.findall(r'[\w.-]+@[\w.-]+', s)
print(cocok[0])

#Ekstraksi Secara Group 7.4
s ='Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'([\w.-]+)@([\w.-]+)', s)
cocok
cocok[0][0]
cocok[0][1]

s = 'Alamatku sri@google.com serta joko@abs.com ok broi. atau don@email.com'

pola = r'[\w\.-]+@[\w\.-]+'
e = re.findall(pola, s)
print(e)


#Group polanya menjadi username dan host

pola = r'([\w\.-]+)@([\w\.-]+)'
e = re.findall(pola, s)
print(e)

for tup in e:
    print('user', tup[0], 'dengan host:',tup[1])

#Pencarian dalam berkas 7.4.1
f = open('test.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'ta\w*'
strings = re.findall(p, teks)




#Soal Latihan 7.6

#No 1

f = open('Indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'me\w*'
strings = re.findall(p, teks)

#No 2
f = open('Indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'di\w*'
strings = re.findall(p, teks)

#No 3
f = open('Indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'di\s\w*'
strings = re.findall(p, teks)

#No 4
#a
f = open('KEI.html', 'r', encoding='latin1')
teks = f.read()
f.close()
p=r'([\w+]+)</a></td>'
strings = re.findall(p, teks)

#b
f = open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
string=re.findall(r'title="([\w+]+)">',teks)
string=re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)
a=[]
for i in string:
    a.append((i[0], float(i[1])))
print(a)



