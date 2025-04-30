#début du programme
#import des modules
import json
import csv

#import des classes
from pyforum.utilisateur import Utilisateur
from pyforum.forum import Forum


class BD:
    """Cette classe permet de gérer la base de données du forum"""

    def __init__(self):
        """Constructeur de la classe permettant de gérer les différents attributs de la classe base de données"""
        self.utilisateurs: list[Utilisateur] = []
        self.forums: list[Forum] = []
        self.publications = []
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
        u = Utilisateur(new_id, username, adresseCourriel, motDePasse, listeForums = [])
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde du nouveau utilisateur: {u}")

        # Retourner l'utilisateur créé
        return u

    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u
    
    def sauvegardeDutilisateurs(self):
        with open('src/pyforum/utilisateurs.json', 'r', encoding='utf-8') as fichier:
            data = json.load(fichier)
        
        
        nouvelutilisateur = self.creer_utilisateur(username="toto", adresseCourriel="toto@gmail.com", motDePasse="loltruc", listeForums=["animeau","finances","voitures"])
        data.append(nouvelutilisateur.to_dict())
        with open('src/pyforum/utilisateurs.json', 'w', encoding='utf-8') as fichier:
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



    # Instancier un nouveau forum et l'ajouter à la liste
        f = Forum(new_id, nom, listePublications, description)
        self.forums.append(f)
        print(f"[Simulé] Sauvegarde du nouveau forum: {f}")

        # Retourner le forum créé
        return f
    
    
    def sauvegardeDeForums(self):
        for f in self.forums:
            with open('src/pyforum/data/forums.json', 'r', encoding='utf-8') as fichier:
                data = json.load(fichier)
            # Vérifier que data est une liste
            if not isinstance(data, list):
                data = []
            
        data.append(f.to_dict())
        with open('src/pyforum/data/forums.json', 'w', encoding='utf-8') as fichier:
            json.dump(data, fichier, ensure_ascii = False, indent = 4)




    def creer_publication(self, titre: str, contenu: str, listeCommentaires: list, date_creation=datetime.now()):
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer une publication
        if titre in [p.titre for p in self.publications]:
            print(f"[Simulé] La publication {titre} est déjà publiée.")
            return
        
        while True:
            commentaire = input("Entrez un commentaire (ou appuyez sur Entrée pour terminer) :")
            if commentaire == "":
                break
            listeCommentaires.append(commentaire)
            

        #créer un nouvel identifiant pour les publications
        new_id = max([p.identifiant for p in self.publications], default=0) + 1
        new_author_id = max([p.identifiantAuteur for p in self.publications], default=0) + 1
        new_forum_id = max([p.identifiantForum for p in self.publications], default=0) + 1

        #ajout de la date de création
        date_creation= datetime.now()
        # Instancier une nouvelle publication et l'ajouter à la liste
        p = publication(titre, new_id, contenu, date_creation.strftime("%Y-%m-%d %H:%M:%S"), new_author_id, new_forum_id, listeCommentaires)
        self.publications.append(p)
        print(f"[Simulé] Sauvegarde de la nouvelle publication: {p}")

        # Retourner la nouvelle publication créée
        return p
    
    def sauvegardeDePublications(self):
        for p in self.publications:
            with open('src/pyforum/data/publications.json', 'r', encoding='utf-8') as fichier:
                data = json.load(fichier)
            
            if not isinstance(data, list):
                data = []

            data.append(p.to_dict())
            with open('src/pyforum/data/publications.json', 'w', encoding='utf-8') as fichier:
                json.dump(data, fichier, ensure_ascii = False, indent = 4)
        
    def creer_commentaire(self, id: str, contenu: str):
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer un commentaire
        if id in [c.id for c in self.commentaires]:
            print(f"[Simulé] Le commentaire {contenu} existe déjà.")

        #créer un nouvel identifiant pour les commentaires
        new_id = max([c.id for c in self.commentaires], default=0) + 1 
        new_author_id = max([c.auteur_id for c in self.commentaires], default=0) + 1
        new_post_id = max([c.publication_id for c in self.commentaires], default=0) + 1

        c = Commentaire(new_id, new_author_id, contenu, new_post_id)
        self.commentaires.append(c)
        print(f"[Simulé] Sauvegarde du nouveau commentaire: {c}")

        return c
    
    def sauvegardeDesCommentaires(self):

        champs = ["id", "id auteur", "contenu", "id publications"]
        données = [c.to_dict() for c in self.commentaires]

        identifiants_connus = [str(c["id"]) for c in données]

        with open('src/pyforum/data/commentairesInitiales.csv', 'r', newline='', encoding='utf-8') as fichierInitiale:
            commentairesInitiaux = (csv.DictReader(fichierInitiale))
            for commentaires in commentairesInitiaux:
                if str(commentaires["id"]) not in identifiants_connus:
                    données.append(commentaires)
            
        with open('src/pyforum/data/commentaires.csv', 'w', newline='', encoding='utf-8') as fichier:
            écrivain = csv.DictWriter(fichier, fieldnames=champs)
            écrivain.writeheader()
            écrivain.writerows(données)

    

    def obtenir_forum_par_nom(self, nom_forum):
        # TODO: Implanter la logique pour chercher un forum à partir de son nom
        for f in self.forums:
            if f.nom == nom_forum:
                return f

    def obtenir_publication_par_titre(self, titre_publication):
        # TODO: Implanter la logique pour chercher une publication à partir de son titre
        for p in self.publications:
            if p.titre == titre_publication:
                return p

    
    
    
    def mettre_a_jour_forum(self, forum_id: int, nouveau_nom: str):
        """
        Permet de modifier le nom d'un forum existant en fonction de son ID.
        """
        chemin_fichier = 'src/pyforum/data/forums.json'  # Chemin fixe vers le fichier JSON

        # Charger les données du fichier JSON
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Erreur : Le fichier forums.json est introuvable.")
            return
        except json.JSONDecodeError:
            print("Erreur : Le fichier forums.json contient des données invalides.")
            return

        # Vérifie que le fichier contient une liste
        if not isinstance(data, list):
            print("Le fichier JSON ne contient pas une liste valide.")
            return

        # Chercher le forum correspondant
        forum_trouve = None
        for forum in data:
            if forum.get("id") == forum_id:
                forum_trouve = forum
                break

        if not forum_trouve:
            print(f"Erreur : Aucun forum trouvé avec l'ID {forum_id}.")
            return

        # Mettre à jour le nom du forum
        ancien_nom = forum_trouve["nom"]
        forum_trouve["nom"] = nouveau_nom

        # Sauvegarder les modifications dans le fichier JSON
        with open(chemin_fichier, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Le forum '{ancien_nom}' a été renommé en '{nouveau_nom}'.")


        #                         ^^^^^^
        #                         Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour mettre à jour le forum et retourner le forum mis à jour
        pass
