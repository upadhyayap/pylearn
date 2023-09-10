# The threading module was first introduced in Python 1.5.2 as an enhancement of the low-level thread module.
# The threading module makes working with threads much easier and allows the program to run multiple operations at once.

# Note that the threads in Python work best with I/O operations, such as downloading resources from the Internet or reading files and directories on your computer.
# If you need to do something that will be CPU intensive, then you will want to look at Python’s multiprocessing module instead.
# The reason for this is that Python has the Global Interpreter Lock (GIL) that basically makes all threads run inside of one master thread.
# Because of this, when you run multiple CPU intensive operations with threads, you may find that it actually runs slower.
# So we will be focusing on what threads do best: I/O operations!

from threading import Timer
import os
import subprocess
import threading
import logging


def doubler(number):
    """
    A function that can be used by a thread
    """
    print(threading.currentThread().getName() + '\n')
    print(number * 2)
    print()


if __name__ == '__main__':
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()
        # wait for the thread to finish
        my_thread.join()

# Creating a custom subclass
# You can also create a custom subclass of the Thread class and override the run() method.


class MyThread(threading.Thread):

    def __init__(self, number, logger):
        threading.Thread.__init__(self)
        self.number = number
        self.logger = logger

    def run(self):
        """
        Run the thread
        """
        logger.debug('Calling doubler')
        doubler(self.number, self.logger)


def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("threading_class.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


def doubler(number, logger):
    """
    A function that can be used by a thread
    """
    logger.debug('doubler function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(
        result))


if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    for i in range(5):
        thread = MyThread(i, logger)
        thread.setName(thread_names[i])
        thread.start()
        print(thread_names[i])

# using locks
# Locks are a very simple way to synchronize threads.
# A lock has two states: locked and unlocked.
# When the state is locked, it does not allow any other thread to enter the code section protected by the lock.
# When the state is unlocked, it allows another thread to enter the code section protected by the lock and then locks the state again.
# This is a very simple way to make sure that only one thread is accessing a shared resource at a time.
# The threading module provides a Lock class to deal with the locks.
# The Lock class has two methods: acquire() and release().
# The acquire() method locks the state and the release() method unlocks the state.
# The Lock class also has an __enter__() and __exit__() method that allows you to use the lock with the with statement.
# The __enter__() method calls the acquire() method and the __exit__() method calls the release() method.
# This is a very convenient way to use locks because it will automatically release the lock when the code block is finished.
# Here is an example of how to use a lock using the try and finally statement:
total = 0
lock = threading.Lock()


def update_total(amount):
    """
    Updates the total by the given amount
    """
    global total
    lock.acquire()
    try:
        total += amount
    finally:
        lock.release()
    print(total)


for i in range(10):
    my_thread = threading.Thread(
        target=update_total, args=(5,))
    my_thread.start()

# using the lock with the with statement
total = 0
# lock = threading.RLock() if you want to use a reentrant lock
lock = threading.Lock()


def update_total_with_lock(amount):
    """
    Updates the total by the given amount
    """
    global total
    with lock:
        total += amount
    print(total)


# Timer: The Timer class represents an action that should be run only after a certain amount of time has passed.


def kill(process): return process.kill()


print("OUTPUT WILL BE:")
print("kill: ", kill)
cmd = ['cat', 'main.py']


cmd = ['ping', 'www.google.com']
ping = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(ping)


my_timer = Timer(2, kill, [ping])

try:
    my_timer.start()
    stdout, stderr = ping.communicate()
finally:
    my_timer.cancel()


# semaphores: A semaphore is a synchronization object that controls access by multiple processes/threads to a common resource in a parallel programming environment.
semaphore = threading.Semaphore(2)


def func():
    semaphore.acquire()
    print(semaphore)
# Acquiring lock
    print("%s Lock acquired." % (threading.current_thread().name))
# Thread access decremented
    print("Available threads access: ", semaphore._value)
    semaphore.release()
# Releasing lock
    print("%s Lock released." % (threading.current_thread().name))
# Thread access incremented
    print("Available threads access: ", semaphore._value)


thread1 = threading.Thread(target=func)
thread2 = threading.Thread(target=func)
thread3 = threading.Thread(target=func)

thread1.start()
thread2.start()
thread3.start()
print("Main thread exited.", threading.main_thread())
