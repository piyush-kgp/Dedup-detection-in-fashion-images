
import time
import threading
import multiprocessing
# from multiprocessing.pool import ThreadPool
import itertools

def cal_square(num1, num2):
	time.sleep(0.5)
	print('squred is %s' %(num1**2 + num2**2))


alist = list(range(100))
blist = list(range(15, 115))
clist = [(alist[i], blist[i]) for i in range(len(alist))]

tit = time.time()
# thr = threading.Thread(target = cal_square, args = dict(zip(alist, blist)))
# thr.join()

pool = multiprocessing.Pool()
results = pool.starmap(cal_square, clist)
tat=time.time()
print('Time taken with MP is %s' %(tat-tit)) #5.034847021102905
