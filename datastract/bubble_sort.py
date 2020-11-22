class Animal:
    pass

anl = Animal()

print(anl)

print(type(anl))

print(type(Animal))

list = (Animal,)
dict = {'name':'哈士奇','age':2 }
atype = type('dog',list,dict)



dog = atype()


print(dog)
print(dog.name)

f = isinstance(dog,Animal)
print(f)

#  元类  生成一个类   实例化类，实例化的结果是一个类

#

# 动态的加载参数

def rename_attr(claname,bases,dicts):
    print('*****')
    print(type(claname))
    print(bases)
    print(dicts)
    _dicts = {}
    # for k,v in dicts.items:
    #     if not  k.startswith("__"):
    #         k = ''.join(['v_',k])
    #         _dicts[k] = v

    list = [(k,v)for k,v in dicts.items if not k.startswith('__') ]
    print(list)
    print(type(list))
    _dicts = dict(list)



    return type (claname,bases,_dicts)

class User(metaclass=rename_attr):
    id = None
    name = None
    sex = None
    card = None


u = User

print(u.v_id)




#

