#!/usr/bin/python

import logging

logformat = "%(levelname)s %(asctime)s -  %(message)s"

logging.basicConfig(filename = '/home/sally/logger/info.log',level = logging.INFO ,format = logformat)
logger  = logging.getLogger()
logger.info("إغتصاب الطفلات أقل من 6 أشهر")
