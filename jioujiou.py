for i in range(1,10):
    for t in range(1,i+1):
        print('{}x{}={}'.format(i, t, i * t), end='\t')
    print()