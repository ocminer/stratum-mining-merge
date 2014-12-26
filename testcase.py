import os,binascii
import mining.DB_Mysql as DB_Mysql
import time

db = DB_Mysql.DB_Mysql()

def gen_solution():
    return binascii.b2a_hex(os.urandom(32))


def insert_share():
    solution = gen_solution()
    timestamp = int(time.time())
    
    db.execute(
         """
         INSERT INTO `shares_mm`
         (time, rem_host, username, our_result, 
         upstream_result, reason, solution, difficulty)
         VALUES 
         (FROM_UNIXTIME(%(time)s), %(host)s, 
         %(uname)s, 
         %(lres)s, 'N', %(reason)s, %(solution)s, %(difficulty)s)
         """,
        {
            "time": timestamp, 
            "host": '114.114.114.114', 
            "uname": 'naituida.naituida', 
            "lres": 'Y', 
            "reason": '',
            "solution": solution,
            "difficulty": 4
        }
    )


for x in xrange(0,100000):
    if x%1000 == 0:
        print "Inserted %d shares" % x
    insert_share()
    

