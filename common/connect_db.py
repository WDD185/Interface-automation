# coding=utf-8
import psycopg2


class OperationDb:
    def __init__(self, database_config: dict):
        self.database_config = database_config

    def query_sql(self, sql_str):
        # 创建连接对象
        with psycopg2.connect(**self.database_config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql_str)
                results = cur.fetchall()
            print('查询结束')
        return results


if __name__ == "__main__":
    """pip install psycopg2-binary"""
    sql = """select student_id,student_name from service_profile.student limit 10"""
    config = {
        'database': 'edu',
        "user": 'read_user',
        "password": 'c5JJUqmtTeaSaOTN2gs7',
        "host": '132.232.15.12',
        "port": 5432
    }
    opd = OperationDb(config).query_sql(sql)
    print(opd)

