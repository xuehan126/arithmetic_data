from timeit import Timer


# 加法
def t1():
        list1 = []
            for i in range(1000):
                        list1 = list1 + [i]


                        # append
                        def t2():
                                list2 = []
                                    for i in range(1000):
                                                list2.append(i)


                                                # 列表生成器
                                                def t3():
                                                        list3 = [i for i in range(1000)]


                                                        # list方法
                                                        def t4():
                                                                list4 = list(range(1000))


                                                                timer1 = Timer(stmt='t1()', setup='from __main__ import t1')
                                                                timer1.timeit(1000)
                                                                print('+ method：', timer1.timeit(1000))

                                                                timer2 = Timer(stmt='t2()', setup='from __main__ import t2')
                                                                timer2.timeit(1000)
                                                                print('append method:', timer2.timeit(1000))

                                                                timer3 = Timer(stmt='t3()', setup='from __main__ import t3')
                                                                timer3.timeit(1000)
                                                                print('列表生成器 method', timer3.timeit(1000))

                                                                timer4 = Timer(stmt='t4()', setup='from __main__ import t4')
                                                                timer4.timeit(1000)
                                                                print('直接list：', timer4.timeit(1000))
