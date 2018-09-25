import numpy as np

def main():
    lst=[[1,3,5],[2,4,6]]
    print(type(lst))
    np_lst=np.array(lst)
    print(type(np_lst))
    np_lst=np.array(lst,dtype=np.float)
    print("shape=",np_lst.shape)
    print(np_lst.ndim)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)
    #2
    print(np.zeros([2,4]))
    print(np.ones([3, 5]))
    print(np.random.rand(2, 4))
    print(np.random.rand())
    print(np.random.randint(1,10,3))
    print(np.random.randn(2,4))
    print(np.random.choice([10,20,30]))
    print(np.random.beta(1,10,100))
    #3
    print(np.arange(1,11).reshape(2,-1))
    lst=np.arange(1, 11).reshape(2, -1)
    print(np.exp(lst))
    print(np.exp2(lst))
    print(np.sqrt(lst))
    print(np.sin(lst))
    print(np.log(lst))



if __name__=="__main__":
    main()