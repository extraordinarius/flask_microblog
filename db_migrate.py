import imp
from migrate.versioning import api
from microblog import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

v = api.db_version(
		SQLALCHEMY_DATABASE_URI,
		SQLALCHEMY_MIGRATE_REPO)

migration = SQLALCHEMY_MIGRATE_REPO + \
			'/versions/{0:03d}_migration.py'.format(v+1)

tmp_module = imp.new_module('old_module')
