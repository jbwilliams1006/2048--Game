#Creating the 2048 game!
import pygame

from pygame.locals import QUIT
#from random import *
import random
import sys
import matplotlib.pyplot as plt
from pygame import mixer

#Instantiate mixer
mixer.init()

buttons = []
class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
 
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
 
		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text = text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
		buttons.append(self)
 
	def change_text(self, newtext):
		self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 
 
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
 
		pygame.draw.rect(display,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(display,self.top_color, self.top_rect,border_radius = 12)
		display.blit(self.text_surf, self.text_rect)
		self.check_click()
 
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print(f'{self.text} clicked')
					self.pressed = False
					self.change_text(self.text)
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'


pygame.init()  #used to initialize the pygame

timer = pygame.time.Clock()
fps = 60
WIDTH = 640
HEIGHT = 480
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("2048 Game by Izzy and Josh")
gui_font = pygame.font.Font('freesansbold.ttf',24)
print(pygame.font.get_fonts())
font = pygame.font.Font('freesansbold.ttf',24)

button3 = Button('USA',75,40,(528,25),5)
button2 = Button('Brazil',75,40,(528,75),5)
button1 = Button('Finland',75,40,(528,125),5)

s = 'sounds'


# bass = pygame.mixer.Sound(os.path.join(s, 'kick-bass.mp3'))
# snare = pygame.mixer.Sound(os.path.join(s, 'snare.mp3'))
# tom1 = pygame.mixer.Sound(os.path.join(s, 'tom-1.mp3'))
# tom2 = pygame.mixer.Sound(os.path.join(s, 'tom-2.mp3'))



# ValueColor = {
#   'purple': (128, 0, 128),
#   'silver': (192, 192, 192),
#   'gray': (128, 128, 128),
#   'Red': (255, 0, 0),
#   'Maroon': (128, 0, 0),
#   'yellow': (255, 255, 0),
#   'olive': (128, 128, 74),
#   'lime': (0, 255, 0),
#   'Green': (0, 128, 0),
#   'Aqua': (0, 255, 255),
#   'teal': (0, 128, 128),
#   'blue': (0, 0, 255),
# }
GameColor = {
    0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)
          }

GameColor_USA = {
      0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
  'light text': (255, 255, 255),
  'dark text': (10, 49, 97),
  'other': (0,0,0),
  'bg': (179, 25, 66),
}
GameColor_Brazil = {
      0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
  'light text': (254, 221, 0),
  'dark text': (1, 33, 105),
  'other': (254, 221, 0),
  'bg': (0, 151, 57),
}

GameColor_Finland = {
      0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
  'light text': (255, 255, 255),
  'dark text': (0, 47, 108),
  'other': (0, 0, 0),
  'bg': (0, 47, 108),
}

#List of values for board
tile_vals = [[0 for _ in range(4)] for _ in range(4)]

game_over = False

spawn_pieces = True

init_count = 0

direction = ''
buttons = []

score = 0

def draw_over():
    pygame.draw.rect(display, 'black', [50, 50, 300, 100], 0, 10)
    game_over_text1 = font.render('Game Over!', True, 'white')
    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
    display.blit(game_over_text1, (130, 65))
    display.blit(game_over_text2, (70, 105))

def getcolor(i):
  return GameColor[i]


#function that takes turn for user 
def take_turn(direc, board):
    global score
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direc == 'UP':
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        board[i - shift][j] = board[i][j]
                        board[i][j] = 0
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift][j] \
                            and not merged[i - shift - 1][j]:
                        board[i - shift - 1][j] *= 2
                        score += board[i - shift - 1][j]
                        board[i - shift][j] = 0
                        merged[i - shift - 1][j] = True
    elif direc == 'DOWN':
      for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board[3 - q][j] == 0:
                        shift += 1
                if shift > 0:
                    board[2 - i + shift][j] = board[2 - i][j]
                    board[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board[2 - i + shift][j] == board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                            and not merged[2 - i + shift][j]:
                        board[3 - i + shift][j] *= 2
                        score += board[3 - i + shift][j]
                        board[2 - i + shift][j] = 0
                        merged[3 - i + shift][j] = True
    elif direc == 'LEFT':
      for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][j - shift] = board[i][j]
                    board[i][j] = 0
                if board[i][j - shift] == board[i][j - shift - 1] and not merged[i][j - shift - 1] \
                        and not merged[i][j - shift]:
                    board[i][j - shift - 1] *= 2
                    score += board[i][j - shift - 1]
                    board[i][j - shift] = 0
                    merged[i][j - shift - 1] = True
    else:
      for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][3 - q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][3 - j + shift] = board[i][3 - j]
                    board[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if board[i][4 - j + shift] == board[i][3 - j + shift] and not merged[i][4 - j + shift] \
                            and not merged[i][3 - j + shift]:
                        board[i][4 - j + shift] *= 2
                        score += board[i][4 - j + shift]
                        board[i][3 - j + shift] = 0
                        merged[i][4 - j + shift] = True

    return board
  
#random pieces drop
def new_pieces(board):
    count = 0
    full = False
    while any(0 in row for row in board) and count < 1:
      row = random.randint(0,3)
      col = random.randint(0,3)
      if board[row][col] == 0:
        count+=1
        if random.randint(1,10) == 10:
          board[row][col] = 4
        else:
          board[row][col] = 2
    if count < 1:
      full = True
    return board , full

def drawBoard():
  pygame.draw.rect(display, GameColor['bg'], [125, 25, 400, 400], 0, 10)
  score_text = font.render(f'Your Score: {score}', True, GameColor['light text'])
  display.blit(score_text, (250, 425))
  pass


def drawTiles(tile_val):
  for row in range(4):
    for col in range(4):
      value = tile_val[row][col]
      if value > 8:
        text_color = GameColor['light text']
      else:
        text_color = GameColor['dark text']
      if value <= 2048:
        ValueColor = GameColor[value]
      else:
        ValueColor = GameColor['other']
      pygame.draw.rect(display, ValueColor, [95 * col + 145, 45 + row * 95, 75, 75], 0, 5)
      if value > 0:
        val_len = len(str(value))
        font = pygame.font.Font('freesansbold.ttf',48 - (5 * val_len))
        val_num = font.render(str(value),True,text_color)
        text_box = val_num.get_rect(center=(col*95+182,row*95 + 82))
        display.blit(val_num, text_box)
        pygame.draw.rect(display, 'black', [95 * col + 145, 45 + row * 95, 75, 75], 2, 5)


while True:
  timer.tick(fps)
  display.fill('tan')
  drawBoard()
  drawTiles(tile_vals)
  button3.draw()
  button2.draw()
  button1.draw()
  if button1.pressed:
      GameColor = GameColor_Finland
  elif button2.pressed:
      GameColor = GameColor_Brazil
  elif button3.pressed:
      GameColor = GameColor_USA
  else:
      pass

  if spawn_pieces or init_count < 2:
    tile_vals, game_over = new_pieces(tile_vals)
    spawn_pieces = False
    init_count += 1
  if direction != '':
    tile_vals = take_turn (direction, tile_vals)
    direction = ''
    spawn_pieces = True 
  if game_over:
    draw_over()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
      sys.exit()
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        direction = 'UP'
        mixer.music.load('crash.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
        #Play the music
        mixer.music.play()
      elif event.key == pygame.K_DOWN:
        direction = 'DOWN'
        mixer.music.load('snare.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
        #Play the music
        mixer.music.play()
      elif event.key == pygame.K_LEFT:
        direction = 'LEFT'
        mixer.music.load('tom-1.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
        #Play the music
        mixer.music.play()
      elif event.key == pygame.K_RIGHT:
        direction = 'RIGHT'
        mixer.music.load('tom-2.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
        #Play the music
        mixer.music.play()
      elif event.key == pygame.K_SPACE:
        mixer.music.load('kick-bass.mp3')
        #Set preferred volume
        mixer.music.set_volume(0.2)
        #Play the music
        mixer.music.play()
      
      if game_over:
                if event.key == pygame.K_RETURN:
                    board_values = [[0 for _ in range(4)] for _ in range(4)]
                    spawn_new = True
                    init_count = 0
                    score = 0
                    direction = ''
                    game_over = False

  pygame.display.update()

  # backgroundpic=pygame.image.load("apps.41595.9007199266246951.602b9e5c-10c7-4f4a-80e2-b4e598790c74.png")
  # font= pygame.font.SysFont("monospace",40)
  # fontofscore = pygame.font.SysFont("monospace",30)

#That guys logic
