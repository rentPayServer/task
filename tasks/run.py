

from models.task import Order,CashoutList,BalList
from utils.time_st import UtilTime
from loguru import logger
from utils.database import MysqlPool

async def clearData(**kwargs):

    db = kwargs.get("db")

    logger.info("清理数据开始...")
    async with MysqlPool().get_conn.atomic_async():
        r1=await db.execute(Order.delete().where(Order.createtime<=UtilTime().today.shift(days=-15).timestamp))
        r2=await db.execute(CashoutList.delete().where(CashoutList.createtime <= UtilTime().today.shift(days=-15).timestamp))
        r3=await db.execute(BalList.delete().where(BalList.createtime <= UtilTime().today.shift(days=-15).timestamp))

        logger.info("清理Order{}条,CashoutList{}条,BalList{}条".format(r1,r2,r3))
    logger.info("清理数据结束...")