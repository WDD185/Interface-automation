import time
import datetime
import random
import psycopg2

createSchoolAreaId = [2389, 2398, 3363, 3015, 3154, 3352, 2369, 3095, 3348, 3333, 3351, 3359, 3345, 3365, 3362, 3339,
                      3353, 3334, 2400, 3360, 3361, 3373, 3371, 3366, 3349, 3372, 3340, 2427, 3367, 3335, 3148, 3374,
                      3377, 3369, 3376, 3378, 3368, 3336, 3370, 3357, 3350, 3001, 3072, 3049, 3342, 3337, 2411, 3344,
                      2412, 3100, 3146, 3052, 3047, 3157, 3107, 3108, 3076, 3147, 3167, 2413, 2383, 3064, 3152, 3063,
                      3101, 3130, 3170, 3074, 3165, 3044, 3059, 3038, 3166, 3168, 2385, 3171, 2373, 3137, 3151, 2417,
                      3041, 3036, 3060, 3125, 3046, 3109, 3110, 3142, 3149, 3037, 3039, 3104, 2422, 3158, 2407, 2386,
                      3099, 2410, 3067, 3329, 2371, 3330, 3133, 3071, 3070, 3053, 3065, 3150, 3061, 3126, 3062, 2423,
                      2364, 3043, 2415, 3131, 2388, 3096, 2376, 3042, 3127, 2402, 2359, 2365, 2408, 2425, 3002, 2391,
                      3135, 3136, 3153, 3139, 3144, 2419, 3075, 2416, 2421, 2363, 2368, 2403, 2414, 2392, 3138, 2406,
                      3156, 3155, 3097, 3098, 3141, 3069, 2405, 2399, 2397, 2360, 3145, 2420, 2404, 2374, 2401, 3054,
                      3124]

followingStatus = ['OVERTIME', 'UNFOLLOWED', 'FOLLOWING']


def end_time():
    today = datetime.date.today().strftime('%Y-%m-%d')
    print(today)
    return today


def start_time():
    last_month = (datetime.datetime.today() + datetime.timedelta(days=-31)).strftime('%Y-%m-%d')
    print(last_month)
    return last_month


def generate_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


def generate_name():
    # encoding: utf-8
    first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
    second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文",
                   "明浩", "光", "超", "军", "达", '新', '信']
    name1 = random.sample(first_name, 1) + random.sample(second_name, 1)
    name = ''.join(name1)
    return name


def generate_intentionLevel():
    Level = ['S', 'A', 'B', 'C']
    intentionLevel = random.sample(Level, 1)[0]
    return intentionLevel


def generate_sourceId():
    ID = [111, 112, 113, 119, 101, 102, 103, 114, 115]
    sourceId = random.sample(ID, 1)
    return sourceId


def pg_data():
    database = 'edu-admin'
    user = 'dev'
    password = 'mko0PL<.;?'
    host = '192.168.32.31'
    port = 5432
    with psycopg2.connect(database=database, user=user,
                          password=password, host=host, port=port)as pg_conn:
        with pg_conn.cursor() as cur:
            cur.execute('SELECT * FROM "service_crm"."clue_basic_info" LIMIT 1')
            results = cur.fetchall()
        return results


lst = [{'id': 111, 'name': '网站'},
       {'id': 112, 'name': '营销工具'},
       {'id': 113, 'name': '公众号'},
       {'id': 119, 'name': '网报小程序'},
       {'id': 101, 'name': '自然口碑'},
       {'id': 102, 'name': '营销活动'},
       {'id': 103, 'name': '营销口碑'},
       {'id': 114, 'name': '地推'},
       {'id': 115, 'name': '广告'},
       {'id': 116, 'name': '户外广告'}]
ids = [x.get("id") for x in lst]
