"""
1.下载sqlalchemy 插件

2.在py  文件中，导入 from sqlalchemy.engine import create_engine 模块

3. 创建一个 引擎对象
engine = create_engine('mysql+pymysql://root/localhost:3306/py1905')

4. 创建一个尸实体类，需要先获取基类

"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.engine import create_engine

# engine = create_engine("mysql://scott:tiger@hostname/dbname",
#                                     encoding='latin1', echo=True)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root@localhost:3306/py1908')

print(engine)

Base = declarative_base()


class Student(Base):
    # 描述的是 表和类的关系
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    # 描述的是  字段  和 属性 的关系

    name = Column('name', String(50))

    age = Column(Integer)

Base.metadata.drop_all(engine)
# 自动生成表
Base.metadata.create_all(engine)
