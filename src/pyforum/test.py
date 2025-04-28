from utilisateur import Utilisateur # Assurez-vous que le fichier utilisateur.py est dans le même répertoire

# Liste pour stocker les instances des utilisateurs
utilisateurs = []

# Nombre d'utilisateurs à créer
nombre_utilisateurs = int(input("Combien d'utilisateurs voulez-vous créer ? "))

# Boucle pour créer des utilisateurs
for _ in range(nombre_utilisateurs):
    # Demander à l'utilisateur d'entrer un ID et un nom d'utilisateur
    id_utilisateur = int(input("Entrez l'ID de l'utilisateur : "))
    nom_utilisateur = input("Entrez le nom d'utilisateur : ")
    
    # Crée un nouvel utilisateur avec les informations saisies
    utilisateur = Utilisateur(id=id_utilisateur, username=nom_utilisateur)
    utilisateurs.append(utilisateur)  # Ajoute l'utilisateur à la liste

# Affichage des utilisateurs créés
print("\nLes utilisateurs créés sont :")
for utilisateur in utilisateurs:
    print(utilisateur)