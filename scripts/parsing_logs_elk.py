import json                      
import datetime                 
import random                   

# Liste d'événements biométriques simulés sachant que les adresses IP sont fictives, je ne vais pas dévoiler nos plages d'adresses privées
events = [
    {"event": "ACCESS_GRANTED", "user": "jdoe", "method": "fingerprint", "ip": "192.168.10.21"},
    {"event": "ACCESS_DENIED", "user": "mdupont", "method": "fingerprint", "ip": "192.168.10.45"},
    {"event": "ENROLLMENT", "user": "arobert", "method": "fingerprint", "ip": "192.168.10.11"},
    {"event": "ERROR", "user": "system", "method": "reader_failure", "ip": "192.168.10.10"},
    {"event": "ACCESS_GRANTED", "user": "nmartin", "method": "fingerprint", "ip": "192.168.10.32"},
]

# Fonction qui génère une liste de logs formatés JSON
def generate_biometric_logs(log_count=20):
    log_entries = []  # Liste qui contiendra tous les logs générés
    for _ in range(log_count):
        event = random.choice(events)  # Choisit un événement au hasard
        timestamp = datetime.datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "event_type": event["event"],
            "user": event["user"],
            "auth_method": event["method"],
            "source_ip": event["ip"],
            "log_level": "INFO" if event["event"] != "ERROR" else "ERROR"
        }
        log_entries.append(log_entry)  # Ajoute l'événement à la liste
    return log_entries

# Génération des logs (par défaut 20)
log_data = generate_biometric_logs()

# Sauvegarde dans un fichier JSON local (à exporter ensuite vers le SIEM)
log_file_path = "biometric_logs.json"
with open(log_file_path, "w") as f:
    json.dump(log_data, f, indent=4)

print(f"{len(log_data)} logs biométriques générés dans le fichier : {log_file_path}")
