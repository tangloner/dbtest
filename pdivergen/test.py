import psycopg2
from time import time

def connect_db(path):
    conn_string = "host='localhost' dbname='tpch20' user='btang'"
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    #cursor.execu('select * from sys.total')
    sqls = readQuery(path)
    t1 = time();
    sqlcommands = sqls.split(';')
    for command in sqlcommands[:-1]:
        #print command
        cursor.execute(command)
    t2 = time();
    print "time cost: %f" %(t2-t1) 
    #print cursor.fetchall()
    #print 'TEST FINISHED'

def readQuery(path):
    fd = open(path,'r')
    sqls = fd.read()
    fd.close()
    return sqls

if __name__=='__main__':
    for y in range(1,2):
        print y
        for x in range(1,23):
            if (x==5):
                path = '/export/scratch2/btang/postgresql-9.5/test/tpch-queries/'+str(x)+'.sql'
                print path
                connect_db(path)
    print 'TEST FINISHED'
