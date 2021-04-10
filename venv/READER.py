mic_path=r'C:\Users\Drastis\Desktop\mic\MIC2.txt'
appendix_path=r'C:\Users\Drastis\Desktop\mic\appendixes\appendix_exact.txt'

import re

with open (mic_path,'r',encoding='utf-8') as f:
    micc=f.read()

with open (appendix_path,'r') as f:
    appendix=f.readlines()

item=appendix[0] #'SKILL SHARD\n'


items_list=[]
for item in appendix:
    print('a')
    name=item.replace('\n','')
    # name = item.replace(' ','^( |\n)$')


    pattern=(r'({}.*?Cost to Create:.*?\.)'.format(name))
    patternRegex=re.compile(pattern,flags=re.DOTALL)
    result= patternRegex.search(micc)
    ITEM = result.group(1)
    items_list.append(ITEM)
    if "WARLOCK" in name:
        break


ITEM='VIPERBLADE\n[PLACEHOLDER]\nPrice (Item Level): 6,302 gp (10th)\nBody Slot: — (held)\nCaster Level: 7th\nAura: Moderate; (DC 18) necromancy\nActivation: Swift (mental)\nWeight: 1 lb.\nThe hilt of this dagger is shaped like a snake,\nand the twisted blade looks like an impossibly\nlong tongue.\nCreated by cults that worship serpent deities, these +1 daggers are prized for their\nability to secrete toxic venom. A viperblade\nhas 5 charges, which are renewed each\nday at dawn. Spending 1 or more charges\nenvenoms the blade (at no risk to you) for\nthe next attack you make during this turn.\nThe poison deals 1d6 points of Constitution\ndamage (both primary and secondary).\nThe save DC depends on the number of\ncharges spent:\n1 charge: Fortitude DC 12.\n2 charges: Fortitude DC 15.\n3 charges: Fortitude DC 18.\nPrerequisites: Craft Magic Arms and\nArmor, poison.\nCost to Create: 3,000 gp (plus 302 gp for\nmasterwork dagger), 300 XP, 6 days.'
ITEM='WARLOCK’S SCEPTER\n[PLACEHOLDER]\nPrice (Item Level): 8,305 gp (12th)\nBody Slot: — (held)\nCaster Level: 10th\nAura: Moderate;\n(DC 20)\nnecromancy\nActivation: — or\nswift (mental); see\ntext\nWeight: 3 lb.\nThis sturdy ebony rod is surmounted by a\ncarving of a demonic, horned skull.\nThis +1 light mace confers a +1 profane bonus on your ranged touch\nattack rolls while you hold it. This\nis a continuous effect and requires\nno activation.\n Furthermore, a warlock’s scepter has\n5 charges, which are renewed each day\nat dawn. Spending 1 or more charges\nimproves the damage of the next\neldritch blast (CAr 7) you make in\nthat round.\n1 charge: +1d6 damage.\n3 charges: +2d6 damage.\n5 charges: +4d6 damage.\n After these charges have been expended,\nthe rod remains a +1 light mace, but it no\nlonger provides a bonus on ranged touch\nattack rolls until its charges are restored.\n Prerequisites: Craft Magic Arms and\nArmor, Craft Rod, bestow curse.\nCost to Create: 4,000 gp (plus 305 gp for\nmasterwork light mace), 320 XP, 8 days.'

# item name a
a = name


# item special b
x_pattern=re.compile(r'(\[.*?\])',flags=re.DOTALL)
result= x_pattern.search(ITEM)
b = result.group(1)


# item price c
x_pattern=re.compile(r'Price \(Item Level\): (.*)')
result= x_pattern.search(ITEM)
DL=result.group(1)
c = result.group(1)


# item slot d
x_pattern=re.compile(r'Body Slot:(.*)')
result= x_pattern.search(ITEM)
DL=result.group(1)
d = result.group(1)

# Item_Casterlevel e
x_pattern=re.compile(r'Caster Level: (.*)')
result= x_pattern.search(ITEM)
DL=result.group(1)
e = result.group(1)

# Item_Aura f
x_pattern=re.compile(r'Aura: (.*)Activation|Weight',flags=re.DOTALL)
result= x_pattern.search(ITEM)
DL=result.group(1)
f = result.group(1)

# Item_Weight g
x_pattern=re.compile(r'Weight: (.*).')
result= x_pattern.search(ITEM)
DL=result.group(1)
g = result.group(1)






# Item_Description h
x_pattern=re.compile(r'Weight:.*.|Activation:.*',flags=re.DOTALL)
result= x_pattern.search(ITEM)
DL=result.group(1)
h = result.group(1)


# Item_Prerequisites i
x_pattern=re.compile(r'Prerequisites: (.*).',flags=re.DOTALL)
result= x_pattern.search(ITEM)
UL=result.group(1)
h = result.group(1)


# Item_Craft j
x_pattern=re.compile(r'Cost to Create: (.*).',flags=re.DOTALL)
result= x_pattern.search(ITEM)
UL=result.group(1)
i = result.group(1)






    #
    # dict={
    #     'Item_Name' :a,
    #     'Item_Special':b,
    #     'Item Price':c,
    #     'Item_Slot':d,
    #     'Item_Casterlevel':e,
    #     'Item_Aura':f,
    #     'Item_Weight':g,
    #     'Item_Description':h,
    #     'Item_Craftprerequisites':i,
    #     'Item_Costtocreate':j,
    #     'Item_Lore':k,
    #     'Item_BookName':l,
    #     'Item_BookDisplay':m,
    #     'DTInsert':n,
    #     'Note ':o,
    #     'Item_Activation':p, }
    # items_list.append(dict)
    #



for item in items_list:
    print(item)
    input()