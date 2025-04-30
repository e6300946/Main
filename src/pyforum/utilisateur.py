class Utilisateur():
    '''Classe permettant de gérer les utilisateurs du forum'''
<<<<<<< HEAD
    def __init__(self, id, username, adresseCourriel, motDePasse, listeForums):
=======
    def __init__(self, id :str, username: str, adresseCourriel: str, motDePasse: str, listeForums: list):
>>>>>>> branche-tony
        '''Constructeur de la classe permettant de gérer les différents attributs de la classe utilisateurs'''
        self.id = id
        self.username = username
        self.adresseCourriel = adresseCourriel
        self.motDePasse = motDePasse
        self.listeForums = []

    def __str__(self):
        """Méthode permettant d'afficher en format lisible les attributs de la classe utilisateur"""
<<<<<<< HEAD
        return f"Utilisateur(id={self.id}, username='{self.username}', adresse courriel='{self.adresseCourriel}', mot de passe='{self.motDePasse}')"
    
    def to_dict(self):
=======
        return f"id:{self.id}, username:{self.username}, adresse courriel:{self.adresseCourriel}, mot de passe:{self.motDePasse}"
    
    def to_dict(self):
        """Cette méthode permet d'ajouter les attributs de la classe utilisateurs dans un dictionnaire"""
>>>>>>> branche-tony
        return {"id":self.id, "username":self.username, "adresse Courriel":self.adresseCourriel, "motDePasse":self.motDePasse, "liste de forums":self.listeForums}
