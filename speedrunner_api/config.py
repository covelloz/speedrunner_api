class Configuration(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = '5000'
        self.admin_usr = 'speedrunner_admin'
        self.admin_pwd = 'for_glory'
        self.database = 'speedrunner'
        self.csv_abspath = '/vagrant/data/speedrunner.csv'

config = Configuration()
