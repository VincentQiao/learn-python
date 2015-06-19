# -*- coding: utf-8 -*-
__author__ = 'vincent'

' Simple ORM using metaclass '
# ORM ``object relational mapping'', 对象-关系映射，把关系数据库的一行映射为一个对象。
# 也即一个类对应一个表

# TODO:
# Field类，负责保存数据库表的字段名和字段类型

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        # <Field, abc>
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs:
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings:
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(self, **kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')