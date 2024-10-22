# import time
# def cube(l1):
#     for i in l1:
#         time.sleep(1)
#         print("cube of:",i,"is",i**3)

# def square(l1):
#     for i in l1:
#         time.sleep(1)
#         print("square of:",i,"is",i**2)

# l1 = [1,2,3,4,5]
# t1 = time.time()
# cube(l1)
# square(l1)
# print(time.time()-t1)


# import time
# import threading
# def cube(l1):
#     for i in l1:
#         time.sleep(1)
#         print("cube of:",i,"is",i**3)

# def square(l1):
#     for i in l1:
#         time.sleep(1)
#         print("square of:",i,"is",i**2)

# l1 = [1,2,3,4,5]
# tt = time.time()
# t1 = threading.Thread(target=cube,args=(l1,))
# t2 = threading.Thread(target=square,args=(l1,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# # cube(l1)
# # square(l1)
# print(time.time()-tt)



# ===============================
import time
import threading
def cube(l1):
    for i in l1:
        time.sleep(1)
        print("cube of:",i,"is",i**3)

def square(l1):
    for i in l1:
        time.sleep(1)
        print("square of:",i,"is",i**2)

l1 = [1,2,3,4,5]
tt = time.time()
t1 = threading.Thread(target=cube,args=(l1,))
t2 = threading.Thread(target=square,args=(l1,))
t1.start()
t2.start()
print(threading.active_count())
t1.join()
t2.join()
# cube(l1)
# square(l1)
print(threading.active_count())
print(time.time()-tt)
print(threading.active_count())

# ============================

# ===============================
import time
import threading
def cube(l1):
    for i in l1:
        time.sleep(1)
        print("cube of:",i,"is",i**3)
        print(threading.current_thread())
        print(t1.getName())

def square(l1):
    for i in l1:
        time.sleep(1)
        print("square of:",i,"is",i**2)
        print(threading.current_thread())
        print(t2.getName())

l1 = [1,2,3,4,5]
tt = time.time()
t1 = threading.Thread(target=cube,args=(l1,))
t2 = threading.Thread(target=square,args=(l1,))
t1.start()
t2.start()
t1.setName("first thread")
t2.setName("second thread")

print(threading.active_count())
t1.join()
t2.join()
# cube(l1)
# square(l1)
print(threading.active_count())
print(time.time()-tt)
print(threading.active_count())