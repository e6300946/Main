# Importation des classes nécessaires
from time import sleep
from datetime import datetime
from pyforum.bd import BD


def afficher_menu():


    """Fonction permettant d'afficher les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. accédée a un forum ou une publication")
    print("6. Rejoindre un forum")
    print("7. Quitter")
    


def main():
    """Fonction permettant d'afdficher les options du menu"""
    print ("hello")
    # Initialisation de la base de données
    db = BD() 
    
    

    while True:
        afficher_menu()
        print ("\n BIENVENUE SUR PYFORUM")
        choix = input("Veulliez choisir une option (1-7): ")
        # Demander à l'utilisateur de choisir une option
        while choix not in ['1', '2', '3', '4', '5', '6', '7']:
            print ("Veuillez choisir une option valide (1-7)")
            choix = input("Veulliez choisir une option (1-7): ")
        

        if choix == '1':
            


            print ("Bienvenue dans le module de création d'utilisateur")
            print ( "voulez vous continuer ? (saisir oui/non) ")
            reponse = input("Réponse : ")
            if reponse == "oui":

                print ("Veuillez entrer les informations suivantes :")
                username = input("Entrez le nom d'utilisateur:")
                adresseCourriel = input("Entrez l'adresse courriel de l'utilisateur:")
                motDePasse = input("Entrez le  mot de passe pour cet utilisateur:")
                listeForums = [input("Entrez les forums de cette utilisateur:")]

                db.creer_utilisateur(username = username, adresseCourriel=adresseCourriel, motDePasse=motDePasse, listeForums=listeForums)
                db.sauvegardeDutilisateurs()
                #print('votre compte utilisateur a été créé avec succès!')
            elif reponse == "non":
                print (afficher_menu)
            
            else : 
                print ( 'veuillez entrer une réponse valide. (oui/non)')
                
            

        elif choix == '2':

            


            # Créer un forum
            print("Bienvenue dans le module de création de forum")
            print("Suivez les instructions suivante pour créer un forum de discussion.")
            print("voulez vous continuer ? (saisir oui/non)")
            reponse = input("Réponse : ")
            if reponse == "oui":
                print ("Veuillez entrer les informations suivantes :")
                nom = input("Entrez le nom du forum que vous voulez créer:")
                description = input("Entrez la description du forum que vous voulez créer:")
                listePublications = [input("Entrez les publications du forum que vous voulez créer:")]
                print (db.creer_forum(nom = nom, description = description, listePublications = listePublications))
                db.sauvegardeDeForums()
                print ("votre forum de discussion a été créé avec succès.")

            elif reponse == "non":
                print (afficher_menu)
            else :
                print ( 'veuillez entrer une réponse valide. (oui/non)')

                "# TODO: Ajouter ici la logique pour demander des informations à l'utilisateur"
                "# TODO: Ajouter l'appel à la base de donnée pour créer le forum "

        elif choix == '3':
            print("Bienvenue dans le module de création de publication")
            print("Suivez les instructions suivante pour créer une publication.")
            print("voulez vous continuer ? (saisir oui/non)")
            reponse = input("Réponse : ")
            if reponse == "oui":

                # Créer une publication
                print("Bienvenue dans le module de création de publication")
                print("Suivez les instructions suivante pour créer une publication.")
                titre = input("Entrez le titre de la publication que vous voulez créer:")
                contenu = input("Entrez le contenu de la publication que vous voulez créer:")
                listeCommentaires = []
                print("Début de saisie des commentaires.")
                
                while True:
                    commentaire = input("Entrez un commentaire (ou appuyez sur Entrée pour terminer) : ")
                    if commentaire == "":
                        break
                    listeCommentaires.append(commentaire)
                print(db.creer_publication(titre=titre, contenu=contenu, listeCommentaires=listeCommentaires))
                db.sauvegardeDePublications()
                print ("votre publication a été créée avec succès.")
                
                # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
                # TODO: Ajouter l'appel à la base de donnée pour créer la publication
            elif reponse == "non":
                print (afficher_menu)
            else :
                print ( 'veuillez entrer une réponse valide. (oui/non)')

                
        elif choix == '4':
            print("Bienvenue dans le module de création d'un commentaire")
            print("Suivez les instructions suivante pour créer une commentaire.")
            print("voulez vous continuer ? (saisir oui/non)")
            reponse = input("Réponse : ")
            if reponse == "oui":
                # Ajouter un commentaire
                print ("Bienvenue dans le module d'ajout de commentaire")
                print ("Suivez les instructions suivante pour ajouter un commentaire à une publication.")
                contenu = input("Entrez le ccommentaire que vous voulez publier:")
                id = input("Entrez un l'identifiant de ce commentaire")
                print (db.creer_commentaire(id = id, contenu = contenu))
                db.sauvegardeDesCommentaires()
                print ("votre commentaire a été ajouté avec succès.")
            elif reponse == "non":
                print (afficher_menu)
            else :
                print ( 'veuillez entrer une réponse valide. (oui/non)')

                # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
                # TODO: Ajouter l'appel à la base de donnée pour créer le commentaire

        elif choix == '5':
                # Joindre un forum
            print("Bienvenue dans le module pour joindre d'un forum")
            print("Suivez les instructions suivante pour joindre forum.")
            print("voulez vous continuer ? (saisir oui/non)")
            reponse = input("Réponse : ")
            if reponse == "oui":
                print("Suivre les intructions suivante pour afficher un forums ou une publication.")
                print ("voulez chercher un forum ou une publication ? (saisir forum/publication)")
                reponse = input ("Réponse : ")
                if reponse != "forum" and reponse != "publication":
                    print ("Veuillez entrer 'forum' ou 'publication")
                    reponse = input ("Réponse : ")
            
                elif reponse == "forum":
                    print (db.obtenir_forum_par_nom)

                    print ("vous avez rejoint ce forum avec succès.")

                elif reponse == "publication":
                    print (db.obtenir_publication_par_titre)
                    
            elif reponse == "non":
                print (afficher_menu)
            else :
                print ( 'veuillez entrer une réponse valide. (oui/non)')    
                # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
                # TODO: Ajouter les appels à la base de donnée pour ajouter l'utilisateur au forum
        
        elif choix == '6':
            print("Bienvenue dans le module pour créer un forum")
            print("Suivez les instructions suivante pour créer forum.")
            print("voulez vous continuer ? (saisir oui/non)")
            reponse = input("Réponse : ")
            if reponse == "oui":
            
                # Rejoindre un forum
                print("Bienvenue dans le module de création d'un commentaire")
                print("Suivez les instructions suivante pour créer une commentaire.")
                print("voulez vous continuer ? (saisir oui/non)")
                reponse = input("Réponse : ")
                if reponse == "oui":
                        print("Bienvenue dans le module de mise à jour d'un forum.")
                        forum_id = int(input("Entrez l'ID du forum que vous souhaitez modifier : "))
                        nouveau_nom = input("Entrez le nouveau nom du forum : ")
                        db.mettre_a_jour_forum(forum_id=forum_id, nouveau_nom=nouveau_nom)
            elif reponse == "non":
                print (afficher_menu)    
                            
                       
                        
        elif choix == '7':
                # Quitter le programme
                print("\nMerci d'avoir utilisé PyForum. À bientôt!")
                break

        else:
                print("Option invalide. Veuillez essayer à nouveau.")

        sleep(1)  # Pause de 1 secondes pour rendre l'interface plus agréable
if __name__ == "__main__":
    main().main()  # Appelle la méthode `main()` de la classe `main`


    