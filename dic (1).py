'''#python dictionary
Dict={}
Dict2=dict()
Dict3=dict([1,'one'),(2,2),(3,[1,2]),(4,(1,2)),(5,{1,2})])
Dict4=dict(1,'one'),(2,2),(3,[1,2]),(4,(1,2)),(5,{1,2})
Dict5=dict(one=1,two=2,Three=3)
Dict6=dict(1,'one',one=1,two=2,three=3)
Dict7={1:'one',2:2,3:[1,2],4:(1,2),5:{1,2}}
Dict8={1:'one',2:2,3:[1,2],4:(1,2),5:{1,2},1:'Two'}
Dict9={1:'a','b':'c',(2,3):'List'}
print('Dict1:',Dict1,'type:',type(Dict1))
print('Dict2:',Dict2,'type:',type(Dict2))
print('Dict3:',Dict3,'type:',type(Dict3))
print('Dict4:',Dict4,'type:',type(Dict4))
print('Dict5:',Dict5,'type:',type(Dict5))
print('Dict6:',Dict6,'type:',type(Dict6))
print('Dict7:',Dict7,'type:',type(Dict7)),'len:',len(Dict7))
print('Dict8:',Dict8,'type:',type(Dict8)),'len:',len(Dict8))
print('Dict9:',Dict9,'type:',type(Dict9))
print(Dict7[1],Dict8[1])'''
'''#Dictionary operators
D1={1:'v1',2:'v2'}
D2={'a':'val1','b':'val2'}
for i in D1:
    print(i,D1[i])
for i in D2:
    print(i,D2[i])
print('D1[1]:',D1[1])
print('D1[2]:',D1[2])
print('D2[1]:',D2['a'])
print('D2[2]:',D2['b'])
D1[1]='New1'
D1['a']='New key1'
D1['b']='New key2'
print('D1:',D1)
D2['a']='New key1'
D2['b']='New key2'
print('D2:',D2)'''
'''#Built in methods
#min(),max(),len(),del()
D1={1:'v1',2:'v2'}
D2={'a':'val1','b':'val2'}
D3={1:'v1',2:'v2','a':'val1','b':'val2'}
print('min D1:',min(D1))
print('min D2:',min(D2))
print('max D1:',max(D1))
print('max D2:',max(D2))
print('len D1:',len(D1))
print('len D3:',len(D3))
print('len D2:',len(D2))
del D2['a']
print(D2)
del D2
print(D2)'''
'''#Dictionary methods:#keys
D1={1:'a',2:'b',3:(1,2)}
D2={'a':'a','b':2,'c':(1,2)}
D3={}
print('D1 keys:',D1.keys())
print('D2 keys:',D2.keys())
print('D3 keys:',D3.keys())
#values:
D1={1:'a',2:'b',3:(1,2)}
D2={'a':'a','b':2,'c':(1,2)}
D3={}
print('D1 values:',D1.values())
print('D2 values:',D2.values())
print('D3 values:',D3.values())
#items
D1={1:'a',2:'b',3:(1,2)}
D2={'a':'a','b':2,'c':(1,2)}
D3={}
print('D1 items:',D1.items())
print('D2 items:',D2.items())
print('D3 items:',D3.items())'''
'''#get
D1={1:'a',2:'b',3:(1,2)}
D2={'a':'a','b':2,'c':(1,2)}
print('D1 key value:',D1.get(2))
print('D2 key value:',D1.get('c'))
print('D1 key value:',D1.get(7))
print('D2 key value:',D1.get('f'))
print('D1  key value:',D1.get(7,'key not found'))
print('D2  key value:',D1.get(7,'key not found'))'''
'''#set default
D1={1:'a',2:'b',3:(1,2)}
D2={'a':'a','b':2,'c':(1,2)}
print('D1 key value:',D1.setdefault(2))
print('D2 key value:',D2.setdefault('c'))
print('D1 key value:',D1.setdefault(7))
print('D2 key value:',D2.setdefault('f'))
print('D1:',D1)
print('D2:',D2)
print('D1  key value:',D1.setdefault(7,'key not found'))
print('D2  key value:',D2.setdefault('f','key not found'))
print('D1:',D1)
print('D2:',D2)'''
'''#update
D1={1:'old'}
D2={1:'a','string':'b'}
D1.update(D2)
print('D1:',D1)
D1.update([4,'value for 4'])
print('D1:',D1)'''

'''#from keys
D1={}
keys2=list(range(5))
keys1=('a','b','c','d')
value='string'
print(dict.fromkeys(keys1))
print(dict.fromkeys(keys2,value))
print(D1.fromkeys(keys1))
print(D1.fromkeys(keys2,value))

#copy
D={1:'One',2:'two'}
D_new=D
D_new2=D.copy()
D[3]='three'
print('D:',D)
print('D_new:',D_new)
print('D_new2:',D_new2)'''

'''#popitem
D1={2:'a','string':'b'}
print(D1.popitem())
print(D1)'''

#pop
D1={2:'a','string':'b'}
print(D1.pop(2))
print(D1)
#print(D1.pop(1))
print(D1.pop(1,'None'))
print(D1)




























