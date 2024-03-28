import project
import datetime
import unittest
import csv
import tabulate

def test_tod():
    assert project.tod(['Wednesday'], datetime.date(2024,3,27)) == True
    assert project.tod(['Wednesday'], datetime.date(2024,3,28)) == False
    assert project.tod(['Monday', 'Wednesday'], datetime.date(2024,3,27)) == True
    assert project.tod(['Monday', 'Wednesday'], datetime.date(2024,3,28)) == False

def test_view():
    assert project.view('test.csv') == tabulate.tabulate([['test', 'test', 'test', '1']], headers=project.FIELDS, tablefmt='fancy_grid')
    assert project.view('test2.csv') == tabulate.tabulate([['test', 'test', 'test', '0'], ['test', 'test', 'test', '2']], headers=project.FIELDS, tablefmt='fancy_grid')

def test_cr