# coding=utf-8
import psycopg2


class OperationDb:
    def __init__(self, database_config: dict):
        self.database_config = database_config

    def query_sql(self, sql_str):
        # 创建连接对象
        conn = psycopg2.connect(**self.database_config)
        cur = conn.cursor()  # 创建指针对象
        try:
            cur.execute(sql_str)
            results = cur.fetchall()
        finally:
            conn.commit()
            cur.close()
            conn.close()
            print('查询结束')
        return results


if __name__ == "__main__":
    sql = """select student_id,student_name from service_profile.student limit 10"""
    opd = OperationDb("../data/config/config.conf").query_sql(sql)
    print(opd)

