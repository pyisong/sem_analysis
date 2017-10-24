# *-* coding:utf-8 *-*

import settings
from sem_index.models import SemMonitorCrawlInfo


def get_company_id(use_id):
    db = settings.get_mysql_db_test()
    sql = 'select company_id from sem_user_info where user_id=%s'
    cursor = db.cursor()
    cursor.execute(sql, use_id)
    result = cursor.fetchone()
    return result[0]


def get_data_sour_id_list(*relate_id):
    db = settings.get_mysql_db_test()
    sql = 'SELECT data_source_id FROM sem_monitor_crawl_info WHERE company_id=%s'
    cursor = db.cursor()
    cursor.execute(sql, relate_id)
    data_sour_id_list = []
    result = cursor.fetchall()
    for item in result:
        data_sour_id_list.append(item[0])
    data_sour_id_list.append(2)
    return data_sour_id_list


def get_data_sour(company_id):
    data_sour_id_list = []
    query_set_list = SemMonitorCrawlInfo.objects.filter(company_id=int(company_id))
    for item in query_set_list:
        data_sour_id_list.append(item.company_name)
    return data_sour_id_list

if __name__ == "__main__":
    # print get_data_sour_id_list(1)
    # get_data_sour(1)
    get_company_id(1)
