import settings


def get_data_source_id_list(*relate_id):
    db = settings.get_mysql_db()
    sql = 'SELECT data_source_id FROM sem_monitor_crawl_info WHERE company_id=%s'
    cursor = db.cursor()
    cursor.execute(sql, relate_id)
    data_source_id_list = cursor.fetchall()
    if relate_id == (2,):
        return [2]
    if relate_id == (1,):
        return [1]
    return data_source_id_list


if __name__ == "__main__":
    print get_data_source_id_list(2)
