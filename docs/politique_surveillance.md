# Politique de contrôle et de surveillance continue
## Projet : Contrôle d’accès biométrique au datacenter – Université de Reims Champagne-Ardenne

### 1. Objectif

Cette politique vise à garantir une surveillance permanente et cohérente des accès physiques au datacenter via le système biométrique mis en place. Elle définit les modalités de collecte, d’analyse et de réaction face aux événements de sécurité.

---

### 2. Périmètre de surveillance

Les éléments suivants font l’objet d’une surveillance continue :
- Tentatives d’accès refusées (empreinte invalide, badge seul)
- Accès autorisés avec horodatage et identification LDAP
- Enrôlements, désactivations et suppressions biométriques
- Accès en dehors des plages horaires définies
- Anomalies techniques : pannes, reboot, déconnexion réseau
- Modifications de configuration ou changement d’IP d’un lecteur

---

### 3. Collecte des données

Les journaux d’événements générés par le serveur biométrique sont :
- Collectés localement (logs horodatés en JSON)
- Transmis au SIEM ELK (via Filebeat avec TLS)
- Indexés pour visualisation dans Kibana

Chaque événement est conservé 30 jours glissants à chaud, sauf incidents critiques (90 jours), conformément aux politiques internes et 60 jours à froid.

---

### 4. Détection et alertes

Des règles de détection ont été définies dans le SIEM :
- Plus de 3 échecs d’accès consécutifs → alerte “Suspicion d’usurpation”
- Accès hors horaires autorisés → alerte “Anomalie de créneau”
- Modification non autorisée de configuration → alerte “Altération matérielle”

Les alertes déclenchent une notification automatique au RSSI via e-mail ou webhook interne. Chaque alerte est tracée et doit faire l’objet d’un ticket dans l’outil de gestion des incidents.

---

### 5. Révision et audit

La politique de surveillance est revue tous les 6 mois lors de la revue de sécurité du SI. Les règles de détection sont mises à jour en fonction des retours du terrain et des audits internes. Chaque modification est documentée dans un changelog spécifique.

---

**Responsables** : RSSI  
**Date de mise en application** : 1er mai 2025
