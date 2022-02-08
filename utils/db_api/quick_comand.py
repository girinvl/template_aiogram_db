from utils.db_api.schemas import Users


async def create_user(id: int, name: str):
    user = await Users.get(id=id)
    if user is None:
        await Users.create(id=id, name=name)
        user = await Users.get(id=id)
    return user


async def get_user(id: int):
    user = await Users.get(id=id)
    return user
