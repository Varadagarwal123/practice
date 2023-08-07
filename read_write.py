#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_database_from_file():
    database = {}
    with open("student_database.txt", 'r') as file:
            file_content = file.read()
    if file_content:
            database = eval(file_content)  
    return database
def save_database_to_file(database):
    with open('student_database.txt', 'w') as file:
        file.write(str(database))

