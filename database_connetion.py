import pymysql
# pip3 install pymysql

def get_connection():

    connection = pymysql.connect(host = 'localhost', user='root', password='Admin@123', database='project_management')
    return connection


def accept(id, name, team_members,technology, deadline):

    connection = get_connection()
    cursor  = connection.cursor()
    query = '''insert into projectinfo values ({},\'{}\',\'{}\',\'{}\',\'{}\');'''.format(id, name, team_members, technology,deadline)
    cursor.execute(query)
    connection.commit()
    print("Record Added Successfully")


# accept(2, "Video proctoring", "Abhijeet", "C#", "March 2023")

def display():
    connection = get_connection()
    cursor = connection.cursor()
    query = '''select * from projectinfo;'''
    cursor.execute(query)
    data = cursor.fetchall()
    for i in data:
        print(i)


def search(project_name):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''select * from projectinfo where name = \'{}\''''.format(project_name)
    cursor.execute(query)
    data = cursor.fetchone()
    print(data)

# search("Video proctoring")

def update(id, name, team_members,technology, deadline):

    connection = get_connection()
    cursor = connection.cursor()
    query = '''update projectinfo set name = \'{}\', members= \'{}\', technologies_used = \'{}\',
    deadline = \'{}\' where projectid = {};'''.format(name, team_members, technology, deadline, id)
    cursor.execute(query)
    connection.commit()

# update(2, "Video proctoring", "Smita", "React Native", "DEC 2023")


def delete(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = '''delete from projectinfo where projectid = {}'''.format(id)
    cursor.execute(query)
    connection.commit()


delete(2)


