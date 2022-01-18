import pygame
pygame.init()

class omega3():
  def run():
    size = width, height = 512, 512

    pygame.display.set_caption("Stratification's Color Palette :D")
    screen = pygame.display.set_mode(size)
    icon = pygame.image.load(r'icon.png')
    pygame.display.set_icon(icon)

    quit = False
    i = 0

    while True:
      z = abs((i%511)-255)
      i += 1

      for events in pygame.event.get():
        if events.type == pygame.QUIT:
          quit = True

      if quit:
        break

      for y in range(256):
        for x in range(256):
          if ((x == 255 or x == 0) and (y == 255 or y == 0)) or ((y == 255 or y == 0) and (z == 255 or z == 0)) or ((z == 255 or z == 0) and (x == 255 or x == 0)):
            pygame.draw.circle(screen, (0, 0, 0), (x+z, y+z), 1)
          elif (x == 255 or y == 255 or z == 255 or x == 0 or y == 0 or z == 0) and (x == 255 or y == 255 or z == 255 or x == 0 or y == 0 or z == 0):
            pygame.draw.circle(screen, (x, y, z), (x+z, y+z), 1)

      pygame.display.update()
