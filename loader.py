from database import Database
from parser import Parser
from json import dumps


'''
    CREATING A CONNECTION TO THE DATABASE
    BY DEFAULT, EACH TIME THE SCRIPT RUNS,
    IT RESTARTS THE DATA INSIDE IT
'''
db = Database(build=True)


'''
    CREATE PARSER, RUNS DIGESTIONS AND RETURNS DATA
'''
ps = Parser()
ps.process()
data = ps.get()


'''
    ADDING FILES DATA INSIDE THE DATABASE
'''
for f in data['files'] :
    db.addTags( f['file'], [f['tag']] )


'''
    ADDING FLASHCARDS DATA INSIDE THE DATABASE
'''
for f in data['flashcards'] :
    db.addFlashcard(
        f['question'],
        f['answer'],
        f['tags']
    )


'''
    ADDING MULTIPLE CHOICES DATA INSIDE THE DATABASE
'''
for m in data['multiples'] :
    db.addMultiple(
        m['question'],
        m['correct'],
        m['q1'],
        m['q2'],
        m['q3'],
        m['q4'],
        m['q5'],
        m['tags']
    )


'''
    SHOWING FINAL DATABASE CONTENT
'''
db.showPopulation()