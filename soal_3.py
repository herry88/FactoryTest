listangka = [94, 92, 96, 70, 83, 87, 84, 80]
nilai_terkecil = listangka[0]
nilai_terbesar = listangka[0]

nilai_rata_rata = 0
jumlah_nilai = 0
jumlah_elemen = 0

for nilai in listangka:
    # menaikkan jumlah elemen seirin perulangan
    jumlah_elemen = jumlah_elemen + 1
    # akumulasikan jumlah nilai sementara
    jumlah_nilai = jumlah_nilai + nilai
    # jika nilai yang diperiksa lebih besar
    if nilai_terbesar < nilai:
        nilai_terbesar = nilai
    if nilai_terkecil > nilai:
        nilai_terkecil = nilai

nilai_rata_rata = jumlah_nilai / jumlah_elemen
print('isi list :', listangka)
print('nilai terbesar :', nilai_terbesar)
print('nilai terkecil :', nilai_terkecil)
print('jumlah elemen :', jumlah_elemen)
print('Akumulasi :', jumlah_nilai)
print('rata rata', nilai_rata_rata)
