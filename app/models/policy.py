from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base


class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, nullable=False)
    policy_number = Column(String, unique=True, nullable=False)
    coverage_amount = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

