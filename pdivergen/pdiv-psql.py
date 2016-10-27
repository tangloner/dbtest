import psycopg2
import os
from time import time

def tpch_queries(qpath, db):
#    os.system(startserver); 
    connection = psycopg2.connect(user='btang', host='localhost', dbname=db)
    cursor = connection.cursor()
    for outloop in range(1,11):
        output = dbname + "-" + str(outloop)+".ret"
        print output
        fout = open(output,'w')
        for qi in range (1,23):
            if(qi!=2) and (qi!=21):
                print qi;
                querypath = qpath + str(qi) +".sql"
                sqls = readsql(querypath);
                queries = sqls.split(';')
                t1 = time();
                for query in queries[:-1]:
                    cursor.execute(query);
                t2 = time();  
                t = t2-t1
                fout.write(str(t)+"\n")
        fout.close()
    connection.close()
#    os.system(stopserver)

def create_db_psqldb(dbname):
    createdb = "createdb " + dbname;
    os.system(createdb);

def drop_db(dbname):
    dropdb = "dropdb " + dbname;
    os.system(dropdb);


def connect_db(dbname):
    connection = monetdb.sql.connect(username="btang", hostname="localhost", database=dbname)
    return connection;
   
def readsql(path):
    fd = open(path,'r')
    sqls = fd.read()
    fd.close()
    return sqls


def converttbltocsv(path):
    cmd="for i in `ls *.tbl`; do sed 's/|$//' $i > ${i/tbl/csv}; echo $i; rm $i; done;"
    os.system(cmd)
#    os.system("rm *.tbl") 


if __name__=='__main__':
    dbfarm = "/export/scratch2/btang/psqlbed"    
    scalefactor = [1,3,10,30,100];  #set tpch scale factor
#    scalefactor = [1];
    prefix_dbgen = "/export/scratch2/btang/tpch/dbgen/dbgen -f -s "
    prefix_dbname = "tpch-"
    schema_path = "/export/scratch2/btang/testbed/tpchtbl.sql";
    data_path = "/export/scratch2/btang/postgresql-9.6rc1/pdivergen/loaddata-psql.sql";

    for sf in scalefactor:
#        startserver = "postgres -D " + dbfarm + " >logfile 2>&1 &";
#        os.system(startserver);

        dbgen = prefix_dbgen + str(sf);
        print "generating data"
        os.system(dbgen);
 
        dbname = prefix_dbname + str(sf);
        print "create database in postgresql"
        create_db_psqldb(dbname)

        bkschema =  "psql " + dbname + " < " + schema_path;
        print "load schema"
        os.system(bkschema)

        print "convert data format"
        converttbltocsv(data_path)

        bkdata = "psql " + dbname + " < " + data_path;
        print "load data"
        os.system(bkdata)

 #       stopserver = " kill -INT `head -1 " + dbfarm +"/postmaister.pid` ";
 #       os.system(stopserver);    
    
        print "start queries"
        qpath = "/export/scratch2/btang/postgresql-9.6rc1/pdivergen/tpch-queries/"
        tpch_queries(qpath, dbname);

        print "dorp db"
        drop_db(dbname)        

