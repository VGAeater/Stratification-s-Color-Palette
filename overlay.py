import pygame, os, math
from PIL import Image 
import numpy as np

class overlay():
  def run():
    ims = []

    for root, dirs, files in os.walk("./"):
      for name in files:
        if name.endswith((".png", ".jpg")):
          imsize = Image.open(name).convert('L').size
          
          if imsize[0] < imsize[1]:
            tempim = Image.open(name)
            ims.append(tempim.resize((int(math.ceil(imsize[0]/(imsize[0]/256))), int(math.ceil(imsize[1]/(imsize[0]/256))))).convert('L'))
          if imsize[0] > imsize[1]:
            tempim = Image.open(name)
            ims.append(tempim.resize((int(math.ceil(imsize[0]/(imsize[1]/256))), int(math.ceil(imsize[1]/(imsize[1]/256))))).convert('L'))
          if imsize[0] == imsize[1]:
            if (256 == imsize[0]) and (256 == imsize[1]):
              ims.append(Image.open(name).convert('L'))
            else:
              tempim = Image.open(name)
              ims.append(tempim.resize((int(math.ceil(imsize[0]/(imsize[1]/256))), int(math.ceil(imsize[1]/(imsize[1]/256))))).convert('L'))

    del(imsize)

    perlin = []
    perlin_collide = []

    for ims_i in range(len(ims)):
      ims[ims_i] = np.stack((ims[ims_i],)*3, axis=-1)
      print(ims_i)
      
      perlin.append([])
      perlin_collide.append(pygame.Rect((ims_i*64+1)-(ims_i//3)*192, 257, 62, 62))

      for im_i in range(len(ims[ims_i])):
        perlin[ims_i].append([])

        for r_i in range(len(ims[ims_i][im_i])):
          perlin[ims_i][im_i].append(ims[ims_i][im_i][r_i][0]/255+.15)

    #perlin.append([])
    #perlin_collide.append(pygame.Rect(((len(perlin)-1)*64+1)-((len(perlin)-1)//3)*192, 257, 62, 62))

    #for im_i in range(256):
    #  perlin[-1].append([])

    #  for r_i in range(256):
    #    perlin[-1][im_i].append((perlin[0][im_i][r_i])/2+(perlin[2][im_i][r_i])/2)

    current_perlin = perlin[0]
    index = 0

    size = width, height = 352, 320

    arrow = pygame.transform.rotozoom(pygame.image.load(r'arrow.png'), 0, .25)

    pygame.display.set_caption("Stratification's Color Palette Overlay")
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    font = pygame.font.SysFont('Comic Sans MS', 20)
    icon = pygame.image.load(r'icon.png')
    pygame.display.set_icon(icon)

    quit = False

    colors = [
      [pygame.Rect(257, 257, 30, 30), '', False, 0],
      [pygame.Rect(289, 257, 30, 30), '', False, 0],
      [pygame.Rect(321, 257, 30, 30), '', False, 0]
    ]

    buttons = [
      [pygame.Rect(194, 257, 30, 62), False],
      [pygame.Rect(226, 257, 30, 62), False]
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
          
          for i in range(len(perlin)):
            if i//3 == index:
              if perlin_collide[i].collidepoint(events.pos):
                current_perlin = perlin[i]
          
          for button in buttons:
            if button[0].collidepoint(events.pos):
              button[1] = True

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
            if height < 320:
                height = 320
            screen = pygame.display.set_mode((width,height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

      if quit:
        break

      screen.blit(arrow, (187,268))
      screen.blit(pygame.transform.rotozoom(arrow, 180, 1), (219,267))

      if buttons[0][1]:
        if index != 0:
          index -= 1
        else:
          index = (len(perlin)-1)//3
        buttons[0][1] = False
      
      if buttons[1][1]:
        if index != (len(perlin)-1)//3:
          index += 1
        else:
          index = 0
        buttons[1][1] = False

      for y in range(256):
        for x in range(256):
          screen.set_at((x,y), (
              255 if colors[0][3]*current_perlin[y][x] > 255 else colors[0][3]*current_perlin[y][x],
              255 if colors[1][3]*current_perlin[y][x] > 255 else colors[1][3]*current_perlin[y][x],
              255 if colors[2][3]*current_perlin[y][x] > 255 else colors[2][3]*current_perlin[y][x]
            )
          )
      
      for i in range(len(perlin)):
        if i//3 == index:
          pygame.draw.rect(screen, (0,0,0), perlin_collide[i], 1)
          for x in range(60):
            for y in range(60):
              color = 255 if (perlin[i][y*4][x*4])*255 > 255 else (perlin[i][y*4][x*4])*255
              screen.set_at((perlin_collide[i].x+x+1, perlin_collide[i].y+y+1), (color, color, color))


      for y in range(256):
        pygame.draw.line(screen, (y, 0, 0), (256, y), (287, y))
        pygame.draw.line(screen, (0, y, 0), (288, y), (319, y))
        pygame.draw.line(screen, (0, 0, y), (320, y), (352, y))

      pygame.draw.rect(screen, (0, 0, 0), colors[0][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[1][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), colors[2][0], width=1)
      pygame.draw.rect(screen, (0, 0, 0), (257,289,94,30), width=1)

      pygame.draw.circle(screen, (156, 156, 156), (272, colors[0][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (304, colors[1][3]), 10, width=4)
      pygame.draw.circle(screen, (156, 156, 156), (336, colors[2][3]), 10, width=4)

      pygame.draw.circle(screen, (196, 196, 196), (272, colors[0][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (304, colors[1][3]), 10, width=2)
      pygame.draw.circle(screen, (196, 196, 196), (336, colors[2][3]), 10, width=2)

      rgbtsurface = font.render(f"{colors[0][3]} - {colors[1][3]} - {colors[2][3]}", False, (0, 0, 0))
      rtsurface = font.render(f"{colors[0][1]}", False, (0, 0, 0))
      gtsurface = font.render(f"{colors[1][1]}", False, (0, 0, 0))
      btsurface = font.render(f"{colors[2][1]}", False, (0, 0, 0))

      screen.blit(rgbtsurface,(261,296))
      screen.blit(rtsurface, (colors[0][0].x+1, colors[0][0].y+8))
      screen.blit(gtsurface, (colors[1][0].x+1, colors[1][0].y+8))
      screen.blit(btsurface, (colors[2][0].x+1, colors[2][0].y+8))

      pygame.display.update()