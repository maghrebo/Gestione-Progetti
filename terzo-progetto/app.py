from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, ListaSpesa

app = Flask(__name__)

# Configurazione del database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializzazione del database con Flask
db.init_app(app)

# Creazione delle tabelle nel database all'avvio dell'applicazione
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # Recupera tutti gli elementi della lista spesa dal database
    lista_spesa = ListaSpesa.query.all()
    return render_template('index.html', lista_spesa=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    # Funzione per aggiungere un nuovo elemento alla lista spesa
    elemento = request.form['elemento']  # Recupera l'elemento dal modulo form dell'html
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento)  # Crea un nuovo oggetto ListaSpesa
        db.session.add(nuovo_elemento)  # Aggiunge l'elemento alla sessione del database
        db.session.commit()  # Salva i cambiamenti nel database
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    # Funzione che rimuove un elemento specifico dalla lista spesa utilizzando l'id ricavato dalla route
    elemento = ListaSpesa.query.get_or_404(indice)  # Trova l'elemento tramite ID o restituisce un errore 404
    db.session.delete(elemento)  # Rimuove l'elemento dalla sessione del database
    db.session.commit()  # Salva i cambiamenti nel database
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    # Funzione che elimina tutti gli elementi dalla lista spesa
    ListaSpesa.query.delete()  # Cancella tutti i dati della tabella ListaSpesa
    db.session.commit()  # Salva i cambiamenti nel database
    return redirect(url_for('home'))

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
