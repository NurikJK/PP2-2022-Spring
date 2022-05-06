import psycopg2
from config import params
import csv

start = False

# Functions
def start():
    start = True

def act(commands):
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(commands)
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    if config is not None:
        config.close()
    if config is not None:
        config.close()

# To add contacts
def phonenumber(name, num):
    commands = (
        f'''
            INSERT INTO accounts(username, tell)
            VALUES('{name}', '{num}');
        '''
    )
    act(commands)

    file = open('data.csv', 'a' ,newline="")
    sbor = (name, num)
    writer = csv.writer(file)
    writer.writerow(sbor)
    file.close() 

# To delete contacts
def deletenumber(name):
    commands = (
        f"""
        DELETE FROM accounts WHERE accounts.username = '{name}';
        """
    )
    act(commands)

# To edit contacts
# update number 
def updatenumber(name, num):
    commands = (
        f"""
        UPDATE accounts SET tell = '{num}' WHERE username = '{name}';
        """
        )
    act(commands)

# update name
def updatename(name, num):
    commands = (
        f"""
        UPDATE accounts SET username = '{name}' WHERE tell = '{num}';
        """
        )
    act(commands)


def showcontacts(f):
    commands = [
        """
        SELECT * FROM accounts;
        """,
        """
        SELECT * FROM accounts
        ORDER BY username;
        """,
        """
        SELECT * FROM accounts
        ORDER BY tell;
        """
        ]
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(commands[f])
        print(current.fetchall(), '\n')
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    if config is not None:
        config.close()

#
start()
while start:
    inp = input('Press\nA - add contact\nD - delete contacts\nE - edit contacts\nQ - quit\nS - show contacts\nYour request: ')
    if inp == 'A':
        name = str(input('Name:\n'))
        num = str(input('Number:\n'))
        try:
            phonenumber(name, num)
            print("Complete\n")
        except:
            print("Error")
            break
    elif inp == 'D':
        name = str((input('Name:\n')))
        try:
            deletenumber(name)
            print("Complete\n")
        except:
            print("Error")
            break
    elif inp == 'E':
        flag = int(input('1 - Change name, 2 - Change number\n'))
        try:
            if flag == 1:
                num = str(input('Number:\n'))
                name = str(input('Name:\n'))
                updatename(name, num)
            else:
                name = str(input('Name:\n'))
                num = str(input('Number:\n'))
                updatenumber(name, num)
            print("Complete\n")
        except:
            print("Error")
            break
    elif inp == 'Q':
        start = False
    elif inp == 'S':
        f = int(input('Filter mode: 0 - date, 1 - name, 2 - number\n'))
        showcontacts(f) 