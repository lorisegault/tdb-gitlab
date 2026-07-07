# Backlog produit

## User Stories

### Sprint 1 — Fondations du projet
- US-001 : En tant que développeur, je veux un projet structuré (backend FastAPI + frontend React statique + Docker) pour démarrer le développement.
- US-002 : En tant que développeur, je veux une base de données SQLite initialisée avec SQLAlchemy pour stocker les données.
- US-003 : En tant que développeur, je veux un point de santé API (/health) pour vérifier que le service tourne.

### Sprint 2 — Intégration GitLab
- US-004 : En tant qu'utilisateur, je veux que l'application se connecte à l'API GitLab pour récupérer les données du dépôt.
- US-005 : En tant qu'utilisateur, je veux que les informations du dépôt (nom, description, branche, dernier commit) soient stockées en cache.

### Sprint 3 — API backend
- US-006 : En tant qu'utilisateur, je veux consulter la liste des Merge Requests ouvertes via l'API.
- US-007 : En tant qu'utilisateur, je veux consulter la liste des Issues ouvertes via l'API.
- US-008 : En tant qu'utilisateur, je veux consulter l'état des pipelines CI/CD via l'API.
- US-009 : En tant qu'utilisateur, je veux consulter les secrets et variables configurés via l'API.

### Sprint 4 — Interface tableau de bord
- US-010 : En tant qu'utilisateur, je veux une page d'accueil avec les infos clés du dépôt.
- US-011 : En tant qu'utilisateur, je veux une page dédiée aux pipelines avec leur statut.
- US-012 : En tant qu'utilisateur, je veux une page dédiée aux secrets.
- US-013 : En tant qu'utilisateur, je veux naviguer entre les sections sans rechargement de page.
- US-014 : En tant qu'utilisateur, je veux que les données soient rafraîchies automatiquement toutes les 3 secondes.

### Sprint 5 — Docker, CI/CD & finalisation
- US-015 : En tant qu'utilisateur, je veux pouvoir lancer l'application avec Docker Compose.
- US-016 : En tant que développeur, je veux une pipeline CI GitHub Actions pour valider le code.
- US-017 : En tant qu'utilisateur, je veux une gestion explicite des erreurs de connexion à GitLab.
