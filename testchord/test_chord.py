from pupdb.core import ChordNode

def test_chord():
    m = 7  # Số bit trong ID của nút
    node_ids = [0, 25, 50, 75]
    nodes = [ChordNode(id, m, f'db_{id}.json') for id in node_ids]

    for i, node in enumerate(nodes):
        node.set_successor(nodes[(i + 1) % len(nodes)])

    for node in nodes:
        node.calculate_finger_table(nodes)

    for node in nodes:
        node.display_finger_table()

    # Thêm dữ liệu vào hệ thống Chord
    start_node = nodes[0]
    for i in range(1, 101):
        start_node.set(i, f'value{i}')
    start_node.set(101, 'Vuongpro')

    # # Lấy dữ liệu từ hệ thống Chord và kiểm tra
    # for i in range(1, 101):
    #     value = start_node.get(i)
    #     print(f'Key {i}:', value)

    # # Kiểm tra các khóa trong hệ thống Chord
    # keys = start_node.keys()
    # print('Keys:', keys)

    # # Kiểm tra các giá trị trong hệ thống Chord
    # values = start_node.values()
    # print('Values:', values)

    # # Kiểm tra các cặp khóa-giá trị trong hệ thống Chord
    # items = start_node.items()
    # print('Items:', items)

    # # Kiểm tra dump của cơ sở dữ liệu
    # db_dump = start_node.dumps()
    # print('Database dump:', db_dump)

    # # Xóa toàn bộ cơ sở dữ liệu
    # start_node.truncate_db()
    # print('Keys after truncate:', start_node.keys())

    # Tìm và in ra ID của nút chịu trách nhiệm quản lý một khóa cụ thể
    key_to_find = 42
    NODE = start_node.resolve(key_to_find)
    print(f"Key {key_to_find} được quản lí bởi {NODE.id}.")
    print(f"{NODE.m}")
    print(f"Giá trị của khóa {key_to_find} là {start_node.get(key_to_find)}.")
    print(f"Giá trị của khóa 101 là {start_node.get(101)}.")

if __name__ == '__main__':
    test_chord()