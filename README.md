# TelegramApiSender

Une API FastAPI moderne pour envoyer des messages via Telegram en utilisant plusieurs bots préconfigurés.

## Fonctionnalités

- **Multi-bots** : Configurez autant de bots que vous le souhaitez.
- **Bot par défaut** : Un bot est utilisé automatiquement si aucun paramètre n'est spécifié.
- **Interface Web** : Une interface premium (Glassmorphism) pour tester l'envoi de messages manuellement.
- **Sécurisé** : Les tokens et Chat IDs sont stockés dans un fichier JSON ignoré par Git.
- **Documentation API** : Intégration automatique de Swagger/OpenAPI.

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

1. Clonez le dépôt.
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
