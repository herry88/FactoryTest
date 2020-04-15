def cekpalindrom(text):
    list = []
    belakang = ""
    depan = ""
    indikator = True
    for i in range(len(text)):
        if text[i] != ',' and text[i] != '.' and text[i] != '""' and text[i] != "'" and text[i] != '"' and text[
            i] != '!' and text[i] != '?' and text[i] != ' ':
            list.append(text[i])
        while len(list) > 1 and indikator:
            depan += list.pop(0)
            belakang += list.pop()
            if belakang != depan:
                indikator = False
            if indikator:
                print(text, 'adalah palyndrom')
            else:
                print(text, 'bukan kalimat palyndrom')


a = input('Masukkan text:')
print('Hasil :')
cekpalindrom(a)
