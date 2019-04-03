# coding:utf-8

from jupyterhub.auth import Authenticator
from tornado import gen

import os
import sqlite3


class SQLiteAuthenticator(Authenticator):

    """JupyterHub Authenticator Based on SQLite"""

    def __init__(self, **kwargs):
        super(SQLiteAuthenticator, self).__init__(**kwargs)

    @staticmethod
    def _verify_password(username, password):
        try:
            # to define sqlite db location in hub images
            os.environ["JUPYTERHUB_SQLITEDB_PATH"]="/home/jovyan/user.db"

            sql_cnn = sqlite3.connect(os.getenv('JUPYTERHUB_SQLITEDB_PATH'))
            cursor = sql_cnn.cursor()
            sql = ("SELECT `password` FROM users WHERE `username` = '{}'").format(username)
            cursor.execute(sql)

            user_passwd = cursor.fetchone()[0]
            input_passwd = password

            if user_passwd == input_passwd:
                cursor.close()
                sql_cnn.close()
                return True
            else:
                cursor.close()
                sql_cnn.close()
                return False
        except:
            cursor.close()
            sql_cnn.close()
            return False

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        passwd = data['password']

        if self._verify_password(username, passwd):
            return data['username']
        else:
            return None
