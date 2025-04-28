#début du programme
#import des modules
import json
import csv

#import des classes
from pyforum.utilisateur import Utilisateur
from pyforum.forum import Forum
from pyforum.publication import publication




class BD:
    """Cette classe permet de gérer la base de données du forum"""

    def __init__(self):
        """Constructeur de la classe permettant de gérer les différents attributs de la classe base de données"""
        self.utilisateurs: list[Utilisateur] = []
        self.forums: list[Forum] = []
        self.publications: list[publication] = []
        self.commentaires = []
        self.utilisateurs_forums = {}
        print("Base de données initialisée.")

    def creer_utilisateur(self, username:str, adresseCourriel: str, motDePasse: str, listeForums: list) -> Utilisateur:
        """Méthode permettant de créer un objet utilisateur, générer son identifiant unique et retourner l'objet créé"""
        #                       ^^^^^^^^^^^^^^
        #            # TODO:    Vous devez ajouter les autres paramètres requis

        # Vérifier si l'utilisateur existe déjà
        if username in [u.username for u in self.utilisateurs]:
            print(f"[Simulé] L'utilisateur {username} existe déjà.")
            

        # Créer un nouvel identifiant pour l'utilisateur
        new_id = max([u.id for u in self.utilisateurs], default=0) + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(new_id, username, adresseCourriel, motDePasse, listeForums)
        self.utilisateurs.append(u)
        #print(f"[Simulé] Sauvegarde du nouveau utilisateur: {u}")

        # Retourner l'utilisateur créé
        return u

    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u
    
    def sauvegardeDutilisateurs(self):
        for u in self.utilisateurs:
            with open('src/pyforum/data/utilisateurs.json', 'r', encoding='utf-8') as fichier:
                data = json.load(fichier)
            
            
            data.append(u.to_dict())
            with open('src/pyforum/data/utilisateurs.json', 'w', encoding='utf-8') as fichier:
                json.dump(data, fichier, ensure_ascii = False, indent = 4)

   

    def creer_forum(self, nom: str, id: str, listePublications: list, description: str) -> Forum:
        #                ^^^^^^
        #                Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer un forum
        if nom in [f.nom for f in self.forums]:
            print(f"[Simulé] Le forum {nom} existe déjà.")
            return
 
    # Créer un nouvel identifiant pour l'utilisateur
        new_id = max([f.id for f in self.forums], default=0) + 1

    # Instancier un nouvel utilisateur et l'ajouter à la liste
        f = Forum(new_id, nom, listePublications, description)
        self.forums.append(f)
        print(f"[Simulé] Sauvegarde du nouveau forum: {f}")

        # Retourner le forum créé
        return f
    
    
    def sauvegardeDeForums(self):
        with open('src/pyforum/utilisateurs.json', 'r', encoding='utf-8') as fichier:
            data = json.load(fichier)
        
        
        nouveauForum = self.creer_forum(username="toto", adresseCourriel="toto@gmail.com", motDePasse="loltruc", listeForums=["animeau","finances","voitures"])
        data.append(nouveauForum.to_dict())
        with open('src/pyforum/utilisateurs.json', 'w', encoding='utf-8') as fichier:
            json.dump(data, fichier, ensure_ascii = False, indent = 4)



    def creer_publication(self, publication):
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer une publication
        pass

    def creer_commentaire(self, commentaire):
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer un commentaire
        pass

    def obtenir_forum_par_nom(self, nom_forum):
        # TODO: Implanter la logique pour chercher un forum à partir de son nom
        for f in self.forums:
            if f.nom == nom_forum:
                return f

    def obtenir_publication_par_titre(self, titre_publication):
        # TODO: Implanter la logique pour chercher une publication à partir de son titre
        pass

    def mettre_a_jour_forum(self, forum):
        #                         ^^^^^^
        #                         Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour mettre à jour le forum et retourner le forum mis à jour
        pass
