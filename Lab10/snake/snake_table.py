import psycopg2
from config import params


def create_table():
    command = (
        '''
        CREATE TABLE SNAKE_GAME(
            name VARCHAR (255) UNIQUE NOT NULL,
            score VARCHAR (12) NOT NULL,
            level VARCHAR (12) NOT NULL
        );
        '''
    )
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(command)
        current.close()
        config.commit()

    except Exception as E:
        print(str(E))
    if config is not None:
        config.close()


create_table()
