# 🎓 Générateur de Page de Garde PFE

Une application web interactive développée en Python pour générer automatiquement des pages de garde de Projet de Fin d'Études (PFE) aux standards académiques, avec une touche esthétique "Renaissance".

> *"Les détails font la perfection, et la perfection n'est pas un détail." — Léonard de Vinci*

## 📋 Présentation

Ce projet vise à simplifier la vie des étudiants ingénieurs en leur offrant un outil capable de créer une page de garde parfaite en quelques secondes. Fini les galères de mise en page sur Word !

**Fonctionnalités principales :**
* 📄 **Génération PDF instantanée** : Respect des normes académiques (Police Times, centrage, hiérarchie).
* 🎨 **Personnalisation** : Choix de la couleur dominante via des commandes textuelles (ex: "Rouge", "Bleu").
* 🖼️ **Intégration de Logo** : Ajout facile du logo de l'établissement.
* 🔗 **QR Code Intelligent** : Génération automatique d'un QR Code vers le lien du projet (GitHub/Portfolio).
* 🚀 **Mode Gratuit** : Fonctionne entièrement en local sans besoin de clé API payante.

## 🛠️ Prérequis

Avant de lancer l'application, assurez-vous d'avoir **Python** installé sur votre machine.

## 📦 Installation

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/ismd2005-lab/PFE-Generator.git](https://github.com/VOTRE_NOM_UTILISATEUR/NOM_DU_PROJET.git)
    cd NOM_DU_PROJET
    ```

2.  **Installer les dépendances :**
    Exécutez la commande suivante pour installer les bibliothèques nécessaires (`streamlit`, `fpdf`, `qrcode`) :
    ```bash
    pip install -r requirements.txt
    ```
    *(Si vous n'avez pas de fichier requirements.txt, lancez : `pip install streamlit fpdf qrcode`)*

## 🚀 Utilisation

Pour lancer l'application, ouvrez votre terminal dans le dossier du projet et tapez :

```bash
streamlit run app.py

L'application s'ouvrira automatiquement dans votre navigateur par défaut (généralement à l'adresse http://localhost:8501).
⚙️ Structure du Projet

    app.py : Le code source principal de l'application.

    requirements.txt : Liste des librairies Python requises.

    README.md : Documentation du projet.

👤 Auteur

Ismail DEMNATI

    Élève Ingénieur en Génie Informatique & Intelligence Artificielle.

    École Nationale des Sciences Appliquées (ENSA).
