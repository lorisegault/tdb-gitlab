# Planification des sprints

## Sprint 1 — Fondations du projet (US-001 à US-003)
**Objectif** : Mettre en place l'architecture du projet, le squelette backend et frontend, la base de données et la conteneurisation Docker.

### Tâches
- [ ] Initialiser le dépôt Git avec la structure de dossiers
- [ ] Créer le squelette FastAPI (main.py, config.py, database.py, models.py, schemas.py)
- [ ] Créer les routers vides (pipeline, secrets, branches, issues, merge_requests)
- [ ] Créer le squelette frontend (index.html, app.js, composants vides)
- [ ] Créer les fichiers Docker (Dockerfile multi-stage, docker-compose.yml, nginx.conf)
- [ ] Créer le backlog et la planification des sprints
- [ ] Valider avec `python -m pytest projet/backend/tests/ -v` (tests vides OK)

**Livrables** : Dépôt Git initialisé, squelette backend/frontend/Docker, backlog produit.

---

## Sprint 2 — Intégration GitLab (US-004 à US-005)
**Objectif** : Connecter l'application à l'API GitLab et mettre en place le cache des données.

### Tâches
- [ ] Implémenter le client GitLab (requêtes API avec httpx)
- [ ] Créer les endpoints de récupération des infos du dépôt
- [ ] Mettre en place le cache SQLite via SQLAlchemy
- [ ] Ajouter les modèles de données manquants (MergeRequest, Issue, Pipeline, Secret)
- [ ] Écrire les tests d'intégration

---

## Sprint 3 — API backend (US-006 à US-009)
**Objectif** : Développer les endpoints API pour toutes les fonctionnalités.

### Tâches
- [ ] Implémenter l'endpoint GET /merge-requests
- [ ] Implémenter l'endpoint GET /issues
- [ ] Implémenter l'endpoint GET /pipelines
- [ ] Implémenter l'endpoint GET /secrets
- [ ] Ajouter les schémas Pydantic pour chaque ressource
- [ ] Écrire les tests unitaires et d'intégration

---

## Sprint 4 — Interface tableau de bord (US-010 à US-014)
**Objectif** : Développer l'interface utilisateur complète.

### Tâches
- [ ] Développer la page d'accueil avec les infos du dépôt
- [ ] Développer la page pipelines avec statut et durée
- [ ] Développer la page secrets
- [ ] Développer la navigation SPA (showSection)
- [ ] Implémenter le polling 3s avec apiFetch
- [ ] Ajouter les statistiques (commits, contributeurs, activité)
- [ ] Appliquer le thème dark (bg-gray-900, text-gray-100)

---

## Sprint 5 — Docker, CI/CD & finalisation (US-015 à US-017)
**Objectif** : Finaliser le projet avec CI/CD, gestion d'erreurs et polish.

### Tâches
- [ ] Finaliser Docker Compose (volumes, variables d'env)
- [ ] Créer la pipeline GitHub Actions (lint, test, build)
- [ ] Ajouter la gestion d'erreurs de connexion à GitLab
- [ ] Tests de non-régression sur l'ensemble des tests
- [ ] Documentation et README
- [ ] Tag de release v1.0.0
