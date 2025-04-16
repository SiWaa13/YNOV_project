# Projet de Sécurisation Biométrique d’un Datacenter Universitaire

Bienvenue sur ce dépôt Git lié au dossier d’admission au **Mastère 2 Expert en Cybersécurité**.

Ce projet, réalisé dans le cadre de l’évaluation, vise à renforcer la sécurité physique d’un datacenter universitaire à travers la mise en œuvre d’une **authentification forte biométrique (empreinte digitale)**, intégrée à l’existant (badge, LDAP/AD, VLAN, SIEM ELK).

## Objectifs du projet

- Mettre en place un système d’authentification physique à deux facteurs (empreinte + badge)
- Centraliser les logs d’accès dans un SIEM (ELK)
- Implémenter une surveillance continue des événements critiques
- Assurer la conformité RGPD et les bonnes pratiques cybersécurité
- Réaliser un POC sur un panel de 20 utilisateurs
- Piloter le projet de bout en bout avec documentation et plan d’audit

## Contenu du dépôt

- `biometric_logs.json` : fichier de simulation de logs biométriques (pour ingestion dans ELK)
- `parsing_logs_elk` : scipt pour parser les logs avant ingestion. (Néanmoins, il y a un module déjà intégré avec logtash dans ELK pour parser, ce script est un test car je ne suis pas expert) 
- `docs/` : documentation technique et fonctionnelle (structure du projet, architecture, procédures, etc.)
- `tests/` : campagne de tests et preuves d’exécution
- `README.md` : ce fichier de présentation

## Auteur

Nom : DELAC MAXIME  
Candidat à l'admission parallèle en M2 Expert en Cybersécurité  
Université de Reims Champagne-Ardenne (URCA)

---

Merci pour votre lecture et votre évaluation.
