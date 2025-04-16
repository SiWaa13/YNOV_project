# Rapport d’audit – Contrôle d’accès biométrique au datacenter URCA

**Date** : 25 septembre 2025  
**Équipe audit** : RSSI, DPO, Chef de projet DN (moi)

## Périmètre audité

- Accès biométriques (empreinte digitale)
- Interconnexion avec LDAP, badge Salto, SIEM
- Procédures d’enrôlement / révocation
- Sensibilisation RGPD
- Conformité technique et réglementaire

## Méthodologie

- Revue documentaire (spécifications, scripts, registre, politique)
- Tests sur environ 20 utilisateurs dans le cadre du POC
- Simulations d’incidents (tentatives d’accès non autorisées, pannes réseau)
- Vérification de l’intégration dans le SIEM (log parsing, alertes)

## Résultats clés

| Éléments audités                    | Statut       | Commentaire |
|------------------------------------|--------------|-------------|
| Authentification biométrique       | Conforme     | Accès réussi et traçable |
| Synchronisation LDAP               | Conforme     | Script de désactivation automatique fonctionnel |
| Sécurité de la console admin       | Conforme     | Accès restreint + MFA |
| Chiffrement des logs               | Conforme     | Filebeat + TLS en place |
| Politique de sensibilisation       | Conforme     | Formation + guide fournis |
| Conformité RGPD (finalité, retrait)| Conforme avec réserve | Prévoir double confirmation lors du retrait |

## Recommandations

- Vérifier tous les 6 mois la validité des habilitations biométriques
- Étudier l’extension du dispositif à d’autres zones sensibles
- Réaliser un audit Purple Team annuel incluant la biométrie

## Conclusion

Le dispositif biométrique mis en place répond aux objectifs de sécurité physique, de traçabilité et de conformité. Il est jugé **conforme et opérationnel**, sous réserve de suivi régulier et d’évolutivité encadrée.
