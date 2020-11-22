import multiprocessing


def down_load_from_web(q):
    '''模拟从网上下载数据'''
    data = [11,22,33,44,55]

    #向队列中写数据
    for temp in  data:
        q.put(temp)
    print('------下载器已经下载数据完成，并且存放到队列中---')


def anaiysis(q):
    '''数据分析'''
    # 从队列中获取数据
    waitting_analysis = list()
    while True:
        data = q.get()
        waitting_analysis.append(data)
        if q.empty():
            break

    print(waitting_analysis)


def main():

    # 1. 创建一个队列
    q = multiprocessing.Queue()


    # 2.创建多个进程，将 队列的引用 当做实参进行传递到里面

    p1 = multiprocessing.Process(target=down_load_from_web,args=(q,))
    p2 = multiprocessing.Process(target= anaiysis,args=(q,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()

