# Cahier des charges – Tableau de bord GitLab intelligent

## 1. Présentation du projet

Développer une application permettant de centraliser et de visualiser les informations essentielles d'un dépôt GitLab au sein d'un tableau de bord moderne et intuitif.

L'objectif est de fournir aux développeurs et aux responsables techniques une vue d'ensemble de l'état d'un projet sans avoir à naviguer entre les différentes pages de GitLab.

À terme, le projet pourra être étendu sous la forme d'une extension Visual Studio Code afin d'offrir les mêmes informations directement dans l'environnement de développement.

---

# 2. Objectifs

L'application devra permettre de :

* Centraliser les informations importantes d'un dépôt GitLab.
* Faciliter le suivi quotidien d'un projet.
* Réduire le temps passé à rechercher des informations dispersées.
* Offrir une interface claire, moderne et ergonomique.
* Servir de base à des fonctionnalités d'analyse ou d'assistance via des agents IA.

---

# 3. Fonctionnalités attendues

Le tableau de bord devra permettre d'afficher notamment :

### Dépôt

* Nom du projet
* Description
* Branche principale
* Dernier commit
* Dernière activité

### Merge Requests

* Liste des Merge Requests ouvertes
* Auteur
* État
* Nombre de commentaires
* Validation (approbations)
* Date de création

### Issues

* Liste des issues ouvertes
* Priorité
* Labels
* Assignation
* Échéance éventuelle

### Pipelines CI/CD

* Derniers pipelines
* Statut (Succès, Échec, En cours...)
* Durée
* Branche concernée
* Accès aux logs

### Sécurité

* Variables protégées
* Secrets configurés
* Alertes de sécurité disponibles
* État des scans (si activés)

### Statistiques

* Nombre de commits récents
* Contributeurs actifs
* Activité sur les derniers jours
* Répartition des Merge Requests et Issues

---

# 4. Évolutions envisagées

Le projet devra être conçu de manière modulaire afin de permettre facilement l'ajout de nouvelles fonctionnalités, notamment :

* Extension Visual Studio Code
* Notifications en temps réel
* Assistant IA pour résumer l'état du projet
* Génération automatique de rapports
* Recommandations sur les Merge Requests
* Détection d'anomalies dans les pipelines
* Suivi multi-projets GitLab

---

# 5. Contraintes techniques

L'application devra respecter les technologies suivantes :

* Backend : Python
* Framework API : FastAPI
* Base de données : SQLite
* Conteneurisation : Docker
* Communication avec GitLab via son API REST
* Architecture modulaire facilitant les évolutions futures

---

# 6. Contraintes fonctionnelles

L'application devra :

* proposer une interface moderne et responsive ;
* être simple à prendre en main ;
* afficher les informations de manière synthétique ;
* permettre une navigation fluide entre les différentes sections ;
* offrir des temps de réponse rapides ;
* gérer les erreurs de connexion à GitLab de manière explicite.

---

# 7. Architecture générale

Le projet sera composé de plusieurs composants :

* **Backend FastAPI** chargé de communiquer avec l'API GitLab.
* **Base SQLite** permettant de stocker les données mises en cache.
* **Interface web** affichant le tableau de bord.
* **Conteneur Docker** pour simplifier le déploiement.
* **Agent IA (OpenCode)** chargé d'orchestrer la récupération, l'analyse et la présentation des informations.

---

# 8. Critères de réussite

Le projet sera considéré comme terminé lorsque :

* les informations principales d'un dépôt GitLab sont récupérées automatiquement ;
* le tableau de bord présente clairement l'état du projet ;
* les Merge Requests, Issues et Pipelines sont consultables ;
* l'application est exécutable via Docker ;
* l'architecture permet d'ajouter facilement de nouvelles fonctionnalités.

---

# 9. Perspectives

À moyen terme, cette application pourra évoluer vers une plateforme d'assistance au développement reposant sur des agents IA capables d'analyser automatiquement un dépôt GitLab, de détecter les points d'attention et de fournir des recommandations aux équipes de développement.
