from replit import db

async def channel_has_list(channel_id: str):
    return channel_id in db.keys()

async def connect_database():
    pass

async def create_list(channel_id: str, label: str):
    if channel_has_list(channel_id):
        # TODO: handle list already exists error
        pass
    else:
        db[channel_id] = []

async def delete_list(channel_id: str, label: str):
    if channel_has_list(channel_id):
        del db[channel_id]
    else:
        # TODO: handle list doesn't exist error
        pass

async def create_item(channel_id: str, label: str):
    if channel_has_list(channel_id):
        todo_list = db[channel_id]
        todo_list.append(label)
        db[channel_id] = todo_list
    else:
        # TODO: handle list doesn't exists error
        pass

async def delete_item(channel_id: str, label: str):
    if channel_has_list(channel_id):
        todo_list = db[channel_id]
        if label in todo_list:
            # remove item from list
            todo_list.remove(label)
            # set channel list to new list (w/o remove item)
            db[channel_id] = todo_list
        else:
            # TODO: handle item doesn't exist in list error
            pass
    else:
        # TODO: handle list doesn't exists error
        pass


async def init():
    await connect_database()

