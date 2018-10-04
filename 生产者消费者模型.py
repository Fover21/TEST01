from multiprocessing import Process, JoinableQueue


def producer(name, food, q):
	for i in range(10):
		info = '%s生产%s %s' % (name, food, i)
		print(info)
		q.put(info)
	q.join()


def consumer(q, name):
	while 1:
		food = q.get()
		info = "%s消费了%s" % (name, food)
		print(info)
		q.task_done()


if __name__ == '__main__':
	q = JoinableQueue()
	p1 = Process(target=producer, args=('Tom', '包子', q))
	p1.start()
	p2 = Process(target=producer, args=('Jack', '饺子', q))
	p2.start()
	c1 = Process(target=consumer, args=(q, 'i1'))
	c2 = Process(target=consumer, args=(q, 'i2'))
	c1.daemon = True
	c2.daemon = True
	c1.start()
	c2.start()
	# p1.join()


# from multiprocessing import Process, JoinableQueue


# def consumer(q, name):
#     while 1:
#         info = q.get()
#         print("%s吃了" % name + info)
#         q.task_done()


# def producer(q, name):
#     for i in range(10):
#         info = '%s生产了%s号包子' % (name, i)
#         q.put(info)
#     q.join()


# if __name__ == '__main__':
#     q = JoinableQueue(10)
#     pro = Process(target=producer, args=(q, 'Tom',))
#     con = Process(target=consumer, args=(q, 'Jake'))
#     con1 = Process(target=consumer, args=(q, 'Jason'))
#     con.daemon = True  # 有几个消费者就有几个守护进程
#     con1.daemon = True
#     con1.start()
#     con.start()
#     pro.start()
#     pro.join()
