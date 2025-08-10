from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost/kiosk_db"
SQLALCHEMY_DATABASE_URL = "postgresql://lstd_user:gCMJ45hF04pyF6LJY2WRSNY56WiZYOtS@dpg-d2c307idbo4c73baolq0-a/lstd"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#comment