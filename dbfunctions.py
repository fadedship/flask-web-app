import psycopg2


database_name = "flaskwebapp"
user_name = "postgres"
password = "123"
host_ip = "localhost"
host_port = 5432


conn = psycopg2.connect(database = "flaskwebapp",
                            user = "postgres",
                            password = "123",
                            host = "localhost",
                            port = 5432)


def login_success(username,password):

    crsor = conn.cursor()

    crsor.execute("SELECT username,password FROM users")

    user_records = crsor.fetchall()

    print(user_records)

    for users in user_records:
        if users[0] == username and users[1] == password:
            return True
        else:
            return False

