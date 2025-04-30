class publication():
    """Méthode permettant de gérer la classe publication"""

    def __init__(self, titre :str, identifiant :str, contenu :str, date_creation :str, identifiantAuteur :str, identifiantForum :str, listeCommentaires :list):
        self.titre = titre
        self.identifiant = identifiant
        self.contenu = contenu
        self.date_creation = date_creation
        self.identifiantAuteur = identifiantAuteur
        self.identifiantForum = identifiantForum
        self.listeCommentaires = []


    def __str__(self):
        """Méthode permettant d'afficher les attributs de la classe publication en format lisible"""
        return f"titre:{self.titre}, identifiant:{self.identifiant}, contenu:{self.contenu}, date de création:{self.date_creation}, identifiant de l'auteur:{self.identifiantAuteur}, identifiant forum:{self.identifiantForum}, liste de commentaires:{self.listeCommentaires}"
    
    def to_dict(self):
        """Cette méthode permet d'ajouter les attributs de la classe utilisateurs dans un dictionnaire"""
        return {"titre":self.titre, "identifiant":self.identifiant, "contenu":self.contenu, "date de création":self.date_creation, "identifiant de l'auteur":self.identifiantAuteur, "identifiant forum":self.identifiantForum, "liste de commentaires":self.listeCommentaires}

''' ceci est le code de la classe publication '''