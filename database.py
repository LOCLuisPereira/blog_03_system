'''
DATABASE
    __init__
        INITIAL DATABASE SETUP
        CREATE DATABASE CONNECTION
        IF BUILD IF SET TRUE, DELETE TABLE IF THEY EXIST
        CREATE TABLES
    executeQuery
        EXECTURE QUERY
        IF SUCCESS, RETURNS THE RESULT OF THE QUERY
        OTHERWISE PRINTS THE ERROR
    showPopulation
        LISTS ALL THE ITEMS INSIDE THE DATABASE
    fakePopulation
        CREATES FAKE ITEMS FOR TESTING THE DATABASE
        BOTH BY USING QUERY AND CLASS CUSTOM METHOD
    createTableTag
        CREATES TAG TABLE
        TABLE WITH A ID, NAME OF FILE AND ONE TAG
        THE GOAL IS TO HAVE MULTIPLE TAGS
        CHOSE TO USE MULTIPLE ROWS, INSTEAD OF A LIST
    createTableFlashcard
        CREATES FLASHCARD TABLE
        TABLE WITH A ID, QUESTION AND ANSWER
    createTableMultipleChoice
        CREATES MULTIPLE TABLE
        TABLE WITH A ID, QUESTION, CORRECT ANSWER AND MULTIPLE OPTIONAL OPTIONS
    createTableFlashcardTag
        CREATES TABLE FOR FLASHCARDTAG
        THIS ALLOWS A MULTITAGGING SYSTEM
    createTableMultipleTag
        CREATES TABLE FOR MULTITAGS
        THIS ALLOW A MULTITAGGING SYSTEM
    dropTableTag
        DELETES TABLE TAG IF IT EXISTS
    dropTableFlashcard
        DELETES TABLE FLASHCARD IF IT EXISTS
    dropTableMultipleChoice
        DELETES TABLE MULTIPLE IF IT EXISTS
    dropTableFlashcardTag
        DROPS FLASHCARDTAG TABLE
    dropTableMultipleTag
        DROPS MULTIPLETAG TABLE
    addTag
        INSERT VALUE INSIDE TAG
        REQUIRES FILE NAME AND TAG STRING
    addFlashcard
        INSERT VLAUE INSIDE FLASHCARD TABLE
        REQUIRES QUESTION AND ANSWER
        ADDS MULTIPLE TAGS ON THE FLASHCARDTAG TABLE
    addMultiple
        INSERT MULTIPLE CHOICE INSIDE MULTIPLE TABLE
        REQUIRES QUESTION AND CORRECT ANSWER
        AFTER ANSWER, ALL THE OPTIONS ARE OPTIONAL
        MAX NUMBER OF OPITIONAL CHOICES ARE 5
        ADDS MULTIPLE TAGS ON THE MULTIPLETAG TABLE
'''
import sqlite3
from sqlite3 import Error
import os


class Database :
    def __init__( self, build=True, name='knowledge_database.db' ) :
        self.conn = sqlite3.connect( name )

        if build:
            self.dropTableTag()
            self.dropTableFlashcard()
            self.dropTableMultipleChoice()
            self.dropTableFlashcardTag()
            self.dropTableMultipleTag()

            self.createTableTag()
            self.createTableFlashcard()
            self.createTableMultipleChoice()
            self.createTableFlashcardTag()
            self.createTableMultipleTag()

    def executeQuery( self, query ) :
        try :
            cursor = self.conn.cursor()
            if query.startswith( 'select' ) :
                return cursor.execute( query ).fetchall()
            cursor.execute( query )
            self.conn.commit()
            return id
        except Error as e :
            print( e )

    ''' AUX '''
    def showPopulation( self ) :
        print( '== Tag Table ==' )
        for rowTag in self.executeQuery( 'select * from tag' ) :
            print( rowTag )

        print( '== Flashcard Table ==' )
        for rowFlash in self.executeQuery( 'select * from flashcard' ) :
            print( rowFlash )

        print( '== Flashcard Tag Table ==' )
        for rowFlash in self.executeQuery( 'select * from flashcardtag' ) :
            print( rowFlash )

        print( '== Multiple Table ==' )
        for rowMultiple in self.executeQuery( 'select * from multiple' ) :
            print( rowMultiple )

        print( '== Multiple Tag Table ==' )
        for rowMultiple in self.executeQuery( 'select * from multipletag' ) :
            print( rowMultiple )

    def fakePopulation( self ) :
        self.executeQuery(
            '''
                insert into tag (file, tag)
                values('test.md', 'programming')
            '''
        )
        self.executeQuery(
            '''
                insert into flashcard (question, answer)
                values('Are you enjoying SQLite?', 'yes')
            '''
        )
        self.executeQuery(
            '''
                insert into multiple (question, correct, option1, option2)
                values('SQLite is?', 'awesome', 'bad', 'it sucks...')
            '''
        )
        self.addTags('here.md', ['testing', 'omg'])
        self.addFlashcard('Almost finish?', 'Only db interface')
        self.addFlashcard('Almost finish this tagging system?', 'Only db interface', tags=['something', 'in', 'here'])
        self.addMultiple('Almost finish?', 'Only db interface', 'here1')
        #self.addMultiple('Almost finish?', 'Only db interface', 'here1', 'here2')
        #self.addMultiple('Almost finish?', 'Only db interface', 'here1', 'here2', 'here3')
        #self.addMultiple('Almost finish?', 'Only db interface', 'here1', 'here2', 'here3', 'here4')
        #self.addMultiple('Almost finish?', 'Only db interface', 'here1', 'here2', 'here3', 'here4', 'here5')
        self.addMultiple('Almost finish tagging?', 'Only db interface', 'here1', tags=['question', 'what'])

    ''' CREATE '''
    def createTableTag( self ) :
        query = '''
            create table tag (
                id integer primary key,
                file text not null,
                tag text not null
            )
        '''
        return self.executeQuery( query )

    def createTableFlashcard( self ) :
        query = '''
            create table flashcard (
                id integer primary key,
                question text not null,
                answer text not null
            )
        '''
        self.executeQuery( query )

    def createTableMultipleChoice( self ) :
        query = '''
            create table multiple (
                id integer primary key,
                question text not null,
                correct text not null,
                option1 text,
                option2 text,
                option3 text,
                option4 text,
                option5 text
            )
        '''
        self.executeQuery( query )

    def createTableFlashcardTag( self ) :
        query = '''
            create table flashcardtag (
                id integer primary key,
                flashcard_id int not null,
                tag text not null
            )
        '''
        return self.executeQuery( query )

    def createTableMultipleTag( self ) :
        query = '''
            create table multipletag (
                id integer primary key,
                multiple_id int not null,
                tag text not null
            )
        '''
        return self.executeQuery( query )

    ''' DROP '''
    def dropTableTag( self ) :
        query = '''
            drop table if exists tag
        '''
        self.executeQuery( query )

    def dropTableFlashcard( self ) :
        query = '''
            drop table if exists flashcard
        '''
        self.executeQuery( query )

    def dropTableMultipleChoice( self ) :
        query = '''
            drop table if exists multiple
        '''
        self.executeQuery( query )

    def dropTableFlashcardTag( self ) :
        query = '''
            drop table if exists flashcardtag
        '''
        self.executeQuery( query )

    def dropTableMultipleTag( self ) :
        query = '''
            drop table if exists multipletag
        '''
        self.executeQuery( query )

    ''' INSERT '''
    def addTags( self, file, tags ) :
        for tag in tags :
            self.executeQuery(
                f'insert into tag (file, tag) values (\'{file}\',\'{tag}\')'
            )

    def addFlashcard( self, question, answer, tags=[] ) :
        self.executeQuery(
            f'insert into flashcard (question, answer) values (\'{question}\',\'{answer}\')'
        )

        x = self.executeQuery(f'select * from flashcard where question=\'{question}\'')
        for x in x :
            for tag in tags :
                self.executeQuery(f'insert into flashcardtag (flashcard_id, tag) values (\'{x[0]}\',\'{tag}\')')

    def addMultiple(
        self, question, correct, option1='None', option2='None',
        option3='None', option4='None', option5='None', tags=[] ) :
        self.executeQuery(
            f'''
                insert into multiple (question, correct, option1, option2, option3, option4, option5)
                values (\'{question}\', \'{correct}\', \'{option1}\', \'{option2}\', \'{option3}\', \'{option4}\', \'{option5}\')
            '''
        )

        x = self.executeQuery(f'select * from multiple where question=\'{question}\'')
        for x in x :
            for tag in tags :
                self.executeQuery(f'insert into multipletag (multiple_id, tag) values (\'{x[0]}\',\'{tag}\')')


if __name__ == '__main__' :
    ''' REBUILD '''
    db = Database( build=True )
    ''' LOAD DB STATE '''
    # db = Database( build=False )
    ''' POPULATE '''
    db.fakePopulation()
    ''' SHOW POPULATION '''
    db.showPopulation()