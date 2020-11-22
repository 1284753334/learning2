
#   顺序查找
def Linear_search(li,val):
    for i in range(len(li)):
        if li[i] == val:
            return i
    return -1
if __name__ == '__main__':
    li=[1,2,3,4,5]
    result = Linear_search(li,5)
    print(result)


