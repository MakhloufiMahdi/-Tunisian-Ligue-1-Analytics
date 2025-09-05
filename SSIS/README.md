Ce projet vise à construire un pipeline ETL  pour intégrer et transformer des données du ligue1  provenant de 8 fichiers CSV. 
Le processus ETL est réalisé avec SQL Server Integration Services (SSIS) et se compose des étapes suivantes :
Extraction : Lecture des fichiers CSV
Transformation : Conversion des types de données et nettoyage.
Chargement : Insertion dans des tables PostgreSQL via ODBC.
Les données concernent les performances des joueurs et des équipes tunisiennes, et sont chargées dans une base de données PostgreSQL pour analyse et visualisation.

