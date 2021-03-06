class database:
    
    def __init__(self):
        """transactions is a mapping from variables to a list of transactions
           nums is a mapping of values stored to their frequency at a given time in transaction.
           transaction: current transaction number. transaction = 0 depicts committed data.
        """
        self.transactions = {}
        self.nums = {}
        self.transaction = 0
    
    def begin(self):
        """start a new transaction by incrementing the
           transaction counter.
        """
        self.transaction+=1
        
    def commit(self):
        """delete all transactions except current transaction from all lists
           and assign a transaction number 0 to depict committed.
        """
        if self.transaction == 0:
            print "NO TRANSACTION"
        else:
            for key in self.transactions:
                if len(self.transactions[key])>0:
                    l=[]
                    l.append((self.transactions[key][-1][0],0))
                    self.transactions[key] = l
 
            self.transaction = 0
                
    def rollback(self):
        """delete all values that have current transaction from all variables in the
           transactions dictionary and decrement the current transaction count.
           also decrement the frequency of values from nums.
        """
        if self.transaction == 0:
            print "NO TRANSACTION"
        else:
            for key in self.transactions:
                  for i in range(len(self.transactions[key])-1, -1, -1):
                      if self.transactions[key][i][1] == self.transaction:
                          if self.transactions[key][i][0]!="NULL":
                              self.nums[self.transactions[key][i][0]]-=1 
                          del self.transactions[key][i]
                          if len(self.transactions[key])>0 and self.transactions[key][-1][0]!="NULL":
                              self.nums[self.transactions[key][-1][0]]+=1
                                      
            self.transaction-=1
        
    def Set(self,var,value):
        """set the new value and adjust the frequency count in nums.
        """
        if var in self.transactions:
            previous = None
            if len(self.transactions[var])!=0:
                previous =  self.transactions[var][-1][0]
            self.transactions[var].append((value,self.transaction))
            if previous != "NULL" and previous!=None:
                self.nums[previous]-=1 
        else:
            self.transactions[var] = [(value,self.transaction)]
            
        if value in self.nums:self.nums[value]+=1
        else:self.nums[value]=1     
            
    def get(self,var):
        """get the most recent value of the variable.
           it will always be the last value in the list.
        """
        if var in self.transactions and len(self.transactions[var]) != 0:
            print self.transactions[var][-1][0]
        else: print "NULL"
            
    def unset(self,var):
        """unset: assign a NULL value and append to the list
           the frequncy count of the value from nums should be decremented.
        """
        if var in self.transactions and len(self.transactions[var])>0:
            previous = self.transactions[var][-1][0]
            if previous!="NULL":
                self.transactions[var].append(("NULL",self.transaction))
                self.nums[previous]-=1
        else:
            print "variable not initialized"
        
            
    def numEqualTo(self,val):
        """return the frequecny of the value.
        """
        if val in self.nums:print self.nums[val]
        else:print "0"
