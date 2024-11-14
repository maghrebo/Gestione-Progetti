
lista = ['banane', 'biscotti', 'caramelle', 'merendine', 'nutella biscuits', 'crema sunsilk']

def aggiunta():

    while True:

        scelta = input('Vuoi aggiungere elementi alla lista? (digita si o no):   ')
        if scelta == 'si':
            aggiunta = input('Che elemento della spesa vorresti aggiungere:  ')
            lista.append(aggiunta)
        elif scelta == 'no':
            print('Va bene hai scelto di no, grazie e arrivederci')
            break
        else:
            print('Hai sbagliato l\'inserimento della scelta, riprova: ')

def stampa_elementi():
    print(lista)

def eliminazione():

    while True:
        decisione = input('Vuoi eliminare un elemento (digita si o no):  ')
        if decisione == 'si':
            while True:
                try:
                    scelta = int(input('Quale elemento vorresti eliminare (inserisci indice):  '))
                    lista.pop(scelta)
                    break
                except:
                    print('Hai inserito un carattere diverso da un numero oppure l\'indice non è presente nella lista, riprova')
                    break
                
                    
        elif decisione == 'no':
            print('Va bene sarai rimandato al menu principale, grazie ')
            break
        else:
            print('Hai inserito una scelta diversa da quelle possibili, riprova')

