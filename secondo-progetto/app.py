from flask import Flask

#Dichiarazione della lista spesa
lista_spesa = []

#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    
    
    #Controllo della lista se è piena o meno e le seguenti azioni
    if len(lista_spesa) == 0 :
        return "La lista è vuota" 
    else:
        return(lista_spesa)

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)

