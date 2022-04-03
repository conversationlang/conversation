#Start me off
lines = str(__import__('sys').argv[1])

#Lets make this thing!
import os
import random as r
import pygame as GUI
from pygame.locals import *
import time
GUI.init()
os.system('clear')
def __():
  pass
def show_text(screen, msg, x, y, color, size=20):
  GUI.font.init()
  font = GUI.font.SysFont('monospace', size)
  text = font.render(msg, True, color)
  screen.blit(text, (x, y))
def pyg_ask(screen, question, x, y, end_to_do=__):
  up = {
    '`':'~',
    '1':'!',
    '2':'@',
    '3':'#',
    '4':'$',
    '5':'%',
    '6':'^',
    '7':'&',
    '8':'*',
    '9':'(',
    '0':')',
    '-':'_',
    '=':'+',
    '[':'{',
    ']':'}',
    '\\':'|',
    ';':':',
    "'":'"',
    ',':'<',
    '.':'>',
    '/':'?'
  }
  answer = ''
  upper = False
  breaker = False
  cursor = False
  while True:
    time.sleep(1)
    if breaker:
      end_to_do()
      GUI.window.update()
      break
    screen.fill((0, 0, 0))
    show_text(screen, question, x, y, (255, 255, 255))
    show_text(screen, answer, x, y+32, (255, 255, 255))
    if cursor:
      GUI.font.init()
      font = GUI.font.SysFont('freesans', 20)
      text = font.render('|', True, (167, 167, 167))
      screen.blit(text, (len(answer) * 12, y+32))
    GUI.window.update()
    for event in GUI.event.get():
      if event.type == QUIT:
        GUI.quit()
        exit()
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          breaker = True
        elif event.key == K_BACKSPACE:
          listed = list(answer)
          try:
            listed[-1] = ''
          except IndexError:
            pass
          answer = ''.join(listed)
        elif 'shift' in GUI.key.name(event.key):
          upper = True
        elif event.key == K_SPACE:
          answer += ' '
        elif len(GUI.key.name(event.key)) > 1:
          pass
        else:
          if upper:
            if GUI.key.name(event.key) in up:
              answer += up[GUI.key.name(event.key)]
            else:
              answer += GUI.key.name(event.key).capitalize()
            upper = False
          else:
            answer += GUI.key.name(event.key)
        screen.fill((0, 0, 0))
        show_text(screen, question, x, y, (255, 255, 255))
        show_text(screen, answer, x, y+32, (255, 255, 255))
        GUI.window.update()
    if cursor:
      cursor = False
    else:
      cursor = True
  return answer
setattr(GUI.draw, 'text', show_text)
setattr(GUI.display, 'input', pyg_ask)
setattr(GUI, 'create_window', GUI.display.set_mode)
del GUI.display.set_mode
setattr(GUI, 'set_title', GUI.display.set_caption)
del GUI.display.set_caption
setattr(GUI, 'window', GUI.display)
del GUI.display
setattr(GUI, 'sounds', GUI.mixer)
del GUI.mixer
yes = True
no = False
idk = None
opers = {
  '==':'!=',
  '>=':'<',
  '<=':'>',
  '!=':'==',
  '<':'>=',
  '>':'<=',
  'in':'not in',
  'not in':'in',
  'True':'False',
  'False':'True'
}
#Data Types
class number(int):
  def __init__(self, x):
    return x.__num__()
  def digits(self):
    return len(str(self))
  __doc__ = """
  number(x) --> x.__num__()
  Create a new number.
  Return x.__num__()
  """
sentence = type('sentence', str.__bases__, dict(str.__dict__))
decimal = type('decimal', float.__bases__, dict(float.__dict__))
letter = type('letter', str.__bases__, dict(str.__dict__))
#Nvm
if 'nevermind\n' in lines or 'nevermind' in lines:
  if lines[len(lines)-1] == 'nevermind\n' or lines[len(lines)-1] == 'nevermind':
    lines = []
  else:
    readit = lines.join('\n')
    for i in range(len(lines)):
      lines[i] = lines[i].strip()
    readit = readit.split('nevermind')
    for j in range(len(readit)-2):
      lines.remove(readit[j])
#Errors
class ConversationError(Exception):
  pass
class UnknownNameError(Exception):
  pass
class ConversationUnexpectedlyEndedError(Exception):
  pass
class UnexpectedConversationLineEndedError(Exception):
  pass
#Classes
class shell:
  def do_it(command):
    os.system(command)
class math:
  def round_to_whole(item):
    return round(item)
  def round_to_nearest(item, nearest):
    return round(item/nearest) * nearest
  def random_num(start, stop):
    return r.randint(start, stop)
class builtin_class():
  def __init__(self):
    pass
  def setInfo(self, info):
    self.__doc__ = info
  def __str__(self):
    return str(self)
setattr(builtin_class, '__vars__', dict(builtin_class.__dict__))
del builtin_class.__vars__['__module__']
del builtin_class.__vars__['__init__']
del builtin_class.__vars__['__str__']
del builtin_class.__vars__['__dict__']
del builtin_class.__vars__['__weakref__']
del builtin_class.__vars__['setInfo']
os.environ['TZ'] = 'US/Pacific'
time.tzset()
class timer:
  class ctime:
    def what_year():
      return time.ctime(time.time())[-4:]
    def what_curr_seconds():
      return time.ctime(time.time())[17:19]
    def what_curr_hour():
      return time.ctime(time.time())[15:16]
    def what_curr_mins():
      return time.ctime(time.time())[14:16]
    def what_day_num():
      return time.ctime(time.time())[9:10]
    def what_month():
      return time.ctime(time.time())[5:9]
    def what_day():
      return time.ctime(time.time())[:2]
  class others:
    wait = time.sleep
#Functions
def say(str='', end='\n'):
  print(str, end=end)
def ask(str):
  return input(str)
def file(the_file, mode='r'):
  return open(the_file, mode)
def do_it(source):
  exec(source)
def bye():
  exit()
def info(item):
  print(item.__doc__)
def num_items(obj):
  return len(obj)
def get_parity(item):
  if item % 2 == 0:
    return 'even'
  else:
    return 'odd'
def from_to(fromm, to, step=1):
  return range(fromm, to, step)
def what_type(item):
  if type(item) == str:
    if len(item) == 1:
      return letter
    else:
      return sentence
  elif type(item) == int:
    return number
  elif type(item) == float:
    return decimal
  else:
    return type(item)
#Keywords
for i in range(0, len(lines)):
  if 'whisp' in lines[i]:
    lines[i] = lines[i].replace('whisp ', '#')
  if ' be ' in lines[i]:
    lines[i] = lines[i].replace(' be ', ' = ')
  if 'let ' in lines[i]:
    lines[i] = lines[i].replace('let ', '')
  if 'commands ' in lines[i]:
    lines[i] = lines[i].replace('commands ', 'def ')
  if '{' in lines[i] and ('def' in lines[i] or 'move' in lines[i] or 'until' in lines[i] or 'if' in lines[i] or 'else' in lines[i] or 'topic' in lines[i]):
    lines[i] = lines[i].replace('{', ':')
  if 'topic ' in lines[i]:
    lines[i] = lines[i].replace('topic', 'class')
  if 'until ' in lines[i]:
    lines[i] = lines[i].replace('until', 'while')
    lines_i = lines[i].split()
    for j in lines_i:
      if j in opers:
        lines[i] = lines[i].replace(j, opers[j])
      else:
        pass
  if 'move ' in lines[i]:
    lines[i] = lines[i].replace('move', 'for')
    if ' through ' in lines[i]:
      lines[i] = lines[i].replace('through', 'in')
  if '--' in lines[i]:
    lines[i] = lines[i].replace('--', '-= 1')
  if '++' in lines[i]:
    lines[i] = lines[i].replace('++', '+= 1')
  if '}' == lines[i].strip():
    lines[i] = '\n'
  if '`s ' in lines[i]:
    lines[i] = lines[i].replace('`s ', '.')


#And finish it
allread = ''.join(lines)
try:
  exec(allread)
except SyntaxError as s:
  if 'EOF' in str(s):
    raise ConversationUnexpectedlyEndedError('Conversation Abruptly Ended')
  elif 'EOL' in str(s):
    raise UnexpectedConversationLineEndedError('Conversation Line Unexpectedly Ended')
  else:
    raise ConversationError(str(s))
except NameError as n:
  raise UnknownNameError(str(n)[5:-15] + ' was never defined')
