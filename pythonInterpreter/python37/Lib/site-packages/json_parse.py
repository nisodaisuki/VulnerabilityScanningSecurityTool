#!/usr/local/env python3
#coding: utf-8



import json
import sys


class Jsonparse(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        file = open(self.file_path, 'rb')
        jsonfile = json.load(file)
        # print(jsonfile['tomcat'])
        # print(jsonfile)
        return jsonfile


# def main():
#     obj = Jsonparse('./config.json')
#     obj.parse()

# if __name__ == '__main__':
#     main()
