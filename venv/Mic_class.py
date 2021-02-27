class CRUD_autopy():


    def __init__(self, name='', price='', ccy='gp'):

        self.Item_Name = ''  ########## nonull
        self.Item_Special = ''
        self.Item_Price = int(1)  ########## nonull int
        self.Item_CCY = 'gp/cp/pp'  ########## nonull
        self.Item_Slot = ''
        self.Item_Casterlevel = ''
        self.Item_Aura = ''
        self.Item_Weight = ''
        self.Item_Description = ''
        self.Item_Craftprerequisites = ''
        self.Item_Costtocreate = ''
        self.Item_Lore = ''
        self.Item_BookNametem_BookName = ''
        self.Item_BookDisplay = ''
        self.DTInsert = 'datetime.datetime.now()'
        self.Note = ''
        self.Item_Activation = ''

        self.variables=''
        self.

]
help = [['Item_Name', 'NOT NULL'],
        ['Item_Special', ''],
        ['Item Price', 'NOT NULL'],
        ['Item CCY =', 'NOT NULL'],
        ['Item_Slot =', ],
        ['Item_Casterlevel =', ],
        ['Item_Aura =', ],
        ['Item_Weight =', ],
        ['Item_Description =', ],
        ['Item_Craftprerequisites =', ],
        ['Item_Costtocreate =', ],
        ['Item_Lore =', ],
        ['Item_BookName =', ],
        ['DTInsert =', 'NOT NULL'],
        ['Note =', ],
        ['Item_Activation =', ]]


table='T_Items'
insert='Item_Name,Item_Special,Item_Price,Item_CCY,Item_Slot,Item_Casterlevel,Item_Aura,Item_Weight,Item_Description,Item_Craftprerequisites,Item_Costtocreate,Item_Lore,Item_BookName,DTInsert,Note,Item_Activation'
sql2=