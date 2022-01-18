import pygame, sys
from classic import classic
from gradient import gradient
from fade import fade
from omega import omega
pygame.init()
pygame.font.init()

def home():
  size = width, height = 512, 288

  pygame.display.set_caption("Stratification's Color Palette Home")
  screen = pygame.display.set_mode(size)
  font = pygame.font.SysFont('Comic Sans MS', 20)
  icon = pygame.image.load(r'icon.png')
  pygame.display.set_icon(icon)

  buttons = [
    [pygame.Rect(1,31,62,30), False, classic],
    [pygame.Rect(65,31,62,30), False, gradient],
    [pygame.Rect(129,31,62,30), False, fade],
    [pygame.Rect(193,31,62,30), False, omega]
  ]

  while True:
    screen.fill("light grey")

    for events in pygame.event.get():
      if events.type == pygame.QUIT:
        sys.exit()

      if events.type == pygame.MOUSEBUTTONDOWN:
        for button in buttons:
          if button[0].collidepoint(events.pos):
            button[1] = True

    for button in buttons:
      if button[1] == True:
        button[2].run()
        button[1] = False
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Stratification's Color Palette Home")
      
      pygame.draw.rect(screen, (0, 0, 0), button[0], width=1)

    tsurface = font.render("Welcome to Stratification's Color Palette!", True, (0, 0, 0))
    classictsurface = font.render("Classic", True, (0, 0, 0))
    gradienttsurface = font.render("Gradient", True, (0, 0, 0))
    fadetsurface = font.render("Fade", True, (0, 0, 0))
    omegatsurface = font.render(":D", True, (0, 0, 0))

    screen.blit(tsurface,(4,8))
    screen.blit(classictsurface,(4,38))
    screen.blit(gradienttsurface,(68,38))
    screen.blit(fadetsurface,(132,38))
    screen.blit(omegatsurface,(197,38))

    pygame.display.update()

home()
