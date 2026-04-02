# 🚀 TP RAG – Retrieval Augmented Generation

Ce projet implémente un système de **RAG (Retrieval Augmented Generation)** avec une interface web interactive développée avec **Streamlit**.

L’application permet de charger un document PDF et de poser des questions en langage naturel. Les réponses sont générées automatiquement à partir du contenu du document grâce à une combinaison de recherche vectorielle et de modèles de langage.

---

## 🧠 Fonctionnalités

- 📄 Upload de fichiers PDF
- 🔍 Extraction et découpage du texte
- 🧩 Création d’embeddings avec OpenAI
- 🗄️ Stockage vectoriel avec FAISS
- 🤖 Chatbot intelligent basé sur RAG
- 💬 Réponses générées à partir du document

---

## 🛠️ Technologies utilisées

- **Python**
- **Streamlit**
- **LangChain**
- **OpenAI API**
- **FAISS**
- **PyPDF / PyMuPDF**
- **python-dotenv**

---

## 📸 Interface

![Interface du projet](assets/screenshot.png)

---

## 📂 Structure du projet

```

rag_tp/
│── assets/
│   └── screenshot.png
│
│── data/
│
│── notebooks/
│   └── RAGV2.ipynb
│
│── src/
│   ├── **init**.py
│   ├── config.py
│   ├── multimodal.py
│   ├── rag.py
│   └── utils.py
│
│── .env
│── pyproject.toml
│── streamlit_app.py
│── README.md

````

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-username/rag_tp.git
cd rag_tp
````

---

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

#### Activation (Windows PowerShell)

```powershell
.venv\Scripts\activate
```

---

### 3. Installer les dépendances

```bash
pip install streamlit openai langchain langchain-openai langchain-community langchain-text-splitters faiss-cpu python-dotenv pypdf pymupdf pillow
```

---

### 4. Configurer la clé API OpenAI

Créer un fichier `.env` à la racine du projet :

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Lancer l’application

```bash
python -m streamlit run streamlit_app.py
```

---

## 🧪 Exemple d’utilisation

1. Lancer l’application
2. Importer un fichier PDF
3. Poser une question, par exemple :

```text
Quels sont les faits marquants de l'exercice ?
```

4. Obtenir une réponse générée automatiquement à partir du document

---

## 📓 Notebook

Le fichier `RAGV2.ipynb` permet de tester séparément :

* le chargement des documents
* le découpage en chunks
* la vectorisation
* le retriever
* la génération de réponse

---

## 📌 Principe du RAG

Le système fonctionne en trois étapes :

1. **Retrieval** → récupération des passages pertinents
2. **Augmentation** → ajout du contexte
3. **Génération** → production de la réponse avec le modèle

---


## 👨‍💻 Auteur

**Khalid Naitali**



