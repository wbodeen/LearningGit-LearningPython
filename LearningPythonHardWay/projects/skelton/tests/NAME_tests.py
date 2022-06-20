import unittest
import sys
sys.path.append('C:\\Users\\wbode\\Documents\\GitHubRepo\\LearningPythonHardWay\\projects\\NAME')


def setup():
    print("Setup!")

def teardown():
    print("Tear down!")

def test_basic():
    print("I ran!", end='')
    