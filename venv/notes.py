



x='''
* item_name =
item_special =
* item price = int
item_slot =
item_casterlevel =
item_aura =
item_weight =
item_description =
item_craftprerequisites =
item_costtocreate =
item_lore =
item_BookName =
Item_BookDisplay =

* DTInsertDTInsert =
Note =
Item_Activation =



hamachi
25.117.131.125

zerotier
a09acf0233439482

ic-project
192.168.193.42

andreas
Qwerty123!


'''
d={'a':1,'b':2,'c':3}


'''
 Price (Item Level):
 Body Slot:',
 Caster Level:',
 Aura: 
 Activation: 
 Weight: 
 Description:
 Lore:
 Prerequisites: 
 Cost to Create: The item’s gp cost, XP cost, and days to create.\n']
'''

''



class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)


ru
ord()


ins=

def ru(x):
    return int(x)

'''
ru(15d6)
'''





import random

random.random()


x="SELECT cast(Item_Price as varchar)+' '+Item_CCY Item_Price, cast(Item_Weight as varchar)+'lb' Item_Weight * FROM T_Items where Item_ID='1'";
