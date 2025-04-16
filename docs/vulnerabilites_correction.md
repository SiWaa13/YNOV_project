
# Vulnérabilités identifiées et mesures correctives

Ce document présente les vulnérabilités identifiées lors du projet de mise en place d’un contrôle d’accès biométrique, ainsi que les mesures prises pour y remédier.

---

## Vulnérabilités techniques

### 1. Firmware obsolète
- **Description** : Lecteur biométrique livré avec une version vulnérable.
- **Correction** : Mise à jour vers la dernière version signée.
- **Preuve** : Log de mise à jour

### 2. Journaux non chiffrés
- **Description** : Logs écrits en clair sur le serveur biométrique.
- **Correction** : Intégration de Filebeat avec transport TLS vers Logstash.
- **Preuve** : Configuration Filebeat + extrait de log sécurisé.

---

## Vulnérabilités organisationnelles

### 1. Enrôlement sans double validation
- **Description** : Un seul agent pouvait enregistrer un utilisateur.
- **Correction** : Création d’un registre signé par 2 agents à chaque enrôlement.
- **Preuve** : Exemple de registre numérique dans `docs/registre_enrolement.pdf`.

### 2. Absence d’audit périodique
- **Description** : Les droits pouvaient persister même après changement de poste.
- **Correction** : Intégration du périmètre biométrique dans la revue semestrielle des habilitations.
- **Preuve** : Extrait du calendrier d’audit + compte-rendu.
