from abc import ABC, abstractmethod
import pymysql


class BaseManager(ABC):
    @abstractmethod
    def __init__(self, db_user: str, db_passwd: str, db_name: str, db_ip: str = "127.0.0.1", db_port: int = 3306,
                 db_enc: str = 'utf8'):
        self.__db_tools_ = 'MySQL'
        self.content = pymysql.Connect(
            host=db_ip, port=db_port, user=db_user, passwd=db_passwd, db=db_name, charset=db_enc
        )
        self.cursor = self.content.cursor()

    @property
    def db_tools(self):
        return self.__db_tools_

    def run_sql_cmd(self, cmd):
        try:
            self.cursor.execute(cmd)
            self.content.commit()
        except:
            self.content.rollback()

        return self.cursor.fetchall()
