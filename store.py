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
    code=int(input('Enter code :'))
    name=input('Enter name: ')
    price=int(input('Enter price: '))
    count=int(input('Enter count: '))
    p.append({'code':code,'name':name,'price':price,'count':count})

def edit():
    name=input('Enter name: ')
    for product in p:
        if name==product['name']:
            while True:
                print('1-change name  2-change code   3-change price    4-change count')
                choice=int(input('Enter choice: '))
                if choice==1:
                    n=input('Enter new name: ')
                    product['name']=n   
                    break   
                if choice==2:
                    c=int(input('Enter new code: '))
                    product['code']=c
                    break
                if choice==3:
                    pr=int(input('Enter new price: '))
                    product['price']=pr
                    break
                if choice==4:
                    co=int(input('Enter new count: '))
                    product['count']=co 
                    break 
        else:
            print('no edit')
            


def search():
    name=input('Enter name: ')
    for product in p:
        if name==product['name']:
            print('search successful')
            print(product)
        else:
            print('search not successful')
        


def delete():
    name=input('Enter name: ')
    for product in p:
        if product['name']==name:
            p.remove(product)
            print('remove successful')
        else:
         print('no remove')
         

def buy():
    name=input('Enter name: ')
    for product in p:
        price=int(product['price'])
        co=int(product['count'])
        if name==product['name']:
            how=int(input('How many: '))
            if how>co or how<=0:
                print('not exist')
            else:
                new_count=co-how
                product['count']=str(new_count)
                c=how*price
                print('name_cala: ',name)
                print('tedad_cala: ',how)
                print('price: ',c)
        else:
            print('no product exist') 

data_load()
while True:
    print('welcome store')
    print('1-add')
    print('2-edit')
    print('3-delete')
    print('4-show list')
    print('5-search')
    print('6-buy')
    print('7-exit')

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
        exit()
            







