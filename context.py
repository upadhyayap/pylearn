from contextlib import contextmanager

# with keyword is used for context management
# with open("data.txt", "r") as f:
#     print(f.read())
# What is context managment ?
# well, it allows to set something up and tear it down automatically
# There are two magic methods that are __enter__ and __exit__
# when you use with keyword, it will call __enter__ method and when you exit the block, it will call __exit__ method
# a custom context manager would look like


class DBConn:
    def __init__(self) -> None:
        self.conn = None

    def __enter__(self):
        self.conn = "Opening connection"
        return self.conn

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn = "Closing connection"
        return self.conn


with DBConn() as db:
    print(db)

with open("data_types.py", "r") as f:
    print(f.read())

# contextlib: a module that provides utilities for common tasks involving the with statement
# contextlib.contextmanager: a decorator that can be used to define a factory function for with statement context managers


@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        f_obj.close()


if __name__ == '__main__':
    with file_open('test.txt') as fobj:
        fobj.write('Testing context managers')
