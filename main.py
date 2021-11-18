def principale():
    while True:
        print("[1] = converti da binario a testo")
        print("[2] = converti da testo a binerio")
        print()
        mod = input('scegli modalità (1/2), esc per uscire ')


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
        elif mod == 'esc':
            quit()
        else:
            print('modo non supportato, codice eroore 1')
            principale()
    
principale()