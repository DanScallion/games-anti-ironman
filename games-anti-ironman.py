import shutil
import sys
from datetime import datetime
import os
import configparser
import argparse
from os import read


def backup():
    configParser = configparser.ConfigParser()
    configFilePath = "settings.ini"
    path = os.path.join(os.path.dirname(sys.argv[0]), configFilePath)
    configParser.read_file(open(path), 'w')
    currentGame = configParser.get('Settings', 'currentGame')
    filePath = configParser.get(currentGame, 'filePath')
    fileName = configParser.get(currentGame, 'fileName')
    fileType = configParser.get(currentGame, 'fileType')
    lastSave = configParser.get(currentGame, 'lastSave')
    shutil.copy(
        filePath + fileName + fileType,
        filePath + "/backup")
    file = fileName + "_" + datetime.today().strftime('%Y-%m-%d %H_%M_%S') + fileType
    os.rename(filePath + "backup/" + fileName + fileType, filePath + "backup/" + file)
    configParser.set(currentGame, 'lastSave', file)
    configParser.write(open(path, 'w'))


def load():
    configParser = configparser.ConfigParser()
    configFilePath = "settings.ini"
    path = os.path.join(os.path.dirname(sys.argv[0]), configFilePath)
    configParser.read_file(open(path), 'w')
    currentGame = configParser.get('Settings', 'currentGame')
    filePath = configParser.get(currentGame, 'filePath')
    fileName = configParser.get(currentGame, 'fileName')
    fileType = configParser.get(currentGame, 'fileType')
    lastSave = configParser.get(currentGame, 'lastSave')
    path2 = os.path.join(os.path.dirname(sys.argv[0]), configFilePath)
    os.remove(filePath + fileName + fileType)
    shutil.copy(
        filePath + "/backup/" + lastSave,
        filePath + fileName + fileType)

parser = argparse.ArgumentParser(description="Choose Action:")
parser.add_argument('-a', type=str,  required=False)
args = parser.parse_args()

if args.a == 'backup':
    backup()

if args.a == 'load':
    load()
