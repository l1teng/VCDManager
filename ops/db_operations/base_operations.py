from abc import ABC, abstractmethod
import pymysql
import logging


class BaseManager(ABC):
    @abstractmethod
    def __init__(self):
        self.db_name = ''
        self.__db_tools_ = 'MySQL'
        self.connection = None

    @property
    def db_tools(self):
        return self.__db_tools_

    @property
    def connection_status(self):
        if self.connection is None:
            return False
        else:
            return self.connection.open

    def connection_establish(self, db_user: str, db_passwd: str, db_ip: str = "127.0.0.1",
                             db_port: int = 3306, db_enc: str = 'utf8', re_login=True):
        if (self.connection_status is False) or (self.connection_status and re_login):
            try:
                self.connection = pymysql.Connect(host=db_ip, port=db_port, user=db_user, passwd=db_passwd,
                                                  database=self.db_name, charset=db_enc)
            except pymysql.err.OperationalError:
                logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Login info mismatch', self.__class__.__name__,
                                                                      'connection_establish'))
                self.connection = None
        else:
            self.connection = None

    def connection_close(self):
        try:
            self.connection.close()
        except pymysql.err.Error:
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection already closed',
                                                                  self.__class__.__name__, 'connection close'))
        except AttributeError:
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__, 'connection close'))

    def run_sql_cmd(self, cmd):
        try:
            cursor = self.connection.cursor()
            cursor.execute(cmd)
            self.connection.commit()
            return cursor.fetchall()
        except AttributeError:
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__, 'execute MySQL scripts'))
        except pymysql.err.Error:
            self.connection.rollback()
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Error occur when commit changes to MySQL',
                                                                  self.__class__.__name__, 'execute MySQL scripts'))
