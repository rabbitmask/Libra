#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import logging

logging.basicConfig(filename='Libra.log',
                    format='%(asctime)s %(message)s',
                    filemode="a", level=logging.INFO)

def loglog(log):
    logging.info(log)

