a= int(input('Masukkan Bilangan ke-1: '))
b= int(input('Masukkan Bilangan ke-2: '))
hasil=[]

tambah=a+b
kurang=a-b
kali=a*b
bagi=a/b
sisa_bagi=a%b

hasil.append(tambah)
hasil.append(kurang)
hasil.append(kali)
hasil.append(bagi)
hasil.append(sisa_bagi)
print(hasil)