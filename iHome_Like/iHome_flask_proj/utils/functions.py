

def get_database_config(database_conf):

    database = database_conf['database']
    driver = database_conf['driver']
    host = database_conf['host']
    port = database_conf['port']
    user = database_conf['user']
    password = database_conf['password']
    name = database_conf['name']

    return '{}+{}://{}:{}@{}:{}/{}'.format(database, driver, user, password, host, port, name)
