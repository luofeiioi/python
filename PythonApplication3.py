import re
import urllib.request
import os

port=urllib.request.urlopen('https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F%E4%B9%8B%E7%BB%9D%E4%B8%96%E6%97%A0%E5%8F%8C&fr=index')
txt=port.read().decode('utf-8')

io=re.compile(r'target="_blank"\sclass="j_th_tit ">(.*)</a>')
ha=re.findall(io,txt)
jk=''
#print(ha)
for i in range(2,25):
    jk += str(i-1)+' '
    jk += ha[i]
    jk += '\n'

print(jk)

a = int(input('haha:'))
but = ha[a+1]
chang='href="(.*)"\stitle="'+but
print(chang)
qwer=re.compile(chang)
haa=re.findall(qwer,txt)
df='https://tieba.baidu.com'+haa[0]
print(df)



portt=urllib.request.urlopen(df)
txtt=portt.read().decode('utf-8')

iio=re.compile(r'class="d_post_content j_d_post_content ">(.*)</div><br>')
hea=re.findall(iio,txtt)


print(hea)


os.system("pause")
#name='绝世无双'+'.'+'txt'
#hj=open(name,'w')
#hj.write(jk)
#hj.close()