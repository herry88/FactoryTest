def fib(n):
    if (n <= 2):
        return 1
    else:
        return (fib(n-1)+fib(n-2))
print ("fungsi untuk menampilkan deret fibonacci sebanyak x buah")
n = int (input("masukkan x:"))
for i in range (1,n):
    print (fib(i))