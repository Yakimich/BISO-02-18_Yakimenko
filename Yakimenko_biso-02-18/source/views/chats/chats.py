
from aiohttp import web


from settings import *

from commands import Command
from log import logger

cmd = Command()


@cmd('/getChat', methods=["GET", "OPTIONS"])

async def chats(request: web.Request, data: dict):
    res = db_mongo.get_chats()
    return res
  