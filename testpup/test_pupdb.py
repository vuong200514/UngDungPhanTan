import os
import json
import logging
from pupdb.core import PupDB
def test_pupdb():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
    db_file_path = 'test_db.json'

    # Khởi tạo cơ sở dữ liệu PupDB
    db = PupDB(db_file_path)

    # Thêm dữ liệu vào cơ sở dữ liệu
    db.set('khoa1', 'giatri1')
    db.set('khoa2', 'giatri2')
    db.set('khoa3', 'giatri3')

    # Lấy dữ liệu từ cơ sở dữ liệu
    print('khoa1:', db.get('khoa1'))
    print('khoa2:', db.get('khoa2'))
    print('khoa3:', db.get('khoa3'))
    print('khoa4:', db.get('khoa4'))  # Khóa không tồn tại

    # Xóa dữ liệu từ cơ sở dữ liệu
    db.remove('khoa1')
    print('khoa1 sau khi xóa:', db.get('khoa1'))

    # Kiểm tra các khóa trong cơ sở dữ liệu
    keys = db.keys()
    print('Các khóa:', list(keys))

    # Kiểm tra các giá trị trong cơ sở dữ liệu
    values = db.values()
    print('Các giá trị:', list(values))

    # Kiểm tra các cặp khóa-giá trị trong cơ sở dữ liệu
    items = db.items()
    print('Các cặp khóa-giá trị:', list(items))

    # Kiểm tra dump của cơ sở dữ liệu
    db_dump = db.dumps()
    print('Dump cơ sở dữ liệu:', db_dump)

    # Xóa toàn bộ cơ sở dữ liệu
    db.truncate_db()
    print('Các khóa sau khi xóa:', list(db.keys()))

    # Xóa file cơ sở dữ liệu
    if os.path.exists(db_file_path):
        os.remove(db_file_path)
if __name__ == '__main__':
    test_pupdb()