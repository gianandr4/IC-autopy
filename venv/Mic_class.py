class CRUD_autopy():


    def __init__(self,price):
        self.Item_Name = ''  ########## nonull
        self.Item_Special = ''
        self.Item_Price = ''  ########## nonull int
        self.Item_CCY = ''  ########## nonull
        self.Item_Slot = ''
        self.Item_Casterlevel = ''
        self.Item_Aura = ''
        self.Item_Weight = ''
        self.Item_Description = ''
        self.Item_Craftprerequisites = ''
        self.Item_Costtocreate = ''
        self.Item_Lore = ''
        self.Item_BookName = ''
        self.Item_BookDisplay = ''
        self.DTInsert = '' #datetime.datetime.now()
        self.Note = ''
        self.Item_Activation = ''







    def check(self):
        'check if minimum fields are filled'
        ''

        return

    def create_dict(self,check=None):
        d={
            'Item_Name': self.Item_Name,       # nonull
            'Item_Special':self.Item_Special,
            'Item_Price' : self.Item_Price,    # nonull int'
            'Item_CCY' :self.Item_CCY ,                     # 'gp/cp/pp'  ,########## nonull'
            'Item_Slot':self.Item_Slot,
            'Item_Casterlevel':self.Item_Casterlevel,
            'Item_Aura':self.Item_Aura,
            'Item_Weight':self.Item_Weight,
            'Item_Description':self.Item_Description,
            'Item_Craftprerequisites':self.Item_Craftprerequisites,
            'Item_Costtocreate':self.Item_Costtocreate,
            'Item_Lore':self.Item_Lore,
            'Item_BookName':self.Item_BookNametem_BookName,
            'Item_BookDisplay':self.Item_BookDisplay,
            'DTInsert':self.DTInsert,                                      #datetime
            'Note':self.Note,
            'Item_Activation':self.Item_Activation
        }
        return d
        




]

x='''
help = [['Item_Name =', 'NOT NULL'],
        ['Item_Special =', 'str'],
        ['Item Price =', 'int  NOT NULL'],
        ['Item CCY =', 'NOT NULL'],
        ['Item_Slot =', 'str'],
        ['Item_Casterlevel =', 'str'],
        ['Item_Aura =', 'str'],
        ['Item_Weight =','int'],
        ['Item_Description =', 'str' ],
        ['Item_Craftprerequisites =', 'str' ],
        ['Item_Costtocreate =', 'str'],
        ['Item_Lore =', 'str'],
        ['Item_BookName =', 'str'],
        ['DTInsert =', 'datetime  NOT NULL'],
        ['Note =', 'str'],
        ['Item_Activation =', 'str' ]]
'''

head , sep, tail =
x=x.replace()



table='T_Items'
insert='Item_Name,Item_Special,Item_Price,Item_CCY,Item_Slot,Item_Casterlevel,Item_Aura,Item_Weight,Item_Description,Item_Craftprerequisites,Item_Costtocreate,Item_Lore,Item_BookName,DTInsert,Note,Item_Activation'
