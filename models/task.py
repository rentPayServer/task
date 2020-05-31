
from peewee import *
from models.base import BaseModel

class Order(BaseModel):

    ordercode = BigAutoField(primary_key=True,verbose_name="订单ID")
    userid = BigIntegerField(verbose_name="商户号",default=0)

    down_ordercode = CharField(verbose_name='下游订单号',default='',max_length=60)
    last_ordercode = CharField(verbose_name='上游订单号',default='',max_length=60)

    paypass = IntegerField(verbose_name="支付渠道",default=0)
    paypassname = CharField(verbose_name="支付渠道名称",default="",max_length=60)

    paytype = IntegerField(verbose_name="支付方式",default=0)
    paytypename = CharField(verbose_name="支付方式名称",default="",max_length=60)

    amount = DecimalField(max_digits=18,decimal_places=6,default=0.000,verbose_name="订单金额")
    confirm_amount = DecimalField(max_digits=18,decimal_places=6,default=0.000,verbose_name="收款金额")

    tech_cost = DecimalField(max_digits=18,decimal_places=6,default=0.000,verbose_name="技术费")

    myfee = DecimalField(max_digits=18, decimal_places=6, default=0.000, verbose_name="抛开码商成本费用")
    codefee = DecimalField(max_digits=18, decimal_places=6, default=0.000, verbose_name="码商费用")
    agentfee = DecimalField(max_digits=18, decimal_places=6, default=0.000, verbose_name="代理费用")

    status = CharField(max_length=1,verbose_name="支付状态 : 0-支付成功,1-等待支付,2-支付失败,3-订单过期")

    down_status = CharField(max_length=1,verbose_name="支付状态 : 0-支付成功,1-等待支付,2-回调失败,3-订单过期",default='1')

    ismobile = CharField(max_length=1,verbose_name="是否手机,0-手机,1-pc",default='0')

    client_ip = CharField(max_length=60,verbose_name="客户端IP",default='')
    notifyurl = CharField(max_length=255,verbose_name="异步通知URL",default='')

    createtime = BigIntegerField(default=0)

    pay_time = BigIntegerField(default=0)

    qr_id = BigIntegerField(default=0,verbose_name="二维码ID")

    qr_type = CharField(max_length=5,default='QR001' ,
                            verbose_name="""二维码类型 QR001-微信个人二维码,
                                         QR005-付临门聚合支付码""")

    keep_info = TextField(verbose_name="请求的信息保存下来，回调时带回去",default='')

    lock = CharField(verbose_name="是否加密,0-加密,1-不加密",default="0",max_length=1)

    isjd = CharField(verbose_name="是否京东订单,0-是,1-否||是否红包",default='1',max_length=1)

    jd_ordercode = CharField(verbose_name="京东订单号||红包订单号",max_length=120,default='')
    jd_payordercode = CharField(verbose_name="红包支付订单号",max_length=120,default='')
    jd_data = CharField(verbose_name="京东json数据|红包数据(抢红包的信息)",max_length=1024,default="")

    # last_userid = models.IntegerField(verbose_name="码商ID",default=0)
    open_name = CharField(verbose_name="开户人", max_length=30, default='')
    bankno = CharField(verbose_name="银行卡",max_length=60,default='')

    class Meta:
        db_table = 'order'

class BalList(BaseModel):
    id = BigAutoField(primary_key=True)
    userid =  BigIntegerField(default=0,verbose_name="用户ID")
    amount = DecimalField(max_digits=18,decimal_places=6,default=0.000,verbose_name="交易金额")
    bal = DecimalField(max_digits=18, decimal_places=6, default=0.000, verbose_name="交易前金额")
    confirm_bal = DecimalField(max_digits=18, decimal_places=6, default=0.000, verbose_name="交易后金额")
    memo = CharField(max_length=255,verbose_name="交易摘要")
    ordercode = CharField(max_length=120,default='0',verbose_name="订单号")
    memo1 = CharField(max_length=255, verbose_name="交易摘要",default="1")

    createtime = BigIntegerField()

    class Meta:
        db_table = 'ballist'

class CashoutList(BaseModel):

    id = BigAutoField(primary_key=True)

    userid = BigIntegerField(verbose_name="用户ID", default=0)
    name = CharField(max_length=120, verbose_name="名称", default='', null=True)

    amount = DecimalField(max_digits=18,decimal_places=6,default=0.000,verbose_name="申请金额")

    bank_name = CharField(max_length=60,verbose_name="银行名称",default='')
    open_name = CharField(max_length=60,verbose_name="开户人",default='')
    open_bank = CharField(max_length=250,verbose_name="支行",default='')
    bank_card_number = CharField(max_length=60,verbose_name="银行卡号",default='')

    status = CharField(max_length=1,verbose_name="提现状态,0-提现申请中,1-提现通过,2-提现拒绝")

    createtime = BigIntegerField(default=0)

    updtime  = BigIntegerField(default=0)

    tranid = CharField(default='',verbose_name="交易流水号,代付产生",max_length=120)
    paypassid = BigIntegerField(default=0,verbose_name="代付产生,渠道号")
    downordercode = CharField(default='',max_length=120,verbose_name="商户订单号")

    df_status = CharField(max_length=1,verbose_name="提现状态,0-支付中,1-支付成功,2-支付失败",default="0")

    memo = CharField(default="",max_length=255,verbose_name="备注")

    class Meta:
        db_table = 'cashout_list'