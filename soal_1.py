score = eval(input("Masukkan Nilai"))

# logic
if score >= 90:
    print("grade A")
elif 80 <= score < 90:
    print("grade B")
elif 70 <= score < 79:
    print("grade C")
elif 60 <= score < 69:
    print("grade D")
else:
    print("grade E")

