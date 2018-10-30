#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/10/30 9:32 PM

__author__ = 'Miracle'

import threading, time, logging
from flask import Flask, Response
import json

app = Flask(__name__)
logging.basicConfig(format='%(threadName)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)


@app.route('/<name>', methods=['GET'])
def th_fn(name):
    logger.info('receive response')
    time.sleep(10)
    # t = threading.Thread(target=lambda: print('after sleep 30s'), args=(), name=name, daemon=True)
    logger.info('after sleep 30s')
    # t.start()
    return Response(response='succeed')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# starts = [threading.Thread(target=th_fn, args=(f't{t}',), name=f'Thread-{t}', daemon=True) for t in range(2)]
# for t in ts:
#     t.start()
#
# for t in ts:
#     t.join()
#
# print('end')
