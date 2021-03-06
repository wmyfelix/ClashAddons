#!/usr/bin/python3
# -*- coding: utf-8 -*-

# run() ex. 
# RegExp: [6x]
# <proxy group>'s <proxies>
# ChinaG's [6x]HKT --> ChinaG_6x's [6x]HKT

import re
import os
import yaml

class SafeLoaderIgnoreUnknown(yaml.SafeLoader):
    def ignore_unknown(self, node):
        return None 

SafeLoaderIgnoreUnknown.add_constructor(None, SafeLoaderIgnoreUnknown.ignore_unknown)


def get_name(content):
    ret = {}
    for x in yaml.load(content, Loader=SafeLoaderIgnoreUnknown)['proxies']:
        ret[x['name']] = x
    return ret


def rename_original(path):
    _file_All = path + '_All'
    if os.path.exists(_file_All):
        os.remove(_file_All)
    os.rename(path, _file_All)


def rm_old(path):
    exec_path = path + '_'
    if os.path.isdir(exec_path):
        for root, dirs, files in os.walk(exec_path):
            for file in files:
                os.remove(os.path.join(root, file))
            for dirc in dirs:
                os.remove(os.path.join(root, dirc))
    else:
        os.makedirs(exec_path)


def dumper(list_dict, file):
    _dump = dict()
    _dump['proxies'] = list_dict
    # allow_unicode = True : fix emoji and etc...
    yaml.dump(_dump, file, allow_unicode=True)


def run(syx, file_path):
    _in = {}
    _plain = []
    _matched_list = []
    file_name = file_path.split('/')[-1]
    print("processing: ", file_path)
    rm_old(file_path)
    with open(file_path) as f:
        f = f.read()
        for x, y in get_name(f).items():
            # re.search.group() only return the first matched match.
            matched = re.search(syx, x, re.IGNORECASE)
            if matched:
                if matched.group() not in _matched_list:
                    _matched_list.append(matched.group())
                    _in[matched.group()] = [y]
                else:
                    _in[matched.group()] += [y]

            else:
                _plain.append(y)
    if _matched_list == []:
        print("pattern cannot be matched.")
    else:
        print('Matched: ', _matched_list)
        # rename_original(file_path)
        for x, y in _in.items():
            with open('{}_/{}_{}'.format(file_path, file_name, x), 'w') as f:
                dumper(y, f)
        if _plain != []:
            with open('{}_/{}_plain'.format(file_path, file_name), 'w') as f:
                dumper(_plain, f)
