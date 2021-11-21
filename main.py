def principale():
    print("Telemaco versione 0.2.2")
    print("visita efish.altervista.org/telemaco")
    while True:
        print("[1] = converti da binario a testo")
        print("[2] = converti da testo a binario")
        print("[3] = converti da da esadecimale a decimale")
        print("[4] = converti da decimale a esadecimale")
        print()
        mod = input('scegli modalità (1/2/3/4), esc per uscire ')


        #definisco il metodo
        if mod == '1':
            a_binary_string = input("inserisci il codice binario con le lettere separate da spazi.. ")
            try:
                ascii_string = "".join([chr(int(binary, 2)) for binary in a_binary_string.split(" ")])
                print(ascii_string)
            except ValueError:
                print("errore di conversione, controlla gli spazi tra i numeri, all'inizio o alla fine.")
                print("codice errore: 2")
                print("visita efish.altervista.org/binario per maggiori informazioni")
        elif mod == '2':
            st = input("inserisci il tuo testo ")
            bin = ' '.join(format(x, 'b') for x in bytearray(st, 'utf-8'))
            print(bin)
        elif mod == '3':
            valori= {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8": 8, "9": 9, "A": 10, "B": 11, "C":12, "D":13, "E": 14, "F":15}
            def esadecimale_a_decimale(number):
                try:
                    list=[]
                    number = number.upper()
                    sum=0
                    power=0
                    for i in number:
                        list.append(i)
                    list.reverse()
                    for i in list:
                        t=valori.get(i)
                        sum=sum+t*16**power
                        power=power+1
                    return sum
                except ValueError:
                    print("modo non supportato, riavvio il programma")
                    print("codice erroe: 2")
                    principale()
            print(esadecimale_a_decimale(input("Please put a hexadecimal number : ")))
        elif mod == '4':
            numch = ""
            n=int(input("Numero decimale"))
            deci = [10, 11, 12, 13, 14, 15 ]
            esa = ["a", "b", "c", "d", "e", "f"]
            try:
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
            except ValueError:
                print("modo non supportato, riavvio il programma")
                print("codice erroe: 2")
                principale()
        elif mod == 'esc':
            quit()
        else:
            print('modo non supportato, codice eroore 1')
            principale()
    
principale()