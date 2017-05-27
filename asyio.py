import asyncio
'''
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
import time

now = lambda : time.time()

async def do_some_work(x):
    print('wating: ', x)
    await asyncio.sleep(x)
    return 'i have done %d' % x

async def do_some_work1():
    for i in range(30):
        print('hello', i)

def callback(future):
    print('callback: ', future.result())

start = now()

#coroutine = do_some_work(2)
'''
loop = asyncio.get_event_loop()
#task = asyncio.ensure_future(coroutine)
task = loop.create_task(coroutine)
task1 = loop.create_task(do_some_work1())
tasks = [task, task1]

task.add_done_callback(callback)
'''
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)
'''
tasks = [asyncio.ensure_future(coroutine1),
         asyncio.ensure_future(coroutine2),
         asyncio.ensure_future(coroutine3)]
'''
loop = asyncio.get_event_loop()
task1 = loop.create_task(coroutine1)
task2 = loop.create_task(coroutine2)
task3 = loop.create_task(coroutine3)
tasks = [task1, task2, task3]
task1.add_done_callback(callback)
task2.add_done_callback(callback)
task3.add_done_callback(callback)
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('Task ret: ', task.result())
print('Time: ', now() - start)