'''
Author: Aditya Geria
KPCB Summer 2018 Challenge Problem

- This program implements the problem in Python 2
Assumptions:
* This table implements hashing with chaining. Values that hash to the same key will be chained.
* Because of chaining, this table will return the first value associated with the key.
To match value with get(), just iterate through next until value == value
* Delete will delete all elements associated with a given key
* Printing the table results in printing only non-Null values, and prints all
values associated with a key
'''

#Defines the class to create an entry in the hash table
#Necessary because of the chaining implementation choice
class entry:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None

#Creates the class for the full table - contains methods for important functions
class ChainedHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.values = 0

    #set a value and key in the hash table (with chaining) - should never fail
    def set(self, value, key):
        index = hash(key) % self.size
        if index < 0: return False

        temp = entry(value, key)
        self.values += 1

        if self.table[index] is None:
            self.table[index] = temp
            return True

        elif self.table[index] is not None and self.table[index].next is None:
            self.table[index].next = temp
            return True

        #chaining implementation
        else:
            temp2 = self.table[index]
            while temp2.next is not None:
                temp2 = temp2.next
            temp2.next = temp
            return True

    #returns the first value at a given key
    #To search through values at a given key, use while() loop
    def get(self, key):
        index = hash(key) % self.size
        if index < 0: return None
        if self.table[index] is None:
            return None
        else:
            return self.table[index].value

    #warning! will delete all elements associated with a given key
    def delete(self, key):
        index = hash(key) % self.size
        if index < 0: return None

        if self.table[index] is not None:
            temp = self.table[index]
            if temp.next is None:
                self.values -= 1
                self.table[index] = None
                return temp.value
            else:
                self.values -= 1
                while temp.next is not None:
                    self.values -= 1
                    temp = temp.next
                self.table[index] = None
                return temp

            self.table[index] = None
            return temp
        else:
            return None

    #returns number of values in the table/size of table
    def load_factor(self):
        return float(self.values)/float(self.size)

    #prints table in a visual format, seperated by key
    def printself(self):
        for i in range(0, self.size):
            temp = self.table[i]
            if temp is not None:
                print "Key: ", temp.key
                print temp.value
                if temp.next is not None:
                    temp = temp.next
                    while temp is not None:
                        print str(temp.value) + ""
                        temp = temp.next
