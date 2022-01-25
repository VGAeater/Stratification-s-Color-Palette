import pygame

class omega2():
  def run():
    size = width, height = 512, 512

    pygame.display.set_caption("Stratification's Color Palette :D")
    screen = pygame.display.set_mode(size)
    icon = pygame.image.load(r'icon.png')
    pygame.display.set_icon(icon)

    quit = False
    i = 0

    while True:
      i += 1
      z = abs((i%510)-255)

      for events in pygame.event.get():
        if events.type == pygame.QUIT:
          quit = True
          break

      if quit:
        break

      for y in range(256):
        for x in range(256):
          screen.set_at((x+z, y+z), (x, y, z))

      pygame.display.update()
