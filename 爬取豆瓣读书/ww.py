import find_book as fb
name = []
tran = []
out = []
date = []
price = []
ss = fb.imformation
for s in ss:
    v = s.split('/')
    if len(v) == 4:
        v.insert(1,'')
    name.append(v[0].strip())
    tran.append(v[1].strip())
    out.append(v[2].strip())
    date.append(v[3].strip())
    price.append(v[4].strip())