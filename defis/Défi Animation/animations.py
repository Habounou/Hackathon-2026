import numpy as np
import pygame


class Button:

    def __init__(self, color, x, y, width, height, text='', text_size=18):
        self.color = color
        self.base_color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0, int(np.ceil(self.text_size / 2)))

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0, int(np.ceil(self.text_size / 2)))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.text_size)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def hover(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
                self.color = (self.base_color[0] + 40, self.base_color[1] + 40, self.base_color[2] + 40)
        else:
            self.color = self.base_color

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

current_screen = "Idol"
mouse_clicked = False
pi = np.pi
rotation = 0
vitesse = 5

while running:
    screen.fill((30, 30, 30))

    cote_restraint = min(screen.get_width() / 1280, screen.get_height() / 720)

    boutons_size = (cote_restraint * 200, cote_restraint * 50)
    bouton_anim1 = Button((70, 70, 70), 0, screen.get_height() - boutons_size[1], boutons_size[0],
                          boutons_size[1], "Animation 1", int(cote_restraint * 18))
    bouton_anim2 = Button((70, 70, 70), (screen.get_width() - boutons_size[0]) // 2,
                          screen.get_height() - boutons_size[1], boutons_size[0],
                          boutons_size[1], "Animation 2", int(cote_restraint * 18))
    bouton_anim3 = Button((70, 70, 70), screen.get_width() - boutons_size[0],
                          screen.get_height() - boutons_size[1], boutons_size[0],
                          boutons_size[1], "Animation 3", int(cote_restraint * 18))
    bouton_anim1.hover(pygame.mouse.get_pos())
    bouton_anim2.hover(pygame.mouse.get_pos())
    bouton_anim3.hover(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if mouse_clicked:
                if bouton_anim1.is_over(pygame.mouse.get_pos()):
                    current_screen = "Animation 1"
                    rotation = 0
                elif bouton_anim2.is_over(pygame.mouse.get_pos()):
                    current_screen = "Animation 2"
                    rotation = 0
                    vitesse = 5
                elif bouton_anim3.is_over(pygame.mouse.get_pos()):
                    current_screen = "Animation 3"
                mouse_clicked = False

    if current_screen == "Idol":
        rectangle_size = (cote_restraint * 600, cote_restraint * 600)
        rectangle = pygame.Rect(((screen.get_width() - rectangle_size[0]) // 2,
                                (screen.get_height() - rectangle_size[1]) // 2), rectangle_size)
        pygame.draw.rect(screen, (255, 0, 0), rectangle)
        pygame.draw.rect(screen, (0, 0, 0), rectangle, int(cote_restraint * 8))

    elif current_screen == "Animation 1":
        rotation -= 1.5

        surface_carree_size = min(screen.get_width(), screen.get_height())
        surface1 = pygame.surface.Surface((surface_carree_size, surface_carree_size), pygame.SRCALPHA)

        rect_parabole_size = (cote_restraint * 350, cote_restraint * 200)
        rectangle_parabole = pygame.Rect(((surface_carree_size - rect_parabole_size[0]) // 2,
                                (surface_carree_size - rect_parabole_size[1] + cote_restraint * 150) // 2), rect_parabole_size)
        rect_yeux_size = (cote_restraint * 100, cote_restraint * 150)
        rectangle_oeil_gauche = pygame.Rect(((surface_carree_size - rect_yeux_size[0] - cote_restraint * 200) // 2,
                                (surface_carree_size - rect_yeux_size[1] - cote_restraint * 150) // 2), rect_yeux_size)
        rectangle_oeil_droit = pygame.Rect(((surface_carree_size - rect_yeux_size[0] + cote_restraint * 200) // 2,
                                      (surface_carree_size - rect_yeux_size[1] - cote_restraint * 150) // 2),
                                     rect_yeux_size)

        pygame.draw.circle(surface1, (255, 255, 0),
                           (surface_carree_size // 2, surface_carree_size // 2), cote_restraint * 300)
        pygame.draw.circle(surface1, (0, 0, 0),
                           (surface_carree_size // 2, surface_carree_size // 2), cote_restraint * 300,
                           int(cote_restraint * 8))
        pygame.draw.arc(surface1, (0, 0, 0), rectangle_parabole, 7 * pi / 6, -pi / 6, int(cote_restraint * 8))
        pygame.draw.ellipse(surface1, (0, 0, 0), rectangle_oeil_gauche)
        pygame.draw.ellipse(surface1, (0, 0, 0), rectangle_oeil_droit)

        surface1 = pygame.transform.rotate(surface1, rotation)
        dx = (screen.get_width() - surface1.get_width()) / 2
        dy = (screen.get_height() - surface1.get_height()) / 2
        screen.blit(surface1, (dx, dy))

    elif current_screen == "Animation 2":
        rotation -= 1.5 * vitesse / 100
        vitesse += 1.4
        vitesse *= 1.01

        surface_carree_size = min(screen.get_width(), screen.get_height())
        surface2 = pygame.surface.Surface((surface_carree_size, surface_carree_size), pygame.SRCALPHA)

        rect_corps_auto_size = (cote_restraint * 250, cote_restraint * 80)
        rectangle_corps_auto = pygame.Rect((0, (surface_carree_size - rect_corps_auto_size[1]) // 2 + cote_restraint * 150), rect_corps_auto_size)
        pygame.draw.rect(surface2, (255, 0, 0), rectangle_corps_auto, border_radius=int(cote_restraint * 20))

        points_capot = [(rectangle_corps_auto.width / 8, rectangle_corps_auto.y),
                        (rectangle_corps_auto.width / 4, rectangle_corps_auto.y - rectangle_corps_auto.height / 1.5),
                        (rectangle_corps_auto.width * 5 / 8, rectangle_corps_auto.y - rectangle_corps_auto.height / 1.5),
                        (rectangle_corps_auto.width * 7 / 9, rectangle_corps_auto.y)]
        pygame.draw.polygon(surface2, (255, 0, 0), points_capot)
        points_vitre = [(rectangle_corps_auto.width / 8 + cote_restraint * 10, rectangle_corps_auto.y),
                        (rectangle_corps_auto.width / 4 + cote_restraint * 4, rectangle_corps_auto.y - rectangle_corps_auto.height / 1.5 + cote_restraint * 10),
                        (rectangle_corps_auto.width * 4 / 9, rectangle_corps_auto.y - rectangle_corps_auto.height / 1.5 + cote_restraint * 10),
                        (rectangle_corps_auto.width * 4 / 9, rectangle_corps_auto.y)]
        pygame.draw.polygon(surface2, (200, 220, 255), points_vitre)
        points_vitre = [(rectangle_corps_auto.width * 4 / 9 + cote_restraint * 10, rectangle_corps_auto.y),
                        (rectangle_corps_auto.width * 4 / 9 + cote_restraint * 10, rectangle_corps_auto.y - rectangle_corps_auto.height / 1.5 + cote_restraint * 10),
                        (rectangle_corps_auto.width * 5 / 8 - cote_restraint * 2, rectangle_corps_auto.y - rectangle_corps_auto.height / 1.5 + cote_restraint * 10),
                        (rectangle_corps_auto.width * 7 / 9 - cote_restraint * 10, rectangle_corps_auto.y)]
        pygame.draw.polygon(surface2, (200, 220, 255), points_vitre)

        surface_roues_size = (cote_restraint * 56, cote_restraint * 56)
        surface_roue_gauche = pygame.surface.Surface(surface_roues_size, pygame.SRCALPHA)
        surface_roue_droite = pygame.surface.Surface(surface_roues_size, pygame.SRCALPHA)

        pygame.draw.circle(surface_roue_gauche, (0, 0, 0), (surface_roues_size[0] // 2, surface_roues_size[1] // 2), cote_restraint * 28)
        pygame.draw.line(surface_roue_gauche, (180, 180, 180), (surface_roues_size[0] // 2 - cote_restraint * 28, surface_roues_size[1] // 2),
                         (surface_roues_size[0] // 2, surface_roues_size[1] // 2), int(np.ceil(cote_restraint * 2)))

        pygame.draw.circle(surface_roue_droite, (0, 0, 0),(surface_roues_size[0] // 2, surface_roues_size[1] // 2), cote_restraint * 28)
        pygame.draw.line(surface_roue_droite, (180, 180, 180), (surface_roues_size[0] // 2 - cote_restraint * 28, surface_roues_size[1] // 2),
                         (surface_roues_size[0] // 2, surface_roues_size[1] // 2), int(np.ceil(cote_restraint * 2)))

        surface_roue_gauche = pygame.transform.rotate(surface_roue_gauche, rotation)
        dx_gauche = -surface_roue_gauche.get_width() / 2
        dy_gauche = -surface_roue_gauche.get_height() / 2
        surface2.blit(surface_roue_gauche, (dx_gauche + rectangle_corps_auto.width / 5, dy_gauche + rectangle_corps_auto.y + rectangle_corps_auto.height))
        surface_roue_droite = pygame.transform.rotate(surface_roue_droite, rotation)
        dx_droite = -surface_roue_droite.get_width() / 2
        dy_droite = -surface_roue_droite.get_height() / 2
        surface2.blit(surface_roue_droite, (dx_droite + rectangle_corps_auto.width * 4 / 5, dy_droite + rectangle_corps_auto.y + rectangle_corps_auto.height))

        screen.blit(surface2, (-rect_corps_auto_size[0] + (vitesse - 30) * cote_restraint, 0))
        if -rect_corps_auto_size[0] + (vitesse - 30) * cote_restraint > screen.get_width():
            vitesse = 5


    bouton_anim1.draw(screen)
    bouton_anim2.draw(screen)
    bouton_anim3.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()