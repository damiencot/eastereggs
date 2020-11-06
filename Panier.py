import pygame


class Panier(pygame.sprite.Sprite):

    def __init__(self, largeur_ecran, hauteur_ecran):
        super().__init__()
        self.largeur_ecran = largeur_ecran
        self.points = 50
        self.maximun_points = 100
        self.image = pygame.image.load('assets/panier.png')
        self.rect = self.image.get_rect()
        self.rect.x = (largeur_ecran / 2)
        self.rect.y = hauteur_ecran - 180
        self.vitesse = 6

    def enlever_points(self):
        if self.points - 2 > 0:
            print("-2 points")
            self.points -= 2
        else:
            print("Perdu")

    # methode pour le deplacement droite
    def deplacement_droite(self):
        if self.rect.x + self.image.get_width() < self.largeur_ecran:
            self.rect.x += self.vitesse

    # methode pour le deplacement gauche
    def deplacement_gauche(self):
        if self.rect.x > 0:
            self.rect.x -= self.vitesse