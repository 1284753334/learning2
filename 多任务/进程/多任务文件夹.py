import multiprocessing
import os
#
# os.mkdir('newdir')
# with open('./newdir/douban.txy','w') as f:
#     f.write('abc  test')
from multiprocessing.pool import Pool



def copy_file(q,file_name,old_folder_name,new_floder_name):
    ''' 完成文件的复制'''
    # print('=====正在复制文件：从%s===>到%s  文件名是:%s' (old_folder_name,new_floder_name,file_name))
   # 读取文件
    with open(old_folder_name+'/'+file_name,'rb') as f:
        content = f.read()
    # 写入文件
    with open(new_folder_name +'/'+file_name,'wb') as f:
        f.write(content)

    #如果拷贝完了文件，那么就像队列中写入一个消息，表示已经完成
    q.put(file_name)

def main():
    # 1.获取用户要copy的文件夹的名字
    old_folder_name = input('请输入要拷贝的文件夹的名字:')

    #2.创建文件夹
    try:
        new_floder_name =old_folder_name+'[复件]'
        os.mkdir(new_floder_name)
    except:
        pass

    # 3.获取文件夹里所有待copy的 文件名字，  listdir()
    file_names = os.listdir(old_folder_name)
    # print(file_names)

    #  4.创建进程池
    po= Pool(5)


    # 5创建一个队列
    q = multiprocessing.Manager().Queue()

    # 6 向进程池中添加copy 文件的任务
    for file_name in  file_names:
        po.apply_async(copy_file, args=(file_name,old_folder_name,new_floder_name))


    po.close()
    # po.join()
    #  测一下所有文件个数
    all_file_num=len(file_name)
    copy_ok_num = 0
    while True:
        file_name =  q.get(file_name)
        copy_ok_num +=1
        print('\r拷贝的进度为:%.2f %%' % (copy_ok_num*100 / all_file_num),end='')
        if copy_ok_num<=all_file_num:
            break

    print()



if __name__ == '__main__':
    main()





