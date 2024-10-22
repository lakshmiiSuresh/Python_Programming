# there are three files source.txt,file1.txt,file2.txt.
# write a function to read from source.txt and write it to file1.txt firstly 
# and then to file2.txt
# import time
# def files(a,b):
#     f = open(a,"r")
#     z =f.read()
#     time.sleep(5)
#     f = open(b,"w")
#     f.write(z)
#     f.close()

# files("source.txt","file1.txt")
# files("source.txt","file2.txt")


# ==========================
# using thread
import threading
import time
def files(a,b):
    f = open(a,"r")
    z =f.read()
    time.sleep(5)
    f = open(b,"w")
    f.write(z)
    f.close()

file1 = "source.txt"
file2 = "file1.txt"
file3 = "file2.txt"
thread1 = threading.Thread(target=files, args=(file1, file2))
thread2 = threading.Thread(target=files, args=(file1, file3))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("file processing completed")
