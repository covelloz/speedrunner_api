from speedrunner_api.db_migration import Migration

if __name__ == '__main__':
    Migration().exec_migration()
