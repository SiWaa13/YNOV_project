# Plan de tests – Projet Contrôle d'accès biométrique (version synthétique)

Ce document résume un échantillon représentatif des tests réalisés dans le cadre du POC de sécurisation biométrique du datacenter URCA.

| Test n° | Type de test   | Scénario                                                        | Résultat attendu                          | Résultat réel                             | Statut | Preuve                     |
|---------|----------------|------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|--------|----------------------------|
| T01     | Fonctionnel    | Enrôlement d’un utilisateur valide                               | Succès de l'enrôlement + log dans SIEM    | Succès + log `ACCESS_GRANTED`             | OK     | `biometric_logs.json`      |
| T02     | Contournement  | Utilisation d’un badge seul (sans empreinte)                     | Refus d’accès                              | Refus confirmé                             | OK     | `log_test_T02.json`        |
| T03     | RGPD           | Suppression d’un utilisateur dans LDAP                           | Révocation automatique de l'accès          | Accès bloqué + log dans SIEM              | OK     | `script_retrait.py`        |
| T04     | Panne          | Extinction du lecteur biométrique principal                      | Basculement automatique sur le lecteur 2   | OK (lecture redirigée)                     | OK     | `syslog_relais.txt`        |
| T05     | Audit sécurité | Accès en dehors des plages horaires                              | Refus + alerte SIEM                        | Alerte déclenchée + mail RSSI              | OK     | `kibana_alerte.txt` |
