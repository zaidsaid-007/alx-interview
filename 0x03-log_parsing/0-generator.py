#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

NUM_LOGS = 10000
IP_RANGE = (1, 255)
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]
DATA_SIZE_RANGE = (1, 1024)

for i in range(NUM_LOGS):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(*IP_RANGE), random.randint(*IP_RANGE), random.randint(*IP_RANGE), random.randint(*IP_RANGE),
        datetime.datetime.now(),
        random.choice(STATUS_CODES),
        random.randint(*DATA_SIZE_RANGE)
    ))
    sys.stdout.flush()