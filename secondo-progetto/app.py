from flask import Flask, request, redirect, url_for, render_template

#request per fare delle richieste sia GET che POST da un client
#redirect per reindirazzare l'utente a un altra pagina o link
#url_for per la creazione di un url dinamico e non statico e per aver meno errori


#Dichiarazione della lista spesa
lista_spesa = []

#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    return render_template('index.html', lista_spesa=lista_spesa)
    
    #Controllo della lista se è piena o meno e le seguenti azioni
    if len(lista_spesa) == 0 :
        return "La lista è vuota" 
    else:
        return(lista_spesa)

@app.route('/aggiungi', methods=['POST'])
#Creazione della funzione per l'aggiunta di un elemento alla lista
def aggiungi():
    #Si estrae la variabile dalla pagina
    elemento = request.form['elemento']
    #Si fa l'if per aggiungerlo
    if elemento:
        lista_spesa.append(elemento)
    #Reindirizzamento alla pagina principale
    return redirect(url_for('home'))

#Route l'eliminazione
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)

