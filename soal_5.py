# tahunkabisat

print("Menentukan Tahun Kabisat")


def is_kabisat(tahun):
    if tahun % 400 == 0:
        print('true')
    elif tahun % 4 != 0:
        print('false')
    elif tahun % 400 != 0:
        if tahun % 100 != 0:
            if tahun % 4 == 0:
                print('true')
            elif tahun % 100 == 0:
                print('false')


# is_kabisat(2020)

a = int(input('Masukkan Tahun:'))
print(is_kabisat(a))
b = int(input('Masukkan Tahun :'))
print(is_kabisat(b))
