import  pymysql
from conf import DB_CONFIG as conf

import threading

def transactional(func):

    def trans_contral(*args,**kwargs):
        try:
            s = func(*args,**kwargs)
        except:
            # 回滚
            DBUtils.get_connection().rollback()

        finally:
            # 关闭connection
            conn = DBUtils.get_connection()
            conn.close()
            # 清除掉 local 中的 conn 属性
            delattr(DBUtils.local,'conn')
        return  s
    return trans_contral







class DBUtils:
    '''
    threading 可以绑定一个值、这个值在多个线程中 不共享

    '''
    # 创建一个 threading对象
    local = threading.local()
    """
    DBUtils 完成数据库的增删改查操作
    CTRL + SHift + u
    """
    @classmethod
    def get_connection(cls):
        #只获取一次 没有conn的话，去创建，有的话，直接返回
        if not  hasattr(cls.local , 'conn'):
            cls.local.conn = pymysql.connect(
                host=conf['HOST'],
                port=conf['PORT'],
                user=conf['USER'],
                password=conf['PASSWORD'],
                database=conf['DATABASE'],
            )
        return  cls.local.conn

    @staticmethod
    def update(sql,args = None):
        """
        该方法支持增删改 三个动作
        :param sql:
        :param args:
        :return:
        """
        try:
            # 获取游标
            cursor = DBUtils.get_connection().cursor()
            #执行SQL
            return cursor.execute(sql,args)
        finally:
            cursor.close()

    @staticmethod
    def save(sql,arge=None ):
        '''


        :param arge:
        :return:
        '''














