# #write alphabets and numbers to a file when a function is called 
# import threading
# import time
# def process_file(source_file):
#     f = open(source_file,"a")
#     f.write("abc def ghi jkl mno pqr uvw xyz\n")

#     time.sleep(5)
#     ff = open(source_file,"a")
#     ff.write("12 34 56 78 90\n")

# source_file = "fileeee.txt"
# # process_file(source_file)
# # process_file(source_file)

# thread1 = threading.Thread(target=process_file, args=(source_file,))
# thread2 = threading.Thread(target=process_file, args=(source_file,))
# thread3 = threading.Thread(target=process_file, args=(source_file,))
# thread4 = threading.Thread(target=process_file, args=(source_file,))
# thread5 = threading.Thread(target=process_file, args=(source_file,))

# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()

# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# print("file processing completed")


# ============================================
## if  from  threading import* is given write lock as  l = Lock()

# from  threading import*
# import time
# l = Lock()
# def process_file(source_file):
#     l.acquire()
#     f = open(source_file,"a")
#     f.write("abc def ghi jkl mno pqr uvw xyz\n")

#     time.sleep(5)
#     ff = open(source_file,"a")
#     ff.write("12 34 56 78 90\n")
#     l.release()

# source_file = "fileeee.txt"
# # process_file(source_file)
# # process_file(source_file)

# thread1 = threading.Thread(target=process_file, args=(source_file,))
# thread2 = threading.Thread(target=process_file, args=(source_file,))
# thread3 = threading.Thread(target=process_file, args=(source_file,))
# thread4 = threading.Thread(target=process_file, args=(source_file,))
# thread5 = threading.Thread(target=process_file, args=(source_file,))

# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()

# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# print("file processing completed")
# ===============================================
## if write , w is given it will get overwritten so append i
## if just  import threading is using then write lock as  l = threading.Lock()
# import threading
# import time
# l = threading.Lock()
# def process_file(source_file):
#     l.acquire()
#     f = open(source_file,"a")
#     f.write("abc def ghi jkl mno pqr uvw xyz\n")

#     time.sleep(5)
#     ff = open(source_file,"a")
#     ff.write("12 34 56 78 90\n")
#     l.release()

# source_file = "fileeee.txt"
# # process_file(source_file)
# # process_file(source_file)

# thread1 = threading.Thread(target=process_file, args=(source_file,))
# thread2 = threading.Thread(target=process_file, args=(source_file,))
# thread3 = threading.Thread(target=process_file, args=(source_file,))
# thread4 = threading.Thread(target=process_file, args=(source_file,))
# thread5 = threading.Thread(target=process_file, args=(source_file,))

# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()

# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# print("file processing completed")
# ==============================================


# inheriting from thread class 
# Mythread class is inherited from Thread class 
# instance of Mythread is created (my).When my.start() is called and if the 
# program has run method it will first run that
# from threading import*
# class Mythread(Thread):
#     def cube(self,a):
#         for i in a:
#             print("cube",i*i*i)
#     def square(self,a):
#         for i in a:
#             print("square",i*i)
#     def run(self):
#         a = [1,2,3,4,5]
#         self.cube(a)
#         self.square(a)

# my = Mythread()
# my.start()

# ===============================================
from threading import Thread
# class Mythread(Thread):
#     def __init__(self,a):
#         super().__init__()
#         self.a=a
#     def cube(self):
#         for i in self.a:
#             print("cube",i*i*i)
#     def square(self):
#         for i in self.a:
#             print("square",i*i)
#     def run(self):
#         t1 = Thread(target=self.cube)
#         t2 = Thread(target=self.square)
#         t1.start()
#         t2.start()
# a = [1,2,3,4,5]
# my = Mythread(a)
# my.start()
# my.join()
# connection oriented protocol
# =============================================
from threading import Thread,Lock
class Mythread(Thread):
    def __init__(self,a,lock):
        super().__init__()
        self.a=a
        self.lock = lock
    def cube(self):
        self.lock.acquire()
        for i in self.a:
            print("cube",i*i*i)
        self.lock.release()
    def square(self):
        self.lock.acquire()
        for i in self.a:
            print("square",i*i)
        self.lock.release()
    def run(self):
        t1 = Thread(target=self.cube)
        t2 = Thread(target=self.square)
        t1.start()
        t2.start()
a = [1,2,3,4,5]
my = Mythread(a,lock)
my.start()
my.join()

# ip address
# port number