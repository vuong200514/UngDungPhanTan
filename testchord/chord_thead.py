from pupdb.core import ChordNode
import threading

def add_data(node, start, end):
    for i in range(start, end):
        j = i
        node.set(j, f'value{j}')

def read_data(node, keys):
    for key in keys:
        print(f'Key {key}:', node.get(key))

def test_chord():
    m = 7  # Số bit trong ID của nút
    node_ids = [25, 50, 75, 100]
    nodes = []

    # Khởi tạo chord
    for id in node_ids:
        node = ChordNode(id, m, f'db_{id}.json', nodes)
        nodes.append(node)

    # Thiết lập các nút kế tiếp cho mỗi nút
    for i, node in enumerate(nodes):
        node.setSucc(nodes[(i + 1) % len(nodes)])

    # Tính bảng finger cho mỗi nút
    for node in nodes:
        node.tinhFingerTable(nodes)

    # Thêm dữ liệu thread
    head = nodes[0]
    write_threads = []
    for i in range(1, 10000, 1000):
        t = threading.Thread(target=add_data, args=(head, i, i + 1000))
        write_threads.append(t)
        t.start()

    for t in write_threads:
        t.join()

    # # Lấy dữ liệu thread
    # read_threads = []
    # keys_to_read = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    # for i in range(0, len(keys_to_read), 2):
    #     t = threading.Thread(target=read_data, args=(head, keys_to_read[i:i + 2]))
    #     read_threads.append(t)
    #     t.start()

    # for t in read_threads:
    #     t.join()

    # # Kiểm tra các khóa trong hệ thống Chord
    # keys = head.keys()
    # print('Keys:', keys)

    # # Kiểm tra các giá trị trong hệ thống Chord
    # values = head.values()
    # print('Values:', values)

    # # Kiểm tra các cặp khóa-giá trị trong hệ thống Chord
    # items = head.items()
    # print('Items:', items)

    # # Kiểm tra dump của cơ sở dữ liệu
    # db_dump = head.dumps()
    # print('Database dump:', db_dump)

    # # Xóa toàn bộ cơ sở dữ liệu
    # head.truncate_db()
    # print('Keys after truncate:', head.keys())

    # Tìm và in ra ID của nút chịu trách nhiệm quản lý một khóa cụ thể
    key_to_find = 15
    NODE = head.timNode(key_to_find)
    print(f"Key {key_to_find} được quản lí bởi {NODE.id}.")
    print(f"Giá trị của khóa {key_to_find} là {head.get(key_to_find)}.")

if __name__ == '__main__':
    test_chord()