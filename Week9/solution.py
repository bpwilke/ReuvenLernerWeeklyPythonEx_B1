from collections import namedtuple

# let's define our namedtuples
Person = namedtuple('Person', 'first last')

# let's define our custom exception
class TableFull(Exception):
    '''Raised when attempting to add a Person to a table that alread has 10 seated'''
    pass

class GuestList():
    max_at_table = 10               #<-- establish our maximum per table
    
    def __init__(self):
        self.allguests = list()              #<-- establish our guestlist
           
    def assign(self, person, table):         #<-- method for adding/assigning, let's try and manage this only with list of lists
        
        entry = [person, table]              #<-- create entry
        exists = False                       #<-- initialize exists as False until we lookup
        
        for idx, guests in enumerate(self.allguests): #<-- check if person exists, and get index of where they exist
            if person == guests[0]:
                exists = True
                break
        
        ## If the person DOES exist and they have a table number in the new assignment
        existing_table_count = 0             #<-- init existing_table_count to check current table occupancy
        if exists == True and table != None:     
            for guest in self.allguests:     #<-- check destination table occupancy
                if guest[1] == table:
                    existing_table_count += 1
            if existing_table_count < self.max_at_table:    #<-- if there's room, make update
                self.allguests.pop(idx)         #<-- remove previous entry for guest
                self.allguests.append(entry)    #<-- add new entry to guestlist
            else:                            #<-- otherwise, no room, throw exception
                raise TableFull
        
        ## If the person DOES NOT exist and they have a table number in the new assignment
        existing_table_count = 0             #<-- init existing_table_count to check current table occupancy
        if exists == False and table != None: #<-- get existing table count for entry table
            for guest in self.allguests:    #<-- check destination table occupancy
                if guest[1] == table:
                    existing_table_count += 1
            if existing_table_count < self.max_at_table:       #<-- if there's room, make update
                self.allguests.append(entry)    #<-- add to guestlist
            else:
                raise TableFull               #<-- otherwise, no room, throw exception
        
        ## If the person DOES exist and they have None in the new table assignment
        if exists == True and table == None:
            self.allguests.pop(idx)         #<-- remove previous entry for guest
            self.allguests.append(entry)    #<-- add new entry to guestlist
        
        ## If the person DOES NOT exist and they have None in the new table assignment
        if exists == False and table == None:
            self.allguests.append(entry)    #<-- add to guestlist no validation as no table assignment 
    
    def unassigned(self):                    #<-- returns list of people with None assigned as table
        return [each[0] for each in self.allguests if each[1] is None]  
   
    def table(self, table):                  #<-- returns list of people assigned to table
        return [each[0] for each in self.allguests if each[1] == table] 
    
    def free_space(self):                    #<-- returns free space for each table
        remaining_space = dict()
        for guest in self.allguests:
            if guest[1] in remaining_space.keys():
                remaining_space[guest[1]] = remaining_space[guest[1]] - 1 #<-- table exists, so substract a seat
            else: 
                remaining_space[guest[1]] = self.max_at_table - 1 #<-- table doesn't exist in dict(), set to self.max_at_table minus 1
        remaining_space.pop(None, None)           #<-- let's remove the None key here, doesn't make sense
        return remaining_space
    
    def __len__(self):                       #<-- implement our own len for our objects
        return len(self.allguests)

    def guests(self):
        assignedguests = [guest for guest in self.allguests if guest[1] is not None]   #<-- let's pop the None's off...for now. we might add them back to this list
        sortedguests = sorted(assignedguests, key = lambda x: (x[1], x[0].last, x[0].first))
        return [guest[0] for guest in sortedguests]    # return only the Person tuple, not the table per requirements
    
    
    def __str__(self):
        
        # borrowed this from guests(), because i need a version with both Person and table number
        assignedguests = [guest for guest in self.allguests if guest[1] is not None]   #<-- let's pop the None's off...for now. we might add them back to this list
        guestssorted = sorted(assignedguests, key = lambda x: (x[1], x[0].last, x[0].first))
        
        printout = ''
        
        currenttable = guestssorted[0][1]        #<-- get the first table 
        printout += str(currenttable) + '\n'
        
        for guest in guestssorted:
            if guest[1] != currenttable:
                printout += str(guest[1]) + '\n'
            currenttable = guest[1]
            printout += f'\t{guest[0].last}, {guest[0].first}\n'               
        return printout