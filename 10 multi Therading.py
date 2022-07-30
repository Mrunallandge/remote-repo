from threading import Thread
def sample(): # it will execute by t1
    print('in sample function')

def test(): # it will execute by t2
    print('in test')

t1 = Thread(target=sample) # create thread t1
t2 = Thread(target=test) # create thread t2

t1.start()
t2.start()

print('in the file')  # it will execute by main