import streamlit as st
st.set_page_config(
    page_title='House Data EDA',
    layout='wide'
)

#st.snow()




import pandas as pd
import sqlite3
conn = sqlite3.connect( 'knowledge_database.db' )




def getTotalFiles() :
    cursor = conn.cursor()
    result = cursor.execute('select count(distinct file) from tag').fetchall()
    return result[0][0]

def getTotalFlashcards() :
    cursor = conn.cursor()
    result = cursor.execute('select count(question) from flashcard').fetchall()
    return result[0][0]

def getTotalMultiple() :
    cursor = conn.cursor()
    result = cursor.execute('select count(question) from multiple').fetchall()
    return result[0][0]


def getFiles() :
    cursor = conn.cursor()
    result = cursor.execute('select distinct file from tag').fetchall()
    return result

def getFileTags( fileName ) :
    cursor = conn.cursor()
    result = cursor.execute(f'select tag from tag where file=\'{fileName}\'').fetchall()
    return result

def getFlashcard() :
    cursor = conn.cursor()
    result = cursor.execute('select * from flashcard').fetchall()
    return result

def getFlashcardTags(id) :
    query = f'''
        select tag
        from flashcardtag
        where flashcard_id={id}
    '''
    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()
    return result

def getMultiple() :
    cursor = conn.cursor()
    result = cursor.execute('select * from multiple').fetchall()
    return result

def getMultipleTags(id) :
    query = f'''
        select tag
        from multipletag
        where multiple_id={id}
    '''
    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()
    return result




menuChoice = st.sidebar.selectbox(
    'Main page',
    ['Main', 'Files', 'Flashcards', 'Multiple Choices']
)


if menuChoice == 'Main' :
    c1, c2, c3 = st.columns(3)
    with c1 :
        st.metric(
            label = 'Total Tagged Files',
            value = getTotalFiles()
        )
    with c2 :
        st.metric(
            label = 'Total Flashcards',
            value = getTotalFlashcards()
        )
    with c3 :
        st.metric(
            label = 'Total Multiple Choice',
            value = getTotalMultiple()
        )

elif menuChoice == 'Files' :
    '''# Files'''

    for item in getFiles() :
        f'''## {item[0]}'''

        tags = [ it[0] for it in getFileTags(item[0]) ]
        if len(tags) :
            tags.sort()

            t = pd.DataFrame.from_dict({'tags':tags}) 
            '''#### Tags'''
            st.dataframe(t)

elif menuChoice == 'Flashcards' :
    '''# Flashcards'''

    for item in getFlashcard() :
        f'''## {item[0]}. {item[1]}'''
        st.info(item[2])

        tags = [ it[0] for it in getFlashcardTags(item[0]) ]
        if len(tags) :
            tags.sort()

            t = pd.DataFrame.from_dict({'tags':tags}) 
            '''#### Tags'''
            st.dataframe(t)

elif menuChoice == 'Multiple Choices' :
    '''# Multiple Questions'''

    for item in getMultiple() :

        f'''## {item[0]}. {item[1]}'''
        st.success(item[2])
        for i in range(3, 8) :
            if item[i] :
                st.error( item[i] )
        
        tags = [ it[0] for it in getMultipleTags(item[0]) ]
        if len(tags) :
            tags.sort()

            t = pd.DataFrame.from_dict({'tags':tags})
            '''#### Tags'''
            st.dataframe(t)