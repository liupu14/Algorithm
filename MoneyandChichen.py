for ii in range(1,21):
    for jj in range(1,34):
        zz = 100 - ii - jj
        if zz%3==0 and 5*ii + 3*jj + zz/3 ==100:
            print("公鸡是{},母鸡是{},小鸡是{}".format(ii,jj,zz))
