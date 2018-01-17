import pygame
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super(self.__class__,self).__init__()

        self.image = pygame.image.load('Pipe.png').convert()

        self.rect = self.image.get_rect()