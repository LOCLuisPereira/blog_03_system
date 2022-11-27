# blog_03_system

# Parsing Structure.
At the present time, the parser is very trivial and requires a very strict structure.
Multiple items can be insert inside the same file for flashcards and multiple choice questions.

## Files.
Parses any obsidian tag.
In obsidian a tag consists on a string that has # as a prefix.
Example, #this #is #a #set #of #tags.

## Flashcards.
- Q: [QUESTION]
- A: [ANSWER]
- T: [LIST OF TAGS USING COMMA (,) AS SEPARATOR

## MULTIPLE CHOICE QUESTIONS
- Q: [QUESTION]
- C: [CORRECT ANSWER]
- Q1: [OPTIONAL STRING]
- Q2: [OPTIONAL STRING]
- Q3: [OPTIONAL STRING]
- Q4: [OPTIONAL STRING]
- Q5: [OPTIONAL STRING]
- T: [LIST OF TAGS USING COMMA (,) AS SEPARATOR

# Done
- Database
    - Created database class.
    - Supports.
        - Create tables.
        - Drop tables.
        - Inserting.
        - Fake population.
        - Showing what is inside database.
        - Function to run queries.
- Parsing.
    - Process files.
        - **Remember**: hard required structure.
- Loading.
    - Run the parser and load data inside the database.
    
# Doing

# ToDo
- Database.
  - Selecting from tables.
  - Searching.
  - Searching with tag.
