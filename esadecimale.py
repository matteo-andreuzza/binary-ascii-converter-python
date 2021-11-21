numch = ""
n=int(input("Numero decimale"))
deci = [10, 11, 12, 13, 14, 15 ]
esa = ["a", "b", "c", "d", "e", "f"]

if n <= 0:
    numch = "0"
else:
    while n != 0:
        x = n % 16
        n = int(n / 16)

        if x < 10:
            numh = str(x)
        else:
            for i in range(7):
              if x == deci[i-1]:
                numh = esa[i-1]

        numch = numh + numch

print("Numero esadecimale",numch)