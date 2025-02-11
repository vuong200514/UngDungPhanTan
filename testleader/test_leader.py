from pupdb.core import ChordNode, Leader

def test_leader():
    m = 7  # Số bit trong ID của nút
    node_ids = [0, 25, 50, 75, 100, 125, 150, 175]
    nodes = []

    # Khởi tạo các nút Chord và tự động thiết lập successor
    for id in node_ids:
        ChordNode(id, m, f'db_{id}.json', nodes)

    # Khởi tạo lớp Leader
    leader = Leader(nodes)
    leader.chonLeader()

    # Lấy thông tin về lãnh đạo hiện tại
    current_leader = leader.layLeader()
    print(f'Leader ID: {current_leader.id}')

    # Thêm một nút mới vào hệ thống
    new_node = ChordNode(200, m, 'db_200.json', nodes)
    new_node.join(leader)

    # # Kiểm tra bảng ngón tay của các nút hiện có
    # for node in nodes:
    #     node.fingerTable()

    # Thêm dữ liệu vào hệ thống Chord
    start_node = nodes[0]
    for i in range(1, 250):
        start_node.set(i, f'value{i}')

    m = 5
    print(f'Key {m}:', start_node.get(m))

    print('nodes:', start_node.getNodes())

    # Kiểm tra các khóa trong hệ thống Chord
    keys = start_node.keys()
    print('Keys:', keys)

    # Kiểm tra các giá trị trong hệ thống Chord
    values = start_node.values()
    print('Values:', values)

    # Kiểm tra các cặp khóa-giá trị trong hệ thống Chord
    items = start_node.items()
    print('Items:', items)

    # Kiểm tra dump của cơ sở dữ liệu
    db_dump = start_node.dumps()
    print('Database dump:', db_dump)

    # # Xóa toàn bộ cơ sở dữ liệu
    # start_node.truncate_db()
    # print('Keys after truncate:', start_node.keys())

    # Tìm và in ra ID của nút chịu trách nhiệm quản lý một khóa cụ thể
    key_to_find = 154
    NODE = start_node.timNode(key_to_find)
    print(f"Key {key_to_find} được quản lí bởi {NODE.id}.")
    print(f"Giá trị của khóa {key_to_find} là {start_node.get(key_to_find)}.")

if __name__ == '__main__':
    test_leader()