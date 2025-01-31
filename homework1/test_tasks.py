import subprocess
import requests
import task2
import task3
import task4
import task5
import task6
import task7

def test_task1():
    result = subprocess.run(["./task1.py"], capture_output=True, text=True)
    assert result.stdout == "Hello, World!\n"

def test_task2():
    assert type(task2.integer) == int
    assert type(task2.floater) == float
    assert type(task2.boolean) == bool
    assert type(task2.string) == str

def test_task3():
    assert task3.primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task3.sum == 5050

def test_task4():
    assert task4.calculate_discount(100,.20) == 80.0
    assert task4.calculate_discount(10.95,5) == 10.4
    assert task4.calculate_discount(73,50) == 36.5
    assert task4.calculate_discount(13.99, 35) == 9.09
    assert task4.calculate_discount(17.49,.80) == 3.5

def test_task5():
    assert len(task5.library_of_congress()) == 3
    assert type(task5.library_of_congress()) == list
    assert type(task5.db) == dict

def pytest_generate_tests(metafunc):
    
    if "input" in metafunc.fixturenames:
        metafunc.parametrize("input, expected", [
            ("task6_read_me.py", 104)
        ], ids=[f"wordcount_of_{x}" for x in ["task6_read_me.py"]])

def test_task6(input, expected):
    assert task6.word_count(input) == expected

def test_task7():
    url = "https://www.google.com"
    assert task7.geturl(url).ok == requests.get(url).ok