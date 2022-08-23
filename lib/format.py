#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# @name   : DragonPhone - Phone numbers OSINT tool
# @author : Shake / Nylux

import re


def formatNumber(InputNumber):
    return re.sub("(?:\+)?(?:[^[0-9]*)", "", InputNumber)


def replaceVariables(string, number):
    string = string.replace('$n', number['default'])
    string = string.replace('$i', number['international'])
    string = string.replace('$l', number['international'].replace(
        '%s ' % (number['countryCode']), ''))

    return string
