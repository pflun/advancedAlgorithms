# -*- coding: utf-8 -*-
import uuid

class InMemoryDB(object):
    def __init__(self):
        self.store = {}

    def insert(self, record):
        if not isinstance(record, dict):
            raise ValueError("Record must be a dictionary")

        record_id = str(uuid.uuid4())
        stored_record = record.copy()
        stored_record['_id'] = record_id

        self.store[record_id] = stored_record
        return record_id

    def find_by_column(self, column_name):
        result = []
        # 使用 itervalues() 避免在内存中拷贝整个 values 列表
        for record in self.store.itervalues():
            if column_name in record:
                result.append(record)
        return result

    def filter_by(self, **conditions):
        result = []
        for record in self.store.itervalues():
            match = True
            # 使用 iteritems() 提高字典遍历性能
            for k, v in conditions.iteritems():
                if record.get(k) != v:
                    match = False
                    break

            if match:
                result.append(record)

        return result

    def filter_by_advanced(self, condition_func):
        return [r for r in self.store.itervalues() if condition_func(r)]

if __name__ == '__main__':
    db = InMemoryDB()

    print "--- 插入数据 ---"
    id1 = db.insert({"name": "Alice", "city": "New York", "age": 28})
    id2 = db.insert({"name": "Bob", "city": "Seattle"})
    id3 = db.insert({"name": "Charlie", "city": "New York", "status": "Active"})

    print "Inserted {0} records.".format(len(db.store))

    print "\n--- 查找包含 'age' column 的记录 ---"
    age_records = db.find_by_column("age")
    for r in age_records:
        print r

    print "\n--- Filter By: city='New York' ---"
    ny_records = db.filter_by(city="New York")
    for r in ny_records:
        print r

    print "\n--- Filter By (多条件): city='New York', status='Active' ---"
    active_ny = db.filter_by(city="New York", status="Active")
    for r in active_ny:
        print r

    print "\n--- Advanced Filter: age > 25 ---"
    older_than_25 = db.filter_by_advanced(lambda r: r.get('age', 0) > 25)
    for r in older_than_25:
        print r