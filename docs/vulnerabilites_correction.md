
# 📄 Vulnérabilités identifiées et mesures correctives

Ce document présente les vulnérabilités identifiées lors du projet de mise en place d’un contrôle d’accès biométrique à l’Université de Reims Champagne-Ardenne, ainsi que les mesures prises pour y remédier.

---

## 🔧 Vulnérabilités techniques

### 1. Firmware obsolète
- **Description** : Lecteur biométrique livré avec une version vulnérable.
- **Correction** : Mise à jour vers la dernière version signée.
- **Preuve** : Log de mise à jour et empreinte SHA256 du firmware installé.

### 2. Journaux non chiffrés
- **Description** : Logs écrits en clair sur le serveur biométrique.
- **Correction** : Intégration de Filebeat avec transport TLS vers Logstash.
- **Preuve** : Configuration Filebeat + extrait de log sécurisé.

### 3. Console d’administration non sécurisée
- **Description** : Interface sans MFA ni restriction d’accès IP.
- **Correction** : Ajout d’une authentification forte (TOTP) + filtrage IP par firewall.
- **Preuve** : Capture de la nouvelle interface + règles du pare-feu local.

---

## 🧭 Vulnérabilités organisationnelles

### 1. Enrôlement sans double validation
- **Description** : Un seul agent pouvait enregistrer un utilisateur.
- **Correction** : Création d’un registre signé par 2 agents à chaque enrôlement.
- **Preuve** : Exemple de registre numérique dans `docs/registre_enrolement.pdf`.

### 2. Révocation d’accès non automatisée
- **Description** : Dépendance manuelle à la désactivation LDAP.
- **Correction** : Script cron quotidien désactivant automatiquement les comptes biométriques désactivés côté LDAP.
- **Preuve** : Script `desactivation_auto.py` dans `scripts/`.

### 3. Absence d’audit périodique
- **Description** : Les droits pouvaient persister indûment.
- **Correction** : Intégration du périmètre biométrique dans la revue semestrielle des habilitations.
- **Preuve** : Extrait du calendrier d’audit + compte-rendu.

---

Toutes les corrections ont été validées dans le cadre du POC et documentées dans le rapport d’audit final.
