from datetime import datetime, date

from sqlalchemy import func
from sqlalchemy.orm import mapped_column, Mapped

from src.db.db_connection import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.current_timestamp(),
                                                 onupdate=func.current_timestamp())
    last_name: Mapped[str]
    first_name: Mapped[str]
    middle_name: Mapped[str]
    city: Mapped[str]
    date_of_birth: Mapped[date]
    salary: Mapped[int]


    def _as_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "city": self.city,
            "date_of_birth": self.date_of_birth,
            "salary": self.salary
        }
