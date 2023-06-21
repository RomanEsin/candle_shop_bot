import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID, Enum, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Status(enum.Enum):
    CREATED = "created"
    PAID = "paid"
    CANCELED = "canceled"
    DELIVERED = "delivered"

    @property
    def title(self):
        if self == Status.CREATED:
            return "Заказ создан"
        elif self == Status.PAID:
            return "Заказ оплачен"
        elif self == Status.CANCELED:
            return "Заказ отменен"
        elif self == Status.DELIVERED:
            return "Заказ выполнен"

    @property
    def description(self):
        if self == Status.CREATED:
            return "Мы получили ваш заказ и обрабатываем его"
        elif self == Status.PAID:
            return "Мы получили оплату и готовим ваш заказ"
        elif self == Status.CANCELED:
            return "Мы отменили ваш заказ"
        elif self == Status.DELIVERED:
            return "Мы доставили ваш заказ"


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(Status), default=Status.CREATED)
    address = Column(String)
    comments = Column(String)
    create_date = Column(DateTime, default=datetime.now())


class TelegramLink(Base):
    __tablename__ = "telegram_link"

    id = Column(Integer, primary_key=True, index=True)
    link_hex = Column(String)
    chat_id = Column(Integer)