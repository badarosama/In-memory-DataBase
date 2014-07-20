{\rtf1\ansi\ansicpg1252\cocoartf1138\cocoasubrtf510
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww13600\viewh10000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\b\fs24 \cf0 To run the program:
\b0 \
Open a terminal and type: python console.py\
Enter the db commands.\

\b \
Design and Analysis.
\b0 \
There are two files. console.py reads the database commands and calls db.py where the functions are implemented.\
\
1-All variables are stored in a dictionary in order to ensure an O(1) lookup time.\
   For example,\
	\{"a": [(3,1),(4,2),(5,3)],\
	  "b": [(4,1),(9,2)]\}\
	\
	keys = variables\
	values = list of tuples. Each tuple consists of value and transaction number. For example,\
	a was set to 3 at transaction 1 and then 4 at transaction 2 and then 5 at transaction 3.\
	Therefore at any given time, GET a would be an O(1) lookup. We always return the last value\
	or the most recent value from the list. SET is also an O(1) operation. Append to the end of the 	list of the variable exist otherwise add it to the dictionary. UNSET is also O(1) because I add a\
	NULL value to the end of the list.\
\
2- For NUMSEQUALTO operation i store another dictionary called nums. \
For example. \{3:2, 4:1\}. It is the mapping of a given variable to its frequency in the transactions dict at any given time. NUMSEQUALTO is O(1) lookup.\
\
3- A transaction counter keeps track of the current transaction. It is incremented with BEGIN and decremented when we ROLLBACK. A transaction value of 0 is reserved for committed variables.\
\
4- COMMIT: Delete all values from transactions except the latest and assign them a transaction value of 0. \
\
5- ROLLBACK.\
Delete all transactions with current transaction count from each variable in transactions. Also, decrement the count of the values from nuns and increment the count of the previous value. For example, \
\{"a":[(3,1),(4,2),(5,3)]\} When we rollback transaction 3, we delete (5,3) from the list so the count of 5 is decremented by 1 and the count of previous value i.e 4 is incremented by 1.\
\
\
\
}