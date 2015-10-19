#!/usr/bin/env python
# encoding:utf-8

# Copyright (C) 2010-2013 Magima Co Ltd. All rights reserved.
#
# @description
#
# @file        confParser.py
# @author      0294
# @date        2014-12-24 09:56
# @version     1.0

import ConfigParser

class Configuration(object):

    ''' This class have functions to iterate config files
        and fetch the available values.
     '''

    def __init__(self, path):

        self.__GLOBAL='global'

        self.__config = None
        self.__all_data = {}
        self.__host_info = {}
        self.__global_info = None

        self.__config = ConfigParser.RawConfigParser()
        self.__config.read(path)

        self.__sections = self.__config.sections()

        for section in self.__sections:
            kvs = self.__config.items(section)
            self.__all_data[section] = dict(kvs)

    def getAllConfigData(self):
        return self.__all_data

