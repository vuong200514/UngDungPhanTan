from pupdb.core import ChordNode

def test_chord():
    m = 7  # Số bit trong ID của nút
    node_ids = [0, 25, 50, 75]
    nodes = []

    #Khởi tạo chord
    for id in node_ids:
        node = ChordNode(id, m, f'db_{id}.json', nodes)
        nodes.append(node)

    # Thiết lập các nút kế tiếp cho mỗi nút
    for i, node in enumerate(nodes):
        node.setSucc(nodes[(i + 1) % len(nodes)])

    # Tính bảng finger cho mỗi nút
    for node in nodes:
        node.tinhFingerTable(nodes)

    # # In bảng finger cho mỗi nút
    # for node in nodes:
    #     node.fingerTable()

    # Thêm dữ liệu vào hệ thống Chord
    head = nodes[0]
    for i in range(1, 31):
        j=i*3
        head.set(j, f'value{j}')

    # Lấy dữ liệu từ hệ thống Chord và kiểm tra
    print(f'Key {21}:', head.get(21))

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