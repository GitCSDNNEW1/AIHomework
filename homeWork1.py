'''
打乱数据集
同时打乱 x,y，保证数据和标签的对应关系
'''
import random
x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']


def shuffle(x,y):
    #获取索引
    index = [i for i in range(len(x))]
    #打乱索引，根据索引输出新的列表，保证一一对应
    random.shuffle(index)
    x = [x[n] for n in index]
    y = [y[n] for n in index]
    return x,y

if __name__=='__main__':
    #调用函数
    x,y = shuffle(x,y)

    # print result for certify
    for i,j in zip(x,y):
        print(i,':',j)