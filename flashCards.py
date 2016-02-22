#! python3
# flashCards.py - A program designed to help you learn the two Japanses
#                 alphabets Hiragana & Katakana by the help of flash cards.

import os, logging

#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def getCharPath(folder = None, hiragana = True):

  path = 'Katakana'
  if hiragana:
    path = 'Hiragana'
  if folder != None:
    path = os.path.join(path,folder)

  characters = []

  for folderName, subfolders, filenames in os.walk(path):
    logging.debug('The current folder is ' + folderName)

    for filename in filenames:
      logging.debug('FILE INSIDE ' + folderName + ': ' + filename)
      characters.append(os.path.join(folderName,filename))

    logging.debug('')
  return characters

characters = getCharPath('Empty',False)
logging.debug(characters)
logging.debug('End of program')
