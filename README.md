# Telegram Message Sender API

API REST légère écrite en Python permettant d’envoyer des notifications Telegram depuis n’importe quelle application, script ou service backend.

Ce projet fournit un service simple et autonome pour envoyer des messages via un ou plusieurs bots Telegram, sans coupler cette logique à une application métier.

---

## Pourquoi ce projet existe

Ce projet est né d’un besoin concret :  
envoyer des notifications automatiques (fin de script, alertes, messages système) vers Telegram de manière simple et fiable.

L’objectif était de :
- isoler la logique de notification
- fournir une API réutilisable et hébergé a distance
- livrer un outil fonctionnel sans complexité inutile

---

## Cas d’usage concrets

- Alertes en cas d’erreur applicative  
- Envoi de messages automatisés depuis un backend  
- Outils internes ou projets personnels  
- Prototypes nécessitant un retour immédiat via Telegram
- Notification de fin de script Python  

---

## Fonctionnalités

- **Multi-bots** : Configurez autant de bots que vous le souhaitez.
- **Bot par défaut** : Un bot est utilisé automatiquement si aucun paramètre n'est spécifié.
- **Interface Web** : Une interface premium (Glassmorphism) pour tester l'envoi de messages manuellement.
- **Sécurisé** : Les tokens et Chat IDs sont stockés dans un fichier JSON ignoré par Git.
- **Documentation API** : Intégration automatique de Swagger/OpenAPI.
- API REST simple et autonome
- Envoi de messages Telegram via bot
- Implémentation en Python
- Configuration par variables d’environnement
- Facilement intégrable dans tout projet backend

---

## Limites volontaires

Ce projet a volontairement été maintenu simple.  
Il ne gère pas :

- l’authentification avancée
- la gestion multi-utilisateurs
- la persistance ou l’historique des messages

Ces choix ont été faits pour rester focalisé sur l’objectif principal :  
**l’envoi fiable et rapide de messages Telegram.**

---

## Améliorations possibles

- Authentification par token
- Support multi-chats ou multi-bots
- Templates de messages
- Logs et monitoring
- Conteneurisation Docker

---

## Prérequis

- Python 3.8+
- Un bot Telegram (créé via BotFather)
- Un token Telegram valide
- L’identifiant du chat Telegram cible

---

## Structure du Projet

```text
TelegramApiSender/
├── app/
│   ├── main.py          # Point d'entrée & Routes
│   ├── config.py        # Logique de configuration
│   ├── services/
│   │   └── telegram.py  # Logique API Telegram
│   ├── schemas/
│   │   └── message.py   # Modèles Pydantic
│   └── static/
│       └── index.html   # Interface Web
├── config/
│   ├── bots.json        # Config active (Tokens & IDs)
│   └── bots.json.example
├── tests/               # Tests unitaires
└── .env                 # Paramètres généraux
```

## Installation

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/yodjii/TelegramMessageSenderAPI.git
   cd TelegramMessageSenderAPI
   ```
2. Créez un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Configurez vos bots :
   - Copiez `config/bots.json.example` vers `config/bots.json`.
   - Modifiez `config/bots.json` avec vos propres tokens et Chat IDs.

## Déploiement (AlwaysData)

Pour un hébergement sur AlwaysData, il est recommandé d'utiliser le type de site **"Programme utilisateur"** :

1. **Répertoire de travail** : `/home/votre-user/votre-projet/`
2. **Commande** :
   ```bash
   env ROOT_PATH=/TelegramApiSender PYTHONPATH=/home/votre-user/votre-projet/.local/lib/python3.13/site-packages python3.13 -m uvicorn app.main:app --host $IP --port $PORT
   ```
3. Assurez-vous d'avoir configuré le `ROOT_PATH` si vous utilisez un préfixe d'URL.

## Utilisation

### Lancer le serveur
```bash
uvicorn app.main:app --reload
```
L'interface est accessible sur `http://localhost:8000`.

### Documentation API
Accédez à `http://localhost:8000/docs` pour la documentation interactive Swagger.

### Exemple d'appel en Python

Voici comment appeler votre API depuis un autre script Python :

```python
import requests

url = "http://localhost:8000/send"
data = {
    "message": "Hello depuis Python !",
    "bot_name": "bot1"  # Optionnel, utilise le bot par défaut si omit
}

response = requests.post(url, json=data)
print(response.json())
```

## Tests

Pour lancer les tests et vérifier la couverture :
```bash
pytest
```

## Licence
MIT
