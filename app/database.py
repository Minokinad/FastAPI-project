import sys
from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

sys.path.append(str(Path(__file__).parent.parent))

from app.config import settings

DB_URL = settings.db_url

engine = create_async_engine(DB_URL)

async_session_maker = sessionmaker(engine,  class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
