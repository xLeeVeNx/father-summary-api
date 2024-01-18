from logging.config import fileConfig

from alembic import context

from app.database import Base, engine
Base.metadata.reflect(bind=engine)

target_metadata = Base.metadata

config = context.config
fileConfig(config.config_file_name)
target_metadata.reflect(bind=engine)

config.set_main_option('sqlalchemy.url', str(engine.url))
config.set_main_option('target_metadata', 'app.database.Base.metadata')