#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/20/18 2:48 PM
# @Author  : Miracle Young
# @File    : hash_sort.py


def hash_find(ascii_str, slot):
    _sum = 0
    for _s in ascii_str:
        _sum += ord(_s)
    return _sum % slot


class HashTable:
    def __init__(self):
        self._size = 11
        self.slots = [None] * self._size
        self.data = [None] * self._size

    def put(self, key, value):
        _hash = self._hash(key, len(self.slots))
        if self.slots[_hash] == None:
            self.slots[_hash] = key
            self.data[_hash] = value
        else:
            if self.slots[_hash] == key:
                self.data[_hash] = value
            else:
                _nextslot = self._rehash(_hash, len(self.slots))
                while self.slots[_nextslot] != None and self.slots[_nextslot] != key:
                    _nextslot = self._rehash(_nextslot, len(self.slots))

                if self.slots[_nextslot] == None:
                    self.slots[_nextslot] = key
                    self.data[_nextslot] = value
                else:
                    self.data[_nextslot] = value

    def _hash(self, key, size):
        return key % size

    def _rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        _startslot = self._hash(key, len(self.slots))

        _data = None
        _stop, _found = False, False
        _pos = _startslot
        while self.slots[_pos] != None and not _stop and not _found:
            if self.slots[_pos] == key:
                _found = True
                _data = self.slots[_pos]
            else:
                _pos = self._rehash(_pos, len(self.slots))
                if _pos == _startslot:
                    _stop = True
        return _data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == '__main__':
    print(hash_find('cat', 11))
