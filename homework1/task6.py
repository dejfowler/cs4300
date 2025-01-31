def word_count(filename):
    with  open(filename, "r") as f:
        lst = f.read().replace(","," ")
        lst = lst.replace("."," ")
        print(len(lst.split()))
        return len(lst.split())