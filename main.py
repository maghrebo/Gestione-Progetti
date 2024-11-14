
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