# import threading 
# x=0
# def increment():
#     global x
#     for i in range(10):
#         x+=1
#         print(x)
# # increment()
# # increment()
# def main():
#     global x 
#     t1 = threading.Thread(target=increment)
#     t2 = threading.Thread(target=increment)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# main()
# main()

# # =======================================================
# import threading 
# x=0
# def increment():
#     global x
#     for i in range(100000):
#         x+=1
#         # print(x)
# # increment()
# # increment()
# def main():
#     global x 
#     x = 0
#     t1 = threading.Thread(target=increment)
#     t2 = threading.Thread(target=increment)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# for i in range(10):
#     main()
#     print("itretion {0}: x={1}".format(i,x))

# =============================================================
import threading 
x=0
def increment(lock):
    global x
    lock.acquire()
    for i in range(100000):
        x+=1
    lock.release()
        # print(x)
# increment()
# increment()
def main():
    lock = threading.Lock()
    global x 
    x = 0
    t1 = threading.Thread(target=increment,args=(lock,))
    t2 = threading.Thread(target=increment,args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
for i in range(10):
    main()
    print("itretion {0}: x={1}".format(i,x))


# Without synchronization, race conditions could occur, where two or more threads try to access and 
# modify shared resources concurrently, leading to unpredictable and incorrect behavior.

# A critical section is a part of the code where shared resources (like variables, files, or data structures) 
# are accessed or modified. 
# If multiple threads try to execute a critical section simultaneously, 
# it can lead to a race condition, where the outcome depends on the order 
# in which the threads are scheduled to run.

# A race condition occurs when multiple threads attempt to modify shared resources at the same time, 
# leading to inconsistent results. This happens because the threads "race" to access the resource, 
# and the result may depend on the unpredictable timing of thread execution.
# To prevent race conditions and ensure thread safety, we can use thread synchronization mechanisms.

# In Python, the threading module provides synchronization tools like Locks to prevent multiple threads 
# from executing a critical section at the same time.

# A lock is a synchronization primitive used to protect the critical section.
#  Only one thread can acquire a lock at a time, and other threads trying
#  to acquire the same lock will be blocked until the lock is released.

# Here is how it works:
# A thread acquires the lock before entering the critical section.
# Once the lock is acquired, no other thread can enter the critical section until the lock is released.
# The thread releases the lock after it is done with the critical section.