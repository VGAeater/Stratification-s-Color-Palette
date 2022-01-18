import pygame
pygame.init()
pygame.font.init()

class classic():
  def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

  def run():
    size = width, height = 352, 352

    pygame.display.set_caption("Stratification's Color Palette Classic")
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    font = pygame.font.SysFont('Comic Sans MS', 20)
    save = pygame.transform.rotozoom(pygame.image.load(r'save.png'), 0, .15)
    clear = pygame.transform.rotozoom(pygame.image.load(r'clear.png'), 0, .15)
    icon = pygame.image.load(r'icon.png')
    pygame.display.set_icon(icon)

    saved_colors = []
    saved_colors_rects = []

    quit = False

    buttons = [
      [pygame.Rect(1,257,30,30), False],
      [pygame.Rect(1,289,30,30), False]
    ]

    colors = [
      [pygame.Rect(257, 257, 30, 30), '', False, 0],
      [pygame.Rect(289, 257, 30, 30), '', False, 0],
      [pygame.Rect(321, 257, 30, 30), '', False, 0]
    ]

    while True:
      screen.fill("light grey")

      for events in pygame.event.get():
        if events.type == pygame.QUIT:
          quit = True
        if pygame.mouse.get_pressed()[0]:
          try:
            mouse_x, mouse_y = events.pos
            if mouse_y < 256:
              if mouse_x > 320:
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
            
          for button in buttons:
            if button[0].collidepoint(events.pos):
              button[1] = True
          
          for i in range(len(saved_colors_rects)):
            if saved_colors_rects[i].collidepoint(events.pos):
              colors[0][3] = saved_colors[i][0]
              colors[1][3] = saved_colors[i][1]
              colors[2][3] = saved_colors[i][2]

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
            if width < 352:
                width = 352
            if height < 352:
                height = 352
            screen = pygame.display.set_mode((width,height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
        
        if events.type == pygame.MOUSEMOTION:
          mouse_pos = events.pos

      if quit:
        break

      pygame.draw.rect(screen, (colors[0][3], colors[1][3], colors[2][3]), (0,0,256,256))

      for y in range(256):
        pygame.draw.line(screen, (y, 0, 0), (256, y), (287, y))
        pygame.draw.line(screen, (0, y, 0), (288, y), (319, y))
        pygame.draw.line(screen, (0, 0, y), (320, y), (352, y))

      if buttons[0][1] == True:
        if len(saved_colors) < 21:
          saved_colors.append((colors[0][3], colors[1][3], colors[2][3]))
          i = len(saved_colors)-1
          saved_colors_rects.append(pygame.Rect(i*32+33-(i//7*224), i//7*32+257, 30, 30))
        buttons[0][1] = False
      
      if buttons[1][1] == True:
        try:
          saved_colors.pop()
          saved_colors_rects.pop()
        except:
          pass
        buttons[1][1] = False

      for i in range(len(saved_colors)):
        pygame.draw.rect(screen, saved_colors[i], saved_colors_rects[i])
        pygame.draw.rect(screen, (0,0,0), saved_colors_rects[i], 1)

      pygame.draw.rect(screen, (0, 0, 0), colors[0][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[1][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[2][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), (257,289,94,30), width=1)
      pygame.draw.rect(screen, (0, 0, 0), (257,321,94,30), width=1)

      pygame.draw.rect(screen, (0, 0, 0), buttons[0][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), buttons[1][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), (1,321,30,30), width=1)

      screen.blit(save, (buttons[0][0].x+3,buttons[0][0].y+3))
      screen.blit(clear, (buttons[1][0].x+3,buttons[1][0].y+3))
      screen.blit(pygame.transform.rotozoom(icon, 0, .18), (2,322))

      pygame.draw.circle(screen, (156, 156, 156), (272, colors[0][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (304, colors[1][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (336, colors[2][3]), 10, width=4)

      pygame.draw.circle(screen, (196, 196, 196), (272, colors[0][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (304, colors[1][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (336, colors[2][3]), 10, width=2)

      rgbtsurface = font.render(f"{colors[0][3]} - {colors[1][3]} - {colors[2][3]}", False, (0, 0, 0))
      hextsurface = font.render(f"#{classic.rgb_to_hex((colors[0][3], colors[1][3], colors[2][3]))}", False, (0, 0, 0))
      rtsurface = font.render(f"{colors[0][1]}", False, (0, 0, 0))
      gtsurface = font.render(f"{colors[1][1]}", False, (0, 0, 0))
      btsurface = font.render(f"{colors[2][1]}", False, (0, 0, 0))

      screen.blit(rgbtsurface,(261,296))
      screen.blit(hextsurface,(261,328))
      screen.blit(rtsurface, (colors[0][0].x+1, colors[0][0].y+8))
      screen.blit(gtsurface, (colors[1][0].x+1, colors[1][0].y+8))
      screen.blit(btsurface, (colors[2][0].x+1, colors[2][0].y+8))

      for i in range(len(saved_colors_rects)):
        if saved_colors_rects[i].collidepoint(mouse_pos):
          length = (pygame.font.Font.size(font, f"#{classic.rgb_to_hex(saved_colors[i])}")[0]+4 if pygame.font.Font.size(font, str(saved_colors[i]))[0] < pygame.font.Font.size(font, f"#{classic.rgb_to_hex(saved_colors[i])}")[0] else pygame.font.Font.size(font, str(saved_colors[i]))[0]+4)

          pygame.draw.rect(screen, "light grey", (mouse_pos[0]-2, mouse_pos[1]-34, length, 34))
          pygame.draw.rect(screen, (156, 156, 156), (mouse_pos[0]-2, mouse_pos[1]-34, length, 34), width=1)
          rgbtag = font.render(f"{str(saved_colors[i])}", False, (0, 0, 0))
          hextag = font.render(f"#{classic.rgb_to_hex(saved_colors[i])}", False, (0, 0, 0))
          screen.blit(rgbtag, (mouse_pos[0], mouse_pos[1]-32))
          screen.blit(hextag, (mouse_pos[0], mouse_pos[1]-16))

      pygame.display.update()