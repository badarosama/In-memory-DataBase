import sys
from db import database

def console():
    db = database()
    while True:
        try:
            args = sys.stdin.readline()[:-1].split()
            if len(args) == 0:
                continue
            elif args[0] == "END" and len(args) ==1:
                break
            elif args[0] == "BEGIN" and len(args) == 1:
                db.begin()
            elif args[0] == "COMMIT" and len(args) == 1:
                db.commit()
            elif args[0] == "ROLLBACK" and len(args) == 1:
                db.rollback()
            elif args[0] == "SET" and len(args) == 3:
                db.Set(args[1],args[2])
            elif args[0] == "GET" and len(args) == 2:
                db.get(args[1])
            elif args[0] == "UNSET" and len(args) == 2:
                db.unset(args[1])
            elif args[0] == "NUMEQUALTO" and len(args) == 2:
                db.numEqualTo(args[1])
            else:
                print "Invalid command or parameters."
                
                
            
        except KeyboardInterrupt:
            break

    

if __name__=="__main__":
    console()
