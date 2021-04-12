# coding=utf-8
import psycopg2
import pymongo
from common.common_config import common_config


class OperationDb:

    database_config = common_config.get("db_config")

    @classmethod
    def query_sql(cls, sql_str):
        # 创建连接对象
        with psycopg2.connect(**cls.database_config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql_str)
                results = cur.fetchall()
            print('查询结束')
        return results


class OperationMongoDb:

    database_config = common_config.get("mongo_db_config")

    @classmethod
    def query_data(cls, table_name, condition={}, fields={}):
        # 创建连接对象
        with pymongo.MongoClient(**cls.database_config) as client:
            db = client["student_statistics"]
            db_collection = db[table_name]
            return list(db_collection.find(condition, fields).skip(0))
            # print(client.list_database_names())
            # print(client.list_databases())
            # print(db.list_collection_names())
            # print(db_collection.count_documents(sql_str))
            # print(type(db_collection.find({"createTime": "2021-04-09"})))
            # print(list(db_collection.find(sql_str, get_fields).limit(10).skip(0)))
            # for x in db_collection.find(sql_str, get_fields).limit(10).skip(0):
            #     print(x)


if __name__ == "__main__":
    """pip install psycopg2-binary"""
    # sql = """select student_id,student_name from service_profile.student limit 10"""
    # config = {
    #     'database': 'edu',
    #     "user": 'read_user',
    #     "password": 'c5JJUqmtTeaSaOTN2gs7',
    #     "host": '132.232.15.12',
    #     "port": 5432
    # }
    # opd = OperationDb(config).query_sql(sql)
    # print(opd)
    omd = OperationMongoDb()
    table_name = "202103_continue"
    condition = {"createTime": "2021-04-09"}
    fields = {'_id': 0, "schoolAreaId": 1, "subject": 1, 'studentId': 1}
    omd.query_data(table_name, condition=condition, fields=fields)


