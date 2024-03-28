import project
import datetime
from unittest.mock import patch
import tabulate
import os
import csv
from itertools import cycle

def test_tod():
    assert project.tod(['Wednesday'], datetime.date(2024,3,27)) == True
    assert project.tod(['Wednesday'], datetime.date(2024,3,28)) == False
    assert project.tod(['Monday', 'Wednesday'], datetime.date(2024,3,27)) == True
    assert project.tod(['Monday', 'Wednesday'], datetime.date(2024,3,28)) == False

def test_createcsv():
    project.createcsv('test.csv')
    assert os.path.exists('test.csv') == True

def test_create():
    hdate = datetime.date.today()
    with patch('builtins.input', side_effect=cycle(['test','7','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])):
        project.create('test.csv')
    with open('test.csv', 'r') as f:
        reader = list(csv.reader(f))
        assert reader == [['test', "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']", hdate.isoformat(), '0']]

def test_log():
    with patch('builtins.input', side_effect='test'):
        project.log('test.csv')
    with open('test.csv', 'r') as f:
        reader = list(csv.reader(f))
        assert reader == [['test', "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']", datetime.date.today(), '1']]


def test_view():
    assert project.view('test.csv') == tabulate.tabulate([['test', "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']", '2024-03-28', '1']], headers=project.FIELDS, tablefmt='fancy_grid')
