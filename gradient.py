import pygame, math

class gradient():
  def maxn(num, max):
    return(max if num > max else num)

  def minn(num, min):
    return(min if num < min else num)

  def run():
    size = width, height = 448, 320

    pygame.display.set_caption("Stratification's Color Palette Gradient")
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    font = pygame.font.SysFont('Comic Sans MS', 20)
    icon = pygame.image.load(r'icon.png')
    pygame.display.set_icon(icon)

    quit = False

    colors = [
      [pygame.Rect(257, 257, 30, 30), '', False, 0],
      [pygame.Rect(289, 257, 30, 30), '', False, 0],
      [pygame.Rect(321, 257, 30, 30), '', False, 0],
      [pygame.Rect(353, 257, 30, 30), '', False, 0],
      [pygame.Rect(385, 257, 30, 30), '', False, 0],
      [pygame.Rect(417, 257, 30, 30), '', False, 0]
    ]

    while True:
      screen.fill("light grey")

      for events in pygame.event.get():
        if events.type == pygame.QUIT:
          quit = True
          break
        if pygame.mouse.get_pressed()[0]:
          try:
            mouse_x, mouse_y = events.pos
            if mouse_y < 256:
              if mouse_x > 416:
                colors[5][3] = int(mouse_y)
              elif mouse_x > 384:
                colors[4][3] = int(mouse_y)
              elif mouse_x > 352:
                colors[3][3] = int(mouse_y)
              elif mouse_x > 320:
                colors[2][3] = int(mouse_y)
              elif mouse_x > 288:
                colors[1][3] = int(mouse_y)
              elif mouse_x > 256:
                colors[0][3] = int(mouse_y)
          except AttributeError:
            pass
          
        if events.type == pygame.MOUSEBUTTONDOWN:
          for color in colors:
            if color[0].collidepoint(events.pos):
              color[2] = not color[2]
            else:
              color[2] = False

        if events.type == pygame.KEYDOWN:
          for color in colors:
            if color[2]:
              if events.key == pygame.K_RETURN:
                try:
                  if int(color[1]) > 255:
                    color[3] = 255
                  else:
                    color[3] = int(color[1])
                  color[2] = False
                except:
                  pass
                color[1] = ''
              elif events.key == pygame.K_BACKSPACE:
                color[1] = color[1][:-1]
              elif len(color[1]) < 3:
                color[1] += events.unicode
        
        if events.type == pygame.VIDEORESIZE:
            width, height = events.size
            if width < 448:
                width = 448
            if height < 320:
                height = 320
            screen = pygame.display.set_mode((width,height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

      if quit:
        break

      for x in range(256):
        pygame.draw.line(screen, (
          gradient.maxn(gradient.minn(colors[0][3]-math.dist((x, 0), (0, 0)), 0)+gradient.minn(colors[3][3]-math.dist((x, 0), (255, 0)), 0), 255),
          gradient.maxn(gradient.minn(colors[1][3]-math.dist((x, 0), (0, 0)), 0)+gradient.minn(colors[4][3]-math.dist((x, 0), (255, 0)), 0), 255),
          gradient.maxn(gradient.minn(colors[2][3]-math.dist((x, 0), (0, 0)), 0)+gradient.minn(colors[5][3]-math.dist((x, 0), (255, 0)), 0), 255)
        ), (x, 0), (x, 255))

      for y in range(256):
        pygame.draw.line(screen, (y, 0, 0), (256, y), (287, y))
        pygame.draw.line(screen, (0, y, 0), (288, y), (319, y))
        pygame.draw.line(screen, (0, 0, y), (320, y), (351, y))

        pygame.draw.line(screen, (y, 0, 0), (352, y), (383, y))
        pygame.draw.line(screen, (0, y, 0), (384, y), (415, y))
        pygame.draw.line(screen, (0, 0, y), (416, y), (447, y))

      pygame.draw.rect(screen, (0, 0, 0), colors[0][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[1][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[2][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), (257,289,94,30), width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[3][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[4][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[5][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), (353,289,94,30), width=1)

      pygame.draw.circle(screen, (156, 156, 156), (272, colors[0][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (304, colors[1][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (336, colors[2][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (368, colors[3][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (400, colors[4][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (432, colors[5][3]), 10, width=4)

      pygame.draw.circle(screen, (196, 196, 196), (272, colors[0][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (304, colors[1][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (336, colors[2][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (368, colors[3][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (400, colors[4][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (432, colors[5][3]), 10, width=2)

      rgb1tsurface = font.render(f"{colors[0][3]} - {colors[1][3]} - {colors[2][3]}", False, (0, 0, 0))
      r1tsurface = font.render(f"{colors[0][1]}", False, (0, 0, 0))
      g1tsurface = font.render(f"{colors[1][1]}", False, (0, 0, 0))
      b1tsurface = font.render(f"{colors[2][1]}", False, (0, 0, 0))

      rgb2tsurface = font.render(f"{colors[3][3]} - {colors[4][3]} - {colors[5][3]}", False, (0, 0, 0))
      r2tsurface = font.render(f"{colors[3][1]}", False, (0, 0, 0))
      g2tsurface = font.render(f"{colors[4][1]}", False, (0, 0, 0))
      b2tsurface = font.render(f"{colors[5][1]}", False, (0, 0, 0))

      screen.blit(rgb1tsurface,(261,296))
      screen.blit(r1tsurface, (colors[0][0].x+1, colors[0][0].y+8))
      screen.blit(g1tsurface, (colors[1][0].x+1, colors[1][0].y+8))
      screen.blit(b1tsurface, (colors[2][0].x+1, colors[2][0].y+8))

      screen.blit(rgb2tsurface,(357,296))
      screen.blit(r2tsurface, (colors[3][0].x+1, colors[3][0].y+8))
      screen.blit(g2tsurface, (colors[4][0].x+1, colors[4][0].y+8))
      screen.blit(b2tsurface, (colors[5][0].x+1, colors[5][0].y+8))

      pygame.display.update()