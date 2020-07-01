
import os

common=dict(
    gzip = 'on',
    debug = False,
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    port = os.environ.get('PORT', '8000'),
    serverurl = "http://localhost:9887",
    busiServer = "http://localhost:9888"
)
common['static'] = os.path.join(common['basedir'],"static")
common['images'] = os.path.join(common['static'],"images")

mysql=dict(
	host = os.environ.get('DBHOST', 'localhost'),
	port = int(os.environ.get('DBPORT', 3306)),
	user = os.environ.get('DBUSER', 'root'),
    name = os.environ.get('DBNAME', 'allwin_new'),
	password = os.environ.get('DBPASS', '123456'),
    min_connections=2,
    max_connections=5,
    charset='utf8'
)

redis=dict(
    host='localhost',
    port=6379,
    password="123456",
    db = 0,
    minsize = 1,
    maxsize = 2,
    encoding = 'utf8'
)

config_insert=dict(
	common = common,
	mysql = mysql,
	redis = redis
)