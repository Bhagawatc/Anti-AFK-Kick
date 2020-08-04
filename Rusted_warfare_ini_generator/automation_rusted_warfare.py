import os
from os import path


x = input('Spawner no.: ') # Asks for ini file number

n_unit_class = 1 # Will be utilised for multiple unit support
spawner_file_name = "spawner" + x # used for file name

unit_names = []
units_quantity = []

if(path.isfile(spawner_file_name) == False): # checks if file exists
    f = open(spawner_file_name + ".ini", "w")
    print("File created called " + str(spawner_file_name))

    thats_it = False # Asking for multiple units (to be implemented)
    while(thats_it == False):

        unit_name = input("What is the unit code? ")
        unit_names.append(unit_name)

        quantity_units = input("How many? ")
        units_quantity.append(quantity_units)

        finished = input('Another unit? (Y or N?) ') 
        if(finished.lower() == 'y'):
            thats_it = False
            n_unit_class = n_unit_class + 1
        elif (finished.lower() == 'n'):
            thats_it = True    
        else: #catches responses that aren't Y/N
            finished = input("Didn't catch that. Try again. Another unit (Y or N)? ")
            thats_it = False
        
    f.write("[core]\n"+ "name: " + spawner_file_name + "\n") #line 1 & #line 2
    f.write("displayText: " + spawner_file_name[0:1].upper() + spawner_file_name[1:7] +" "+ spawner_file_name[7:8] + "\n") #line 3

    f.write("displayDescription: Spawns " + unit_name + " x " + quantity_units )
    for x in unit_names:
        f.write("," + unit_names[n_unit_class-1] + " x " + units_quantity[n_unit_class-1] + "\n") #line 4

    f.write("class: CustomUnitMetadata\n"+ "price: 0\n" +"maxHp: 4000\n" + "mass: 0 \n" + "radius: 0 \n" + "// n/a\n" +"\n"+ "isBuilding: true \n" +"\n"+"[hiddenAction_Spawn]\n"+"autoTrigger: if numberOfUnitsInEnemyTeam(withTag='commandCenter', equalTo=1)\n"+"\n") #line 5 & line 6 & line 7 & line 8 & line 9 & line 10 & line 11 & line 12 & line 13 & line 14 & line 15 & line 16 & line 17

    f.write("spawnUnits:" + unit_name+"*"+str(quantity_units)+"(offsetRandomY=115, offsetRandomX=115)" ) #line 18 & line 19
    for x in unit_names:
        f.write("," + unit_names[n_unit_class-1]+"*"+units_quantity[n_unit_class-1]+"(offsetRandomY=115, offsetRandomX=115)")
    f.write("\n")
    f.write("alsoTriggerActions:delete\n"+ "\n" +"[hiddenAction_delete]\n"+ "deleteSelf:true \n"+ "\n"+ "[graphics]\n" + "image: picker.png \n" +"imageScale:0 \n" +"\n"+"[attack]\n"+"canAttack: false" + "\n" + "canAttackFlyingUnits: false" + "\n" + "canAttackLandUnits: false" + "\n" + "canAttackUnderwaterUnits: false\n" + "\n" + "[movement]" + "\n" + "movementType: NONE" ) #line 20 & line 21 & line 22 & line 23 & line 24 & line 25 & line 26 & line 27 & line 28 & line 29 & line 30-33 & line 34 & line 35-36
else:
    print("I dunno man you fucked something up")
        
