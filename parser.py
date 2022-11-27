'''
PARSER
  __init__
    DEFINE PATHS FOR FOLDER
    INITIALIZE INTERNAL VARIABLES FOR HOLDING INFORMATION
  parseFiles
    PARSES THROUGH ALL THE FILES INSIDE THE RESPECTIVE FILES
  parseFlashcards
    PARSES THROUGH ALL THE FLASHCARDS INSIDE THE RESPECTIVE FOLDER
  parseMultiples
    PARSES THROUGH ALL THE MULTIPLE CHOICES INSIDE THE FILES MULTIPLE CHOICES
  showInfo
    CHECK ALL THE INFORMATION THAT HAS BEEN DIGESTED INSIDE THE PARSER
  process
    TRIGGER THE PARSER TO PARSE ALL THE INFORMATION INSIDE THE FOLDERS
  get
    RETURNS THE INTERNAL STATE OF THE PARSER AS A DICITIONARY WITH
    FILES, FLASHCARDS AND MULTIPLE CHOICES

MAIN
'''
from json import dumps
import os


class Parser :
  def __init__( self, folder='Second_Brain' ) :
    self.folder_files = f'{folder}/Files'
    self.folder_flashcards = f'{folder}/Flashcards'
    self.folder_multiples = f'{folder}/Multiple_choices'

    self.files = []
    self.flashcards = []
    self.multiples = []


  def parseFiles( self ) :
    for f in os.listdir(self.folder_files) :
      with open( f'{self.folder_files}/{f}' , 'r') as handler :
      
        for line in handler :
          for word in line.split( ' ' ) :
            if word[0] == '#' :
              if len(word) > 1 :
                self.files.append(
                  {
                    'file' : f,
                    'tag' : word[1:].strip()
                  }
                )


  def parseFlashcards( self ) :
    for f in os.listdir( self.folder_flashcards ) :
      with open( f'{self.folder_flashcards}/{f}' , 'r') as handler :
          lines = handler.readlines() + ['\n']
          for x, y, z in zip(lines, lines[1:], lines[2:]) :
            if '- Q:' not in x and '- A:' not in y : continue

            question = x.strip('- Q: ').strip('\n')
            answer = y.strip('- A: ').strip('\n')
            if '- T:' in z :
              tags = [ tag.strip() for tag in z.strip('- T: ').split(',') ]
            else :
              tags = []

            self.flashcards.append({
              'question' : question,
              'answer' : answer,
              'tags' : tags
            })


  def parseMultiples( self ) :
    for f in os.listdir( self.folder_multiples ) :
      with open( f'{self.folder_multiples}/{f}' , 'r') as handler :
        lines = handler.readlines()
        for i, line in enumerate( lines ) :
          if '- Q: ' in line :
            question = line.strip('- Q: ').strip('\n')
            correct = lines[i+1].strip('- C: ').strip('\n')
            q1 = lines[i+2].strip('- A1: ').strip('\n')
            q2 = lines[i+3].strip('- A2: ').strip('\n')
            q3 = lines[i+4].strip('- A3: ').strip('\n')
            q4 = lines[i+5].strip('- A4: ').strip('\n')
            q5 = lines[i+6].strip('- A5: ').strip('\n')
            tags = [ tag.strip() for tag in lines[i+7].strip('- T: ').split(',') ]

            self.multiples.append({
              'question' : question,
              'correct' : correct,
              'q1' : q1,
              'q2' : q2,
              'q3' : q3,
              'q4' : q4,
              'q5' : q5,
              'tags' : tags
            })


  def showInfo( self ) :
    print( '==== Files ====' )
    print( dumps( self.files, indent=2 ) )
    print( '==== Flashcards ====' )
    print( dumps( self.flashcards, indent=2 ) )
    print( '==== Questions ====' )
    print( dumps( self.multiples, indent=2 ) )


  def process( self ) :
    self.parseFiles()
    self.parseFlashcards()
    self.parseMultiples()


  def get( self ) :
    return {
      'files' : self.files,
      'flashcards' : self.flashcards,
      'multiples' : self.multiples
    }


if __name__ == '__main__' :
  ps = Parser()
  ps.process()
  print( dumps( ps.get(), indent=2 ) )