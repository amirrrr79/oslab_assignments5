import csv

p=[]

def data_load():
    f=open('data.csv','r')
    for line in f:
        info=line[:-1].split(',')
        new_dict={'code':info[0],'name':info[1],'price':info[2],'count':info[3]}
        p.append(new_dict)


def show_list():
    print('code\tname\tprice\tcount')
    for product in p:
        print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])

        
def add():
    code=int(input('Enter code: '))    
    name=input('Enter name: ') 
    price=int(input('Enter price: '))
    count=int(input('Enter count: '))
    p.append({'code':code,'name':name,'price':price,'count':count})


def edit():
    name=input('Enter name: ')
    for product in p:
        if name==product['name']:
            while True:
                print('1-change code   2-change name   3-change price   4-change count')
                choice=int(input('Enter choice: ')) 
                if choice==1:
                    c=int(input('new code: '))
                    product['code']=c
                    break
                if choice==2:
                    n=input('new name: ')
                    product['name']=n
                    break
                if choice==3:
                    pr=int(input('new price: '))
                    product['price']=pr
                    break
                if choice==4:
                    co=int(input('new count: ')) 
                    product['count']=co
                    break
    if name!=product['name']:
       print('no edit')


def delete():
    name=input('Enter name: ')
    for product in p:
        if name==product['name']:
            print('delete successful')
            p.remove(product)      
    if name!=product['name']:
       print('no delete')    


def search():
    name=input('Enter name: ')
    for product in p:
        if product['name']==name:
            print('search successful')
            print(product)
    if product['name']!=name:
        print('not found')        


def buy():
    name=input('Enter name: ')
    
    for product in p:   
        if name==product['name']:
            x=int(input('how many: '))
            if x>int(product['count']) or x<=0:
                print('not exist')
                    
            else:
                product['count']=int(product['count'])
                product['count']-=x
                product['price']=int(product['price'])
                pr=product['price']*x
                print('name_cala:',name)
                print('tedad_cala:',x)
                print('price:',pr)
    else:
        print('not exist')            
                    
              


def save_and_exit():
    info=['','','','']
    f=open('data.csv','w')
    writer=csv.writer(f)
    for product in p:
        info[0]=product['code']
        info[1]=product['name']
        info[2]=product['price']
        info[3]=product['count']
        writer.writerow(info)
    exit()   


data_load()
while True:
    print('welcome store')
    print('1-add')
    print('2-edit')
    print('3-delete')
    print('4-show list')
    print('5-search')
    print('6-buy')
    print('7-save and exit')
    choice=int(input('Enter choice: '))  
 
    if choice==1:
        add()
    if choice==2:
        edit()    
    if choice==3:
        delete()    
    if choice==4:
        show_list() 
    if choice==5:
        search()
    if choice==6:
        buy()    
    if choice==7:
        save_and_exit()            