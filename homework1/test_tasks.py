import subprocess
import task2
import task3

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