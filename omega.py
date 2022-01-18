import pygame
from omega1 import omega1
from omega2 import omega2
from omega3 import omega3
pygame.init()
pygame.font.init()

class omega():
  def run():
    size = width, height = 512, 288

    pygame.display.set_caption("Stratification's Color Palette :D")
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont('Comic Sans MS', 20)
    icon = pygame.image.load(r'icon.png')
    pygame.display.set_icon(icon)

    buttons = [
      [pygame.Rect(1,31,62,30), False, omega1],
      [pygame.Rect(65,31,62,30), False, omega2],
      [pygame.Rect(129,31,62,30), False, omega3],
      #[pygame.Rect(193,31,62,30), False, omega4]
      [pygame.Rect(1,95,62,30), False]
    ]

    quit = False

    while True:
      screen.fill("light grey")

      for events in pygame.event.get():
        if events.type == pygame.QUIT:
          quit = True

        if events.type == pygame.MOUSEBUTTONDOWN:
          for button in buttons:
            if button[0].collidepoint(events.pos):
              button[1] = True

      for button in buttons:
        if button == buttons[-1]:
          if button[1] == True:
            quit = True
        elif button[1] == True:
          button[2].run()
          button[1] = False
          screen = pygame.display.set_mode(size)
          pygame.display.set_caption("Stratification's Color Pallet Home")
        
        pygame.draw.rect(screen, (0, 0, 0), button[0], width=1)
      
      if quit:
        break

      tsurface = font.render("Welcome to Stratification's Color Palette!", True, (0, 0, 0))
      omega1tsurface = font.render("Original", True, (0, 0, 0))
      omega2tsurface = font.render("V2", True, (0, 0, 0))
      omega3tsurface = font.render("V3", True, (0, 0, 0))
      #omega4tsurface = font.render(":D", True, (0, 0, 0))
      backtsurface = font.render("Back", True, (0, 0, 0))

      screen.blit(tsurface,(4,8))
      screen.blit(omega1tsurface,(4,38))
      screen.blit(omega2tsurface,(68,38))
      screen.blit(omega3tsurface,(132,38))
      #screen.blit(omega4tsurface,(197,38))
      screen.blit(backtsurface,(4,102))

      pygame.display.update()
