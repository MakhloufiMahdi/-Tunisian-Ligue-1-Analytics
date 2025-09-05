# 📌 Contexte
Ce DAG fait partie de projet Tunisian-Ligue-1-Analytics
Après le chargement des données dans PostgreSQL, Apache Airflow applique des transformations automatiques pour enrichir les tables statistiques.
# 🛠️ Objectif du DAG

Mettre à jour les contributions des joueurs (goals + assists).

Calculer la différence de buts des équipes.

Mettre à jour la différence de buts dans le classement

# 🔄 Dépendances des tâches

transform_players → transform_team_stats → transform_standings

# 📅 Planification

Le DAG est exécuté tous les jours à 01h00 (@daily).
