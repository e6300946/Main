class Commentaire:
    def __init__(self, id: str, auteur_id: str, contenu: str, publication_id: str):
        self.id = id
        self.auteur_id = auteur_id
        self.contenu = contenu
        self.publication_id = publication_id

    def __repr__(self):
        return (f"Commentaire(id={self.id}, auteur_id={self.auteur_id}, "
                f"contenu={self.contenu}, publication_id={self.publication_id})")
    "cette méthode permet d'afficher en format lisible les attributs de la classe commentaire"

    def to_dict(self):
        """Cette méthode permet d'ajouter les attributs de la classe commentaire dans un dictionnaire"""
        return {"id":self.id, "identifiant de l'auteur":self.auteur_id, "adresse Courriel":self.contenu, "publications":self.publication_id}
