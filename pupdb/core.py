"""
    Core module containing entrypoint functions for PupDB.
"""

import logging
import os
import json
import traceback

from filelock import FileLock

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(process)d | %(levelname)s | %(message)s'
)


# pylint: disable=useless-object-inheritance
class PupDB(object):

    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        self.process_lock_path = '{}.lock'.format(db_file_path)
        self.process_lock = FileLock(self.process_lock_path, timeout=-1)
        self.init_db()

    def __repr__(self):
        return str(self._get_database())

    def __len__(self):
        return len(self._get_database())

    def init_db(self):
        with self.process_lock:
            if not os.path.exists(self.db_file_path):
                with open(self.db_file_path, 'w') as db_file:
                    db_file.write(json.dumps({}))
        return True

    def _get_database(self):
        with self.process_lock:
            with open(self.db_file_path, 'r') as db_file:
                database = json.loads(db_file.read())
                return database

    def _flush_database(self, database):
        with self.process_lock:
            with open(self.db_file_path, 'w') as db_file:
                db_file.write(json.dumps(database))
                return True

    def set(self, key, val):
        try:
            database = self._get_database()
            database[key] = val
            self._flush_database(database)
        except Exception:
            logging.error(
                'Error while writing to DB: %s', traceback.format_exc())
            return False
        return True

    def get(self, key):
        key = str(key)
        database = self._get_database()
        return database.get(key, None)

    def remove(self, key):
        key = str(key)
        database = self._get_database()
        if key not in database:
            raise KeyError(
                'Non-existent Key {} in database'.format(key)
            )
        del database[key]

        try:
            self._flush_database(database)
        except Exception:
            logging.error(
                'Error while writing to DB: %s', traceback.format_exc())
            return False
        return True

    def keys(self):
        return self._get_database().keys()

    def values(self):
        return self._get_database().values()

    def items(self):
        return self._get_database().items()

    def dumps(self):
        return json.dumps(self._get_database(), sort_keys=True)

    def truncate_db(self):
        self._flush_database({})
        return True

class ChordNode:
    def __init__(self, id, m, db_file_path, nodes):
        self.id = id
        self.m = m
        self.db = PupDB(db_file_path)
        self.finger_table = []
        self.succ = None
        self.nodes = nodes
        nodes.append(self)
        self.tinhFingerTable(nodes)
        self.setSucc(nodes[(nodes.index(self) + 1) % len(nodes)])

    def tinhFingerTable(self, nodes):
        for i in range(1, self.m + 1):
            p = (self.id + 2**(i - 1)) % (2**self.m)
            successor = self.timSucc(p, nodes)
            self.finger_table.append(successor)

    def timSucc(self, id, nodes):
        for node in sorted(nodes, key=lambda x: x.id):
            if node.id >= id:
                return node
        return nodes[0]

    def setSucc(self, succ):
        self.succ = succ

    def timNode(self, key):
        key = int(key)
        if self.id <= key < self.succ.id or (self.id > self.succ.id and (key >= self.id or key < self.succ.id)):
            return self.succ
        else:
            for finger in reversed(self.finger_table):
                if finger.id > self.id and finger.id <= key:
                    return finger.timNode(key)
            return self.succ.timNode(key)

    def fingerTable(self):
        print(f"Node {self.id} Finger Table:")
        print("i   |   Node ID")
        for i, node in enumerate(self.finger_table):
            print(f"{i + 1}   |   {node.id}")
        print()

    def set(self, key, value):
        key1 = ((int)(key) % 100)
        NODE = self.timNode(key1)
        NODE.db.set(key, value)

    def get(self, key):
        NODE = self.timNode(key)
        return NODE.db.get(key)

    def remove(self, key):
        NODE = self.timNode(key)
        return NODE.db.remove(key)

    def keys(self):
        all = []
        for node in self.nodes:
            all.extend(node.db.keys())
        return all

    def values(self):
        all = []
        for node in self.nodes:
            all.extend(node.db.values())
        return all

    def items(self):
        all = []
        for node in self.nodes:
            all.extend(node.db.items())
        return all

    def dumps(self):
        all = {}
        for node in self.nodes:
            all.update(node.db._get_database())
        return json.dumps(all, sort_keys=True)

    def truncate_db(self):
        for node in self.nodes:
            node.db.truncate_db()
        return True
    
    def getNodes(self):
        return [node.id for node in self.nodes]

    def join(self, leader):
        leader.themNut(self)

class Leader:
    def __init__(self, nodes):
        self.nodes = nodes
        self.leader = None

    def chonLeader(self):
        self.leader = max(self.nodes, key=lambda node: node.id)

    def layLeader(self):
        return self.leader

    def themNut(self, node):
        for n in self.nodes:
            n.tinhFingerTable(self.nodes)
        for i, n in enumerate(self.nodes):
            n.setSucc(self.nodes[(i + 1) % len(self.nodes)])