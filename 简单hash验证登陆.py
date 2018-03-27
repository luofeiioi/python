import hashlib

def hashh(wo):
    jj=hashlib.sha256(bytes(wo,encoding='utf-8'))
    return jj.hexdigest()


def sign(user,password):
    with open('ha','a',encoding='utf-8') as o:
        temp=user+'|'+hashh(password)+'\n'
        o.write(temp)

def read(bn,nb):
    with open('ha','r',encoding='utf-8') as f:
        for line in f:
            j,k=line.strip().split('|')
            if bn== j and hashh(nb)==k:
                return True
            else:
                return False
            




i=input('1,注册\n2,登陆\n')

if i=='1':
    us=input('shutu')
    pa=input('shuru')
    sign(us,pa)



elif i=='2':
    uss=input('shutu')
    paa=input('shuru')

    if read(uss,paa):
        print('yes')
    else:
        print('no')


