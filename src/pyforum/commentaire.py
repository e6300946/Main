class Commentaire:
    def __init__(self, id: str, auteur_id: str, contenu: str, publication_id: str):
        self.id = id
        self.auteur_id = auteur_id
        self.contenu = contenu
        self.publication_id = publication_id

    def __repr__(self):
        return (f"Commentaire(id={self.id}, auteur_id={self.auteur_id}, "
                f"contenu={self.contenu}, publication_id={self.publication_id})")