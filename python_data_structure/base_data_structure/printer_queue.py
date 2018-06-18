#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/18 11:29 AM
# @Author  : Miracle Young
# @File    : printer_queue.py


import random

from python_data_structure.base_data_structure.queue import Queue


class Task:
    def __init__(self, init_ts):
        # create task time
        self._init_ts = init_ts
        self._pages = random.randrange(1, 21)

    def get_stamp(self):
        return self._init_ts

    def get_pages(self):
        return self._pages

    # time to wait to execute print
    def wait_time(self, current_time):
        return current_time - self._init_ts

    @classmethod
    def new_task(cls):
        _num = random.randrange(1, 181)
        return _num == 180


class Printer:
    def __init__(self, pagerate):
        # 60s can do how many tasks
        self._pagerate = pagerate
        self._current_task = None
        # current time, printer need times to finish job
        self._time_remaining = 0

    # simulate task working
    def tick(self):
        if self._current_task is not None:
            self._time_remaining -= 1
            if self._time_remaining <= 0:
                self._current_task = None

    def busy(self):
        return self._current_task is not None

    # execute next job in the queue
    def start_next(self, new_task: Task):
        self._current_task = new_task
        self._time_remaining = self._current_task.get_pages() * 60 / self._pagerate


def simulation(total_seconds, pagerate):
    # init a printer
    _printer = Printer(pagerate)
    _task_queue = Queue()
    # store total time that all tasks waiting time
    _wait_time = []

    # _current_second to record init time
    for _current_second in range(total_seconds):
        if Task.new_task():
            # init one task, record init time
            _task = Task(_current_second)
            _task_queue.enqueue(_task)

        if (not _printer.busy()) and (not _task_queue.is_empty()):
            _next_task = _task_queue.dequeue()
            _wait_time.append(_next_task.wait_time(_current_second))
            _printer.start_next(_next_task)

        _printer.tick()

    _avg_time = sum(_wait_time) / len(_wait_time)
    print(f"Average Wait {_avg_time:6.2f} secs {_task_queue.size():3d} tasks remaining.")


if __name__ == '__main__':
    for _ in range(10):
        simulation(3600, 10)
