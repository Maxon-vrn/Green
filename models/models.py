from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, func, JSON, Boolean

metadata = MetaData()


#В таблице ролей будет происходить соотнесение и хранение организации и роли в этой организации для доступов к контенту
role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),    #название роли / предварительно нужно сделать 3 роли с правами(админ,исполнитель,контролер?)
    Column('permissions', JSON),   #хранение роли пользователя в организации и другой информации
    Column('created_at', TIMESTAMP, default=datetime.utcnow),
    Column('updated_at', TIMESTAMP, onupdate=datetime.utcnow),  #utcnow - универсальный часовой пояс

)

#создаем таблицу сущностей "Оргнизация"
organization = Table(
    'organization',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name_organization', String(255), nullable=False),   # nullable=False - не может быть пустым\description='наименование организации'
    Column('name_admin', String(255), nullable=False),
    Column('login', String(255), nullable=False),
    Column('password', String(255), nullable=False),    #требуется проверка что оба пароля были введены одинаковыми на странице регистрации/пароли всегда храним в захешированном виде
    Column('email', String(255), nullable=False),
    #вводим ограничение длинны номера(пример +79034567654 или 89034353423) - min_length=10, max_length=12,
    Column('phone', String(12), nullable=False),
    # если inn совпадают \ ограничениие длинны ИНН 10(юрики) или 12 символов физики
    Column('inn', String(12), nullable=False),


    Column('created_at', TIMESTAMP, default=datetime.utcnow),     #время регистрации пользователя
)



user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),    #index=True, unique=True
    Column('username', String(255), nullable=False),
    Column('login', String(255), nullable=False),
    Column('hashed_password', String(255), nullable=False),
    Column('email', String(255), nullable=False),
    Column('phone', String(12), nullable=False),    #вводим ограничение длинны номера(пример +79034567654 или 89034353423)
    Column('inn', String(12), nullable=False), #если inn совпадают \ ограничениие длинны ИНН 10 или 12 символов
    Column('role_id', Integer, ForeignKey(role.c.id),primary_key=True), #табличка физлиц ссылатся на таблицу ролей
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),

    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)



