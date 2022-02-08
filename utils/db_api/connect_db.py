from utils.db_api.create_session import async_db_session


async def init_app():
    await async_db_session.init()
    await async_db_session.create_all()
