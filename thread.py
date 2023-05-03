print('The main thread executes the code') 

from threading import Thread
from time import sleep


def threadFunc(arg1,arg2):
    print('The child thread starts')
    print(f'The thread function parameter is:{arg1}, {arg2}')
    sleep(5)
    print('Thread end')


thread = Thread(
   
    target=threadFunc, 


    args=('Parameter 1', 'Parameter 2')
)


thread.start()


thread.join()
print('Main thread end')
