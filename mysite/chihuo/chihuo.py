# coding:UTF8
from mysite.chihuo.models import Store, Pocily

# 将来要做成模糊查询
def query_store(store_name):
    store = Store.objects.get(name=store_name)
    return store

def query_pocily(store_name):
    store = Store.objects.get(name=store_name)
    return store.pocilys.filter(valid=True)
    
if __name__ == "__main__":
    print 123
    print query_pocily('xxx')
