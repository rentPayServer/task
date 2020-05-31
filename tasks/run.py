

from models.task import Order,CashoutList,BalList
from utils.time_st import UtilTime
from loguru import logger

def clearData(**kwargs):

    db = kwargs.get("db")

    logger.info("清理数据开始...")
    with db.atomic():
        r1=Order.delete().where(Order.createtime<=UtilTime().today.shift(days=-15).timestamp).execute()
        r2=CashoutList.delete().where(CashoutList.createtime <= UtilTime().today.shift(days=-15).timestamp).execute()
        r3=BalList.delete().where(BalList.createtime <= UtilTime().today.shift(days=-15).timestamp).execute()

        logger.info("清理Order{}条,CashoutList{}条,BalList{}条".format(r1,r2,r3))
    logger.info("清理数据结束...")