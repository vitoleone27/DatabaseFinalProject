from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode


def connectToMySQL():
    cnx = mysql.connector.connect(password='project', user='project')
    cursor = cnx.cursor()
    return cursor, cnx


def createDatabase(cursor, DB_NAME):
    '''
    :param cursor: instance of the connection to the database
    :param DB_NAME: name of the database to create
    Creates the database at cursor with the given name.
    '''
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def createQueries():
    queries = {}
    questionsFile = open("questions.txt", "r")
    queryFile = open("queries.sql", "r")
    for question in questionsFile:
        question = question.strip()
        query = queryFile.readline()
        query = query.strip()
        data = question.split(',')
        queries[data[0]] = [question[2:], query]
    questionsFile.close()
    queryFile.close()
    return queries


def questionA(cursor, queries):
    question = 'a'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    i = 1
    while result is not None:
        print(i, result[0], sep=') ')
        result = cursor.fetchone()
        i += 1
    print()

def questionB(cursor, queries):
    question = 'b'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    i = 1
    while result is not None:
        print(i, result[0], sep=') ')
        result = cursor.fetchone()
        i += 1
    print()


def questionC(cursor, queries):
    question = 'c'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    i = 1
    while result is not None:
        print(i.__str__() + ") " + result[0], result[1], sep=" || ")
        result = cursor.fetchone()
        i += 1
    print()


def questionD(cursor, queries):
    question = 'd'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    i = 1
    while result is not None:
        print(i, result[0], sep=') ')
        result = cursor.fetchone()
        i += 1
    print()


def questionE(cursor, queries):
    question = 'e'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    i = 1
    while result is not None:
        print(i.__str__() + ") " + result[0], result[1], sep=" || ")
        result = cursor.fetchone()
        i += 1
    print()


def questionF(cursor, queries):
    question = 'f'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    i = 1
    while result is not None:
        print(i.__str__() + ") " + result[0], result[1], sep=" || ")
        result = cursor.fetchone()
        i += 1
    print()


def questionG(cursor, queries):
    question = 'g'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    i =1
    while result is not None:
        print(i, result[0], sep= ") ")
        result = cursor.fetchone()
        i += 1
    print()


def questionH(cursor, queries):
    question = 'h'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    while result is not None:
        print(result[0])
        result = cursor.fetchone()
    print()


def questionI(cursor, queries):
    question = 'i'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1], multi=True)
    result = cursor.fetchone()
    while result is not None:
        print(result[0], result[1], sep=" || ")
        result = cursor.fetchone()
    print()


def questionJ(cursor, queries):
    question = 'j'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1], multi=True)
    result = cursor.fetchone()
    i = 1
    while result is not None:
        print(i, result[0], sep=') ')
        result = cursor.fetchone()
        i += 1
    print()


def questionK(cursor, queries):
    question = 'k'
    print(question, queries[question][0], sep='. ')
    print("____________________________________________________________________________________________________")
    cursor.execute(queries[question][1], multi=True)
    result = cursor.fetchone()
    i = 1
    while result is not None:
        print(i.__str__() + ") " + result[0], result[1], sep=" || ")
        result = cursor.fetchone()
        i += 1
    print()


def showAnswer(choice, cursor, queries):
    if choice == 'a':
        questionA(cursor, queries)
    elif choice == 'b':
        questionB(cursor, queries)
    elif choice == 'c':
        questionC(cursor, queries)
    elif choice == 'd':
        questionD(cursor, queries)
    elif choice == 'e':
        questionE(cursor, queries)
    elif choice == 'f':
        questionF(cursor, queries)
    elif choice == 'g':
        questionG(cursor, queries)
    elif choice == 'h':
        questionH(cursor, queries)
    elif choice == 'i':
        questionI(cursor, queries)
    elif choice == 'j':
        questionJ(cursor, queries)
    elif choice == 'k':
        questionK(cursor, queries)
    else:
        print("Not an option, enter again")


def main():
    DB_NAME = 'FinalProject'
    cursor, connection = connectToMySQL()

    sql = "DROP DATABASE IF EXISTS FinalProject"
    cursor.execute(sql)

    createDatabase(cursor, DB_NAME)  # data base already exists so no need to create it
    cursor.execute("USE {}".format(DB_NAME))

    # Now create the pet table data into table

    with open('create.sql', 'r') as f:
        for line in f:
            sql = line
            sql.strip()
            cursor.execute(sql)

    queries = createQueries()

    choice = ""
    questionsFile = open("questions.txt", "r")
    for question in questionsFile:
        question = question.strip()
        print(question)

    while choice != "quit":
        questionsFile = open("questions.txt", "r")
        choice = input("Which question would you like answered? Enter \"questions\""
                       + " to see the list of possible questions. Enter \"quit\" to exit: ")
        choice = choice.lower()
        if choice == "questions":
            for question in questionsFile:
                question = question.strip()
                print(question)
        if choice != "quit" and choice != "questions":
            showAnswer(choice, cursor, queries)

    print("Thank you!")
    # Print table
    # result = cursor.fetchall()
    # for row in result:
    #  print(row)

    # don't modify below this line

    connection.commit()
    cursor.close()
    connection.close()


main()
