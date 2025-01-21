from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Utenti
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Configurazione del database SQLite
app.config['SECRET_KEY'] = 'mysecretkey'  # Chiave segreta per la sessione
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utenti.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializzazione del database con Flask
db.init_app(app)

# Inclusione di Bcrypt con l'applicazione
bcrypt = Bcrypt(app)

# Creazione delle tabelle nel database all'avvio dell'applicazione
with app.app_context():
    db.create_all()

# Pagina di home predefinita
@app.route('/')
def home():
    return "Benvenuto nell'app di gestione utenti!"

# Registrazione dell'utente
@app.route('/registrazione', methods=['GET', 'POST'])
def registrazione():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifica che l'utente non esista già
        existing_user = Utenti.query.filter_by(username=username).first()
        if existing_user:
            flash('Nome utente già esistente!', 'danger')
            return redirect(url_for('registrazione'))
        
        # Crea un hash sicuro per la password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Crea l'utente e aggiungilo al database
        nuovo_utente = Utenti(username=username, hashed_password=hashed_password)
        db.session.add(nuovo_utente)
        db.session.commit()

        flash('Registrazione avvenuta con successo!', 'success')
        return redirect(url_for(''))

    return render_template('registrazione.html')



# Login dell'utente
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Trova l'utente nel database
        utente = Utenti.query.filter_by(username=username).first()
        if utente and bcrypt.check_password_hash(utente.password, password):
            flash('Login riuscito!', 'success')  # Usa 'flash' per il messaggio di successo
            return redirect(url_for('/'))
        else:
            flash('Credenziali non valide', 'danger')  # Usa 'flash' per il messaggio di errore
            return redirect(url_for('/'))

    return render_template('login.html')

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
