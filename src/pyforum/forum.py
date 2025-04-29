class Forum():
    '''Classe permettant de gérer les forum'''

    def __init__(self, id :str, nom :str, listePublications :list, description :str):
        '''Constructeur de la classe permettant de gérer les différents attributs de la classe forum'''
        self.id = id
        self.nom = nom
        self.listePublications = []
        self.description = description

    def __str__(self):
        '''Cette méthode permet d'afficher les attributs de la classe Forum en format lisible'''
        return f"Forum(id={self.id}, nom='{self.nom}', liste de publication='{self.listePublications}', description='{self.description}')"
    
    def to_dict(self):
        return {"id":self.id, "nom":self.nom, "liste de Publications":self.listePublications, "description":self.description}
