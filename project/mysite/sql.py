import pandas as pd
import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='1234',database='test')
cursor = conn.cursor()

def create_table():
    sql = '''
    CREATE TABLE `company_info` (
      `序号` int(11) DEFAULT NULL,
      `股票代码` varchar(255) DEFAULT NULL,
      `股票简称` varchar(255) DEFAULT NULL,
      `公司名称` varchar(255) DEFAULT NULL,
      `省份` varchar(255) DEFAULT NULL,
      `城市` varchar(255) DEFAULT NULL,
      `主营业务收入(202112)` varchar(255) DEFAULT NULL,
      `净利润(202112)` varchar(255) DEFAULT NULL,
      `员工人数` varchar(255) DEFAULT NULL,
      `上市日期` varchar(255) DEFAULT NULL,
      `招股书` varchar(255) DEFAULT NULL,
      `公司财报` varchar(255) DEFAULT NULL,
      `行业分类` varchar(255) DEFAULT NULL,
      `产品类型` text,
      `主营业务` text
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    '''
    cursor.execute(sql)
    conn.commit()


def insert_into_table():
    df = pd.read_csv(r'C:\Users\chang\Desktop\project\mysite\上市公司信息.csv', dtype=str)
    for index,col in df.iterrows():
        print(col)
        sql = 'insert into `mysite_echarts_list` values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql,[str(k) for k in list(col)])
    conn.commit()


if __name__ == '__main__':
    insert_into_table()



