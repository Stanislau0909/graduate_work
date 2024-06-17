from sqlalchemy import select
from sqlalchemy.dialects.postgresql import psycopg2

from src.db.db_connection import Base, engine, get_session
from src.db.tables import User
from faker import Faker


faker = Faker("ru_RU")


def create_users(num: int = 10):
    for i in range(num):
        for session in get_session():
            session.add(
                User(
                    last_name=faker.last_name(),
                    first_name=faker.first_name(),
                    middle_name=faker.last_name(),
                    city=faker.city(),
                    date_of_birth=faker.date_of_birth(minimum_age=18, maximum_age=65),
                    salary=faker.random_int(min=30000, max=500000)
                )
            )


# def list_users():
#     users = []
#     for session in get_session():
#         data = session.scalars(select(User)).all()
#         for row in data:
#             users.append(row._as_dict())
#     return users

def filter_users(id_lower_limit: int) -> list[dict]:
    stmt = select(User)
    if id_lower_limit:
        stmt = stmt.where(User.id > id_lower_limit)
    print(stmt.compile(compile_kwargs={"literal_binds": True}))
    users = []
    for session in get_session():
        data = session.scalars(select(User)).all()
        for row in data:
            users.append(row._as_dict())
    return users


Base.metadata.create_all(engine)







print(filter_users(id_lower_limit=2))