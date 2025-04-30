# Importation des classes nécessaires
from time import sleep
from datetime import datetime
from pyforum.bd import BD


def liste_vide ():
    utilisateurs = []
    forums = []
    publications = []
    commentaires = []



def afficher_menu():

    """Affiche les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. accédée a un forum ou une publication")
    print("6. Rejoindre un forum")
    print("7. Quitter")
    


def main():
    print ("hello")
    # Initialisation de la base de données
    db = BD() 
    
    

    while True:
        afficher_menu()
        print ("\n BIENVENUE SUR PYFORUM")
        choix = input("Veulliez choisir une option (1-6): ")
        # Demander à l'utilisateur de choisir une option
        while choix not in ['1', '2', '3', '4', '5', '6']:
            print ("Veuillez choisir une option valide (1-6)")
            choix = input("Veulliez choisir une option (1-6): ")
        

        if choix == '1':
            ' from bd import BD'


            print ("Bienvenue dans le module de création d'utilisateur")
            print ( "voulez vous continuer ? (saisir oui/non) ")
            reponse = input("Réponse : ")
            while reponse == "oui":

                print ("Veuillez entrer les informations suivantes :")
                username = input("Entrez le nom d'utilisateur:")
                adresseCourriel = input("Entrez l'adresse courriel de l'utilisateur:")
                motDePasse = input("Entrez le  mot de passe pour cet utilisateur:")
                listeForums = [input("Entrez les forums de cette utilisateur:")]

                db.creer_utilisateur(username = username, adresseCourriel=adresseCourriel, motDePasse=motDePasse, listeForums=listeForums)
                db.sauvegardeDutilisateurs()
                #print('votre compte utilisateur a été créé avec succès!')
            if reponse == "non":
                print (afficher_menu)
            
            else : 
                print ( 'veuillez entrer une réponse valide. (oui/non)')
                
            

        elif choix == '2':

            x=0


            # Créer un forum
            print("Bienvenue dans le module de création de forum")
            print("Suivez les instructions suivante pour créer un forum de discussion.")
            print("voulez vous continuer ? (saisir oui/non)")
            reponse = input("Réponse : ")
            while reponse == "oui":
                print ("Veuillez entrer les informations suivantes :")
                nom = input("Entrez le nom du forum que vous voulez créer:")
                description = input("Entrez la description du forum que vous voulez créer:")
                listePublications = [input("Entrez les publications du forum que vous voulez créer:")]
                print (db.creer_forum(nom = nom, description = description, listePublications = listePublications))
<<<<<<< HEAD
=======
                db.sauvegardeDeForums()
>>>>>>> main
                print ("votre forum de discussion a été créé avec succès.")

            if reponse == "non":
                print (afficher_menu)
            else :
                print ( 'veuillez entrer une réponse valide. (oui/non)')

                "# TODO: Ajouter ici la logique pour demander des informations à l'utilisateur"
                "# TODO: Ajouter l'appel à la base de donnée pour créer le forum "

        elif choix == '3':

                # Créer une publication
                print("Bienvenue dans le module de création de publication")
                print("Suivez les instructions suivante pour créer une publication.")
                titre = input("Entrez le titre de la publication que vous voulez créer:")
                contenu = input("Entrez le contenu de la publication que vous voulez créer:")
<<<<<<< HEAD
                print (db.creer_publication(titre = titre, contenu = contenu, date_creation= datetime.now()))
=======
                listeCommentaires = []
                print("Début de saisie des commentaires.")
                
                while True:
                    commentaire = input("Entrez un commentaire (ou appuyez sur Entrée pour terminer) : ")
                    if commentaire == "":
                        break
                    listeCommentaires.append(commentaire)
                print(db.creer_publication(titre=titre, contenu=contenu, listeCommentaires=listeCommentaires))
                db.sauvegardeDePublications()
>>>>>>> main
                print ("votre publication a été créée avec succès.")
                
                # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
                # TODO: Ajouter l'appel à la base de donnée pour créer la publication

        elif choix == '4':
                # Ajouter un commentaire
                print ("Bienvenue dans le module d'ajout de commentaire")
                print ("Suivez les instructions suivante pour ajouter un commentaire à une publication.")
<<<<<<< HEAD
                print (db.creer_commentaire)
=======
                contenu = input("Entrez le ccommentaire que vous voulez publier:")
                id = input("Entrez un l'identifiant de ce commentaire")
                print (db.creer_commentaire(id = id, contenu = contenu))
                db.sauvegardeDesCommentaires()
>>>>>>> main
                print ("votre commentaire a été ajouté avec succès.")
                

                # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
                # TODO: Ajouter l'appel à la base de donnée pour créer le commentaire

        elif choix == '5':
                # Joindre un forum
                
                print("Suivre les intructions suivante pour afficher un forums ou une publication.")
                print ("voulz chercher un forum ou une publication ? (saisir forum/publication)")
                reponse = input ("Réponse : ")
                while reponse != "forum" and reponse != "publication":
                    print ("Veuillez entrer 'forum' ou 'publication")
                    reponse = input ("Réponse : ")
            
                if reponse == "forum":
                    print (db.obtenir_forum_par_nom)

                    print ("vous avez rejoint ce forum avec succès.")

                elif reponse == "publication":
<<<<<<< HEAD
                    print (obtenir_publication_par_titre)
                    print ("Veuillez entrer le nom de la publication que vous souhaitez rejoindre.")        
                print (cree_joindre_forum) 
                print ("vous avez rejoint ces forums avec succès.")
=======
                    print (db.obtenir_publication_par_titre)
                    
>>>>>>> main
                 
                # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
                # TODO: Ajouter les appels à la base de donnée pour ajouter l'utilisateur au forum
        elif choix == '6':
                        # Rejoindre un forum
                        print("Bienvenue dans le module de rejoindre un forum")
                        print("Suivez les instructions suivante pour rejoindre un forum.")
                        print ("voulez vous rejoindre un forum ? (saisir oui/non)")
                        print ("vous avez rejoint ce forum avec succès.")
                        reponse = input("Réponse : ")
                        while reponse == "oui":
                            print (mettre_a_jour_forum)
                            break
                        else:
                             return (main)
                            
                       
                        
        elif choix == '7':
                # Quitter le programme
                print("\nMerci d'avoir utilisé PyForum. À bientôt!")
                break

        else:
                print("Option invalide. Veuillez essayer à nouveau.")

        sleep(1)  # Pause de 1 secondes pour rendre l'interface plus agréable
if __name__ == "__main__":
    main().main()  # Appelle la méthode `main()` de la classe `main`


    