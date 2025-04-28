class publication():

    def __init__(self, titre, identifiant, contenu, date_creation):
        self.titre = titre
        self.identifiant = identifiant
        self.contenu = contenu
        self.date_creation = date_creation


    def __str__(self):
        return f"Publication {self.identifiant} : {self.contenu} - {self.date_creation}"
    

''' ceci est le code de la classe publication '''