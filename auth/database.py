from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, Boolean, Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from models.models import role

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"  #база дынных и драйвер(асинкпж)
Base: DeclarativeMeta = declarative_base()  #информайия из примера - мета данные для аккамулирования


engine = create_async_engine(DATABASE_URL)  # точка входа нашей sql-создаёт асинхронное подключение к базе данных PostgreSQL, используя драйвер asyncpg.
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)    # создание соединения на основе точки входа - создаёт фабрику асинхронных сессий, используя созданный движок. Сессии используются для выполнения транзакций в базе данных.


class User(SQLAlchemyBaseUserTable[int], Base):
    #id = Column(Integer, primary_key=True) - попробовать привести к такому виду!
    id = Column('id', Integer, primary_key=True, index=True, unique=True)
    username = Column('username', String(255), nullable=False)
    login = Column('login', String(255), nullable=False)
    hashed_password = Column('hashed_password', String(255), nullable=False)
    email = Column('email', String(255), nullable=False)
    phone = Column('phone', String(12),
           nullable=False)  # вводим ограничение длинны номера(пример +79034567654 или 89034353423)
    inn = Column('inn', String(12), nullable=False)  # если inn совпадают \ ограничениие длинны ИНН 10 или 12 символов
    role_id = Column('role_id', Integer, ForeignKey(role.c.id), primary_key=True)  # табличка физлиц ссылатся на таблицу ролей
    registered_at = Column('registered_at', TIMESTAMP, default=datetime.utcnow)

    is_active = Column('is_active', Boolean, default=True, nullable=False)
    is_superuser = Column('is_superuser', Boolean, default=False, nullable=False)
    is_verified = Column('is_verified', Boolean, default=False, nullable=False)




    #id: Mapped[int] = mapped_column(Integer, primary_key=True,
    #                                )  #в примери использовалась другая структура Colomn без использования  Mapped...
    #username: Mapped[str] = mapped_column(String, primary_key=True)
    #login: Mapped[str] = mapped_column(String, primary_key=True)
    #hashed_password: Mapped[str] = mapped_column(String(length=1024))  #ссылка на пароль регистрации в бд |nullable=False -хз ругался на аргумент
    #email: Mapped[str] = mapped_column(String(length=255), unique=True, index=True, nullable=False)
    #phone: Mapped[str] = mapped_column(String(length=12), nullable=False)
    #inn: Mapped[str] = mapped_column(String(length=12),
    #                                 nullable=False)  #если inn совпадают \ ограничениие длинны ИНН 10(юрики) или 12 символов физики
    #role_id: Mapped[int] = mapped_column(Integer, ForeignKey(
    #    role.c.id))  #ссылка на другую колонку с названием из другой таблицы
    #registered_at: Mapped[datetime] = mapped_column(TIMESTAMP,
    #                                                default=datetime.utcnow)  #ссылается на дату и время регистрации
    #is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    #is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    #is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)



async def get_async_session() -> AsyncGenerator[AsyncSession, None]:    #получение асинхронной сессии
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):  # получение пользователя
        #Depends - инъекция зависимостей  и параметров
    yield SQLAlchemyUserDatabase(session, User)
