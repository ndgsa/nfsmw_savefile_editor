import sys
import hashlib
import codecs
import binascii
from os.path import exists
import struct


#Globals
inptr = open(sys.argv[1], "rb+")
inptr.seek(0x0)
bytearray_data = bytearray(inptr.read(-1))
Car_List = []
Tunning_Slot_List = []
Marker_List = []
Career_Slot_List = []

#Main Car List
CarNameList = [{'CarCode': '08D4BE6E08D4BE6E', 'CarSlot': '48', 'CarName': 'Dodge Viper SRT10'}, {'CarCode': '0BC42C7B0BC42C7B', 'CarSlot': '41', 'CarName': 'Lamborghini Gallardo'}, {'CarCode': '117AEEA6117AEEA6', 'CarSlot': '3B', 'CarName': 'Fiat Punto'}, {'CarCode': '1945949019459490', 'CarSlot': '49', 'CarName': 'Chevrolet Camaro SS'}, {'CarCode': '206518DF206518DF', 'CarSlot': '3D', 'CarName': 'Cadillac CTS'}, {'CarCode': '2FAF77822FAF7782', 'CarSlot': '38', 'CarName': 'Mercedes CLK 500'}, {'CarCode': '33C8098E33C8098E', 'CarSlot': '24', 'CarName': 'Mazda RX-7'}, {'CarCode': '3434F1663434F166', 'CarSlot': '42', 'CarName': 'Toyota Supra'}, {'CarCode': '34898C190D563B5F', 'CarSlot': '43', 'CarName': 'Subaru Impreza WRX STI'}, {'CarCode': '36493D3136493D31', 'CarSlot': '2C', 'CarName': 'Lotus Elise'}, {'CarCode': '374433D6374433D6', 'CarSlot': '4C', 'CarName': 'Mazda RX-8'}, {'CarCode': '4DFD939B4DFD939B', 'CarSlot': '39', 'CarName': 'Ford Mustang GT'}, {'CarCode': '4E4ACC23B35F084E', 'CarSlot': '37', 'CarName': 'BMW M3 GTR'}, {'CarCode': '4E4ACC23F8E0DA39', 'CarSlot': '27', 'CarName': 'BMW M3 GTR (Slow)'}, {'CarCode': '534B0579534B0579', 'CarSlot': '31', 'CarName': 'VW Golf Gti'}, {'CarCode': '6A1CB6A46A1CB6A4', 'CarSlot': '4B', 'CarName': 'Aston Martin DB9'}, {'CarCode': '6FF43E9B6FF43E9B', 'CarSlot': '40', 'CarName': 'Porsche 911 GT2'}, {'CarCode': '7B4BF6F8BF427E9B', 'CarSlot': '21', 'CarName': 'Audi A4 Quattro'}, {'CarCode': '7BC1727BE514C4D5', 'CarSlot': '2F', 'CarName': 'Audi A3 Quattro'}, {'CarCode': '8D5B7DD28D5B7DD2', 'CarSlot': '4F', 'CarName': 'Porsche 911 Turbo S'}, {'CarCode': '929986C4D43D0667', 'CarSlot': '29', 'CarName': 'Porsche Carrera GT'}, {'CarCode': '9540785A9540785A', 'CarSlot': '34', 'CarName': 'Chevrolet Cobalt SS'}, {'CarCode': '9E5765019E576501', 'CarSlot': '20', 'CarName': 'Corvette C6.R'}, {'CarCode': 'A1E1D3D8A1E1D3D8', 'CarSlot': '3E', 'CarName': 'Vauxhall Monaro VXR'}, {'CarCode': 'A1F94771A1F94771', 'CarSlot': '3F', 'CarName': 'Mercedes SL65 AMG'}, {'CarCode': 'A6FEC2813F0888CD', 'CarSlot': '4D', 'CarName': 'BMW M3 (Street)'}, {'CarCode': 'AF2DC3C10C076C8F', 'CarSlot': '50', 'CarName': 'Police Corvette'}, {'CarCode': 'AF2DC3C149393B74', 'CarSlot': '36', 'CarName': 'Civilcar Pickup'}, {'CarCode': 'AF2DC3C14BC7F2C5', 'CarSlot': '4A', 'CarName': 'Pizza'}, {'CarCode': 'AF2DC3C1645FDCF9', 'CarSlot': '46', 'CarName': 'Ford Mustang GT?'}, {'CarCode': 'AF2DC3C195DC4969', 'CarSlot': '2B', 'CarName': 'Police GTO'}, {'CarCode': 'AF2DC3C1AE75E628', 'CarSlot': '28', 'CarName': 'Police SUV'}, {'CarCode': 'AF2DC3C1C71A47A7', 'CarSlot': '23', 'CarName': 'Dumptruck'}, {'CarCode': 'AF2DC3C1D8E0EC71', 'CarSlot': '2D', 'CarName': 'Civilcar VAN'}, {'CarCode': 'AF2DC3C1F11AF07A', 'CarSlot': '2E', 'CarName': 'Taxi'}, {'CarCode': 'AF2DC3C1F57E6670', 'CarSlot': '3C', 'CarName': 'Police'}, {'CarCode': 'AF2DC3C1FAFFD951', 'CarSlot': '45', 'CarName': 'Cementtruck'}, {'CarCode': 'B02FFF5BB02FFF5B', 'CarSlot': '4E', 'CarName': 'Lexus IS300'}, {'CarCode': 'B6FBEECCB6FBEECC', 'CarSlot': '44', 'CarName': 'Mitsubishi Lancer EVO VIII'}, {'CarCode': 'BBB500A8BBB500A8', 'CarSlot': '25', 'CarName': 'Mercedes SL 500'}, {'CarCode': 'BBD92AE3BBD92AE3', 'CarSlot': '1F', 'CarName': 'Mercedes SLR McLaren'}, {'CarCode': 'BD0BD7A2BD0BD7A2', 'CarSlot': '32', 'CarName': 'Mitsubishi Eclipse'}, {'CarCode': 'C63D48AAC63D48AA', 'CarSlot': '47', 'CarName': 'Pontiac GTO'}, {'CarCode': 'C88B3A19C88B3A19', 'CarSlot': '30', 'CarName': 'Audi TT Quattro'}, {'CarCode': 'CF82E522E48C1146', 'CarSlot': '26', 'CarName': 'Corvette C6'}, {'CarCode': 'DAA74D3CDAA74D3C', 'CarSlot': '2A', 'CarName': 'Porsche 911 Carrera S'}, {'CarCode': 'EAA5C042EAA5C042', 'CarSlot': '22', 'CarName': 'Ford GT'}, {'CarCode': 'EB5B5541EB5B5541', 'CarSlot': '3A', 'CarName': 'Porsche Cayman S'}, {'CarCode': 'EB6718EBEB6718EB', 'CarSlot': '33', 'CarName': 'Renault Clio v6'}, {'CarCode': 'EB77CDC1EB77CDC1', 'CarSlot': '35', 'CarName': 'Lamborghini Murciélago'}]

#Bonus Car List
BonusCarNameList = [{'TunningSlot': '00', 'CarName': 'BMW M3 GTR'}, {'TunningSlot': '01', 'CarName': 'BL#10 Porsche Cayman S'}, {'TunningSlot': '02', 'CarName': 'BL#11 Mitsubishi Eclipse'}, {'TunningSlot': '03', 'CarName': 'BL#12 Mazda RX-8'}, {'TunningSlot': '04', 'CarName': 'BL#13 Toyota Supra'}, {'TunningSlot': '05', 'CarName': 'BL#14 Lexus IS300'}, {'TunningSlot': '06', 'CarName': 'BL#15 VW Golf GTI'}, {'TunningSlot': '07', 'CarName': 'BL#2 Mercedes SLR McLaren'}, {'TunningSlot': '08', 'CarName': 'BL#3 Aston Martin DB9'}, {'TunningSlot': '09', 'CarName': 'BL#4 Dodge Viper SRT10'}, {'TunningSlot': '0A', 'CarName': 'BL#5 Corvette C6'}, {'TunningSlot': '0B', 'CarName': 'BL#6 Lamborghini Gallardo'}, {'TunningSlot': '0C', 'CarName': 'BL#7 Mercedes CLK500'}, {'TunningSlot': '0D', 'CarName': 'BL#8 Ford Mustang GT'}, {'TunningSlot': '0E', 'CarName': 'BL#9 Lancer EVO VIII'}, {'TunningSlot': '0F', 'CarName': 'Corvette C6.R (Yellow)'}, {'TunningSlot': '10', 'CarName': 'Porsche 911 GT2 (White)'}, {'TunningSlot': '11', 'CarName': 'Mercedes SL65 AMG (Black)'}, {'TunningSlot': '12', 'CarName': 'Porsche 911 Carrera S'}, {'TunningSlot': '13', 'CarName': 'Corvette C6.R (Red)'}, {'TunningSlot': '14', 'CarName': 'Camaro SS'}, {'TunningSlot': '15', 'CarName': 'Corvette C6'}, {'TunningSlot': '16', 'CarName': 'Lotus Elise'}, {'TunningSlot': '17', 'CarName': 'Porsche 911 GT2 (black)'}, {'TunningSlot': '18', 'CarName': 'BMW M3 GTR (Street)'}, {'TunningSlot': '19', 'CarName': 'Mercedes SL500'}, {'TunningSlot': '1A', 'CarName': 'Mercedes SL56 AMG (deep blue)'}, {'TunningSlot': '1B', 'CarName': 'Toyota Supra'}, {'TunningSlot': '1C', 'CarName': 'Ford GT (Castrol)'}, {'TunningSlot': '1D', 'CarName': 'BL#1 BMW M3 GTR'}, {'TunningSlot': '1E', 'CarName': 'BMW M3 GTR (Slow)'}]

#Bonus Markers Code List
MarkerNameList = [{'MarkerName': 'Brakes', 'bMarker': '010000000000000001000000'}, {'MarkerName': 'Engine', 'bMarker': '020000000000000001000000'}, {'MarkerName': 'Nitro', 'bMarker': '030000000000000001000000'}, {'MarkerName': 'Turbo', 'bMarker': '040000000000000001000000'}, {'MarkerName': 'Suspension', 'bMarker': '050000000000000001000000'}, {'MarkerName': 'Tyres', 'bMarker': '060000000000000001000000'}, {'MarkerName': 'Transmission', 'bMarker': '070000000000000001000000'}, {'MarkerName': 'Body', 'bMarker': '080000000000000001000000'}, {'MarkerName': 'Hood', 'bMarker': '090000000000000001000000'}, {'MarkerName': 'Spoiler', 'bMarker': '0A0000000000000001000000'}, {'MarkerName': 'Rims', 'bMarker': '0B0000000000000001000000'}, {'MarkerName': 'RoofScoop', 'bMarker': '0C0000000000000001000000'}, {'MarkerName': 'Armaturen', 'bMarker': '0D0000000000000001000000'}, {'MarkerName': 'Vinyl', 'bMarker': '0E0000000000000001000000'}, {'MarkerName': 'Sticker', 'bMarker': '0F0000000000000001000000'}, {'MarkerName': 'Paint', 'bMarker': '100000000000000001000000'}, {'MarkerName': 'Out-of-Jail', 'bMarker': '110000000000000001000000'}, {'MarkerName': 'Extra-Impound-Strike', 'bMarker': '140000000000000001000000'}, {'MarkerName': 'Car-Impound-Release', 'bMarker': '150000000000000001000000'}]


hex_decode = codecs.getdecoder('hex_codec')
hex_encode = codecs.getencoder('hex_codec')
if sys.version_info[0] >= 3:
  def bytearray_hexstr(arr):
    return str(hex_encode(arr)[0], 'ascii')
else:
  def bytearray_hexstr(arr):
    return str(hex_encode(arr)[0])


class Car:
    #Number
    CarName = None
    CarType = None
    bSlotNumber = None
    bCarCode = None
    bCarCategory = None
    TunningSlot = {}    
    CareerSlot = {}
    hCarLocation = None

    def __init__(self, CarName, CarType, bSlotNumber, bCarCode, bCarCategory, bTunningSlot, bCareerSlot, hCarLocation):
        self.CarName = CarName
        self.CarType = CarType
        self.bSlotNumber = bSlotNumber
        self.bCarCode = bCarCode
        self.bCarCategory = bCarCategory
        self.TunningSlot = {bTunningSlot: {}}    
        self.CareerSlot = {bCareerSlot: {}}
        self.hCarLocation = hCarLocation

    def __repr1__(self):
        pass

    def print_car(self):
        from pprint import pprint
        pprint(vars(self))

    def pretty_print_car(self):
        print("CarType:{:9s} CarName:{:30s}  SlotNumber:{} CarCode:{} CarCategory:{} TunningSlot:{} CareerSlot:{} hLocation:{}".format(self.CarType, self.CarName, self.bSlotNumber.hex(), self.bCarCode.hex(), self.bCarCategory.hex(), [key.hex() for key in self.TunningSlot.keys()][0], [key.hex() for key in self.CareerSlot.keys()][0], hex(self.hCarLocation)))  


class TunningSlot:
    #we create 1 object for tunning that are used by car, 
    #and 1 object for unused tunning slot becouse no car used it
    TunningSlot = {} #{"Value": zzz , "hTunningSlotLocation": zz}
    RoofScoop = {}
    Hood = {}
    Rims = {}
    Paint = {}
    Vinyl = {}
    RimColor = {}
    #"Performance": {}
    Tires = {}
    Brakes = {}
    DriveTrain = {}
    Transmission = {}
    Engine = {}
    Turbo = {}
    Nitro = {}
    Junkman = {}
    IsUsed = False

    def __init__(self, TunningSlot, RoofScoop, Hood, Rims, Paint, Vinyl, RimColor, Tires, Brakes, DriveTrain, Transmission, Engine, Turbo, Nitro, Junkman, IsUsed=False):
        self.TunningSlot = TunningSlot
        self.RoofScoop = RoofScoop
        self.Hood = Hood
        self.Rims = Rims
        self.Paint = Paint
        self.Vinyl = Vinyl
        self.RimColor = RimColor
        #"Performance": {}
        self.Tires = Tires
        self.Brakes = Brakes
        self.DriveTrain = DriveTrain
        self.Transmission = Transmission
        self.Engine = Engine
        self.Turbo = Turbo
        self.Nitro = Nitro
        self.Junkman = Junkman
        self.IsUsed = IsUsed

    def __repr1__(self):
        pass

    def print_tunningslot(self):
        from pprint import pprint
        pprint(vars(self))

    def pretty_print_tunningslot(self):
        print("TunningSlot:{} hLocation:{}".format(self.TunningSlot["Value"].hex()[:2], hex(self.TunningSlot["hLocation"])))  


class CareerSlot:
    CareerSlot = {}
    Impound = {}
    Unused1 = {}
    HeatLevel = {}
    Bounty = {}
    Infractions = {}
        
    def __init__(self, CareerSlot, Impound, Unused1, HeatLevel, Bounty, Infractions,):
        self.CareerSlot = CareerSlot
        self.Impound = Impound
        self.Unused1 = Unused1
        self.HeatLevel = HeatLevel
        self.Bounty = Bounty
        self.Infractions = Infractions

    def __repr1__(self):
        pass

    def print_careerslot(self):
        from pprint import pprint
        pprint(vars(self))

    def pretty_print_careerslot(self):
        print("CareerSlot:{} hLocation:{}".format(self.CareerSlot["Value"].hex(), hex(self.CareerSlot["hLocation"])))  


def read_cars_from_savefile1():
    #Insert car objects to Car_List 
    
    # Use global scobe to empty the list becouse without it old items will be in list
    global Car_List
    Car_List = []
    
    #0x5BC5 - location of first Bonus Car 
    #inptr.seek(0x14, 1) - seek next (14 hex) from current position (1 - parameter means continue from here)
    inptr.seek(0x5BC5)
    
    #31 = 1F (convert int to hex); 1F*14=26C ; 26C + 0x5BC5 - location of first Stock Car 
    #50 = 32 (convert int to hex); 32*14=3E8 ; 3E8 + 0x5e31 - location of first Player Car
    #if player win all the cars there must be at leas 15 cars in garage + other cars that player buyed
    #there are 200 limit of car slots in savefile alocated
    for ic in range(1,201):
        # inptr.tell() - return current location of cursor - "inptr.seek(0x5BC5)"
        hCarLocation = inptr.tell()
        
        #there are (14 hex) for each slot
        bSlotNumber = inptr.read(0x4)
        if(bSlotNumber.hex() == "ffffffff"):
            #if find FFFFFFF is empty car slot, they can be added by user
            break
        #1 hex = XX, 4 hex = XX XX XX XX
        #0x8 - (8 hex) value long
        #keep in mind inptr.read(xx) - always move position to the end
        #inptr.read(0x8) - read (8 hex) data and move cursor to the end of readed hexes
        bCarCode = inptr.read(0x8)
        bCarCategory = inptr.read(0x4)
        bTunningSlot = inptr.read(0x1)
        bCareerSlot = inptr.read(0x3)
        #bDelimiter = inptr.read(2) # last 2 hex is CDCD
        
        if ic <= 31:
            CarType = "BonusCar"
        if ic <= 81 and ic > 31:
            CarType = "StockCar"
        if ic > 81 and bCareerSlot.hex()[:2] != "ff":
            CarType = "PlayerCar"
        elif ic > 81 and bCareerSlot.hex()[:2] == "ff":
            CarType = "ShopCar"
        
        CarName = ""
        #Find Car Names form CarNameList
        for i in CarNameList:
            if i["CarCode"].casefold() == str(bCarCode.hex()).casefold() and bSlotNumber.hex().casefold().startswith(i["CarSlot"].casefold()):
                CarName = i["CarName"]
                
        #Find Car Names by comparing tunnig slot from BonusCarNameList
        for i in BonusCarNameList:
            if i["TunningSlot"].casefold() == str(bTunningSlot.hex()).casefold() and CarName == "":
                CarName = "*" + i["CarName"]
        
        #whene modding with vlted some cars don display carnames so need this lines
        if CarName == "" and str(bTunningSlot.hex()).casefold() == "ff":
            for i in CarNameList:
                if i["CarCode"].casefold() == str(bCarCode.hex()).casefold():
                    CarName = i["CarName"]
                
        #Create new object Car
        new_car = Car(CarName, CarType, bSlotNumber, bCarCode, bCarCategory, bTunningSlot, bCareerSlot, hCarLocation, )
        Car_List.append(new_car)

    #Player Car Names will change by using Car Category - (01 = Stock, 02 = Career, 04 = My Cars, 08 = Bonus Cars, 42 = Cars You Won)
    for i in Car_List:
        for j in Car_List:
            if i.CarType == "PlayerCar" and i.CarName == "" and (i.bCarCategory.hex()[:2] not in ["01", "04", "08", "42"]):
                if i.bCarCode == j.bCarCode and (Car_List.index(j) > 31):
                    i.CarName = "Player " + j.CarName
                    break
            elif i.CarType == "PlayerCar" and i.CarName == "" and (i.bCarCategory.hex()[:2] in ["01", "04", "08", "42"]):
                if i.bCarCode == j.bCarCode:
                    i.CarName = j.CarName
                    break
            elif i.CarType == "ShopCar" and i.CarName == "":
                if i.bCarCode == j.bCarCode:
                    i.CarName = j.CarName
                    break                


def get_cars1():
    print()
    print("Cars: (There is room for 200 Cars total)")
    print("Bonus Cars: 1-31, Stock Cars: 32-81, Player Cars: 82-200(FFFFFFFF)")
    c = 1
    for i in Car_List:
        print("{:02d}".format(c), end=" ")
        i.pretty_print_car()
        c = c + 1


def read_tunningslots_from_savefile1():
    
    global Tunning_Slot_List
    Tunning_Slot_List = []
    
    # 1 - tunning slot is size of (198 hex)
    #0x6B65 - location of first Tunning Slot
    inptr.seek(0x6B65)

    for i in range(75):
        hTunningSlotLocation = inptr.tell()
        hCurrTunningSlot = inptr.tell()
        bTemp = inptr.read(0x194)
        bTunningSlot = inptr.read(0x4)
        if(bTunningSlot.hex() == "ffcdcdcd"):
            continue
        
        hRoofScoop = hCurrTunningSlot + 0x7C
        inptr.seek(hRoofScoop)
        bRoofScoop = inptr.read(0x2)
        hHood = hCurrTunningSlot + 0x7E
        inptr.seek(hHood)
        bHood = inptr.read(0x2)
        hRims = hCurrTunningSlot + 0x84
        inptr.seek(hRims)
        bRims = inptr.read(0x2)
        hPaint = hCurrTunningSlot + 0x98
        inptr.seek(hPaint)
        bPaint = inptr.read(0x2)
        hVinyl = hCurrTunningSlot + 0x9A
        inptr.seek(hVinyl)
        bVinyl = inptr.read(0x2)
        hRimColor = hCurrTunningSlot + 0x9C
        inptr.seek(hRimColor)
        bRimColor = inptr.read(0x2)
        hPerformance = hCurrTunningSlot + 0x118
        inptr.seek(hPerformance)
        
        #bPerformance = inptr.read(0x1F)
        #(Tires, Brakes, Drive train, Transmission, Engine, Turbo, Nitro, Unique (each 4 bytes). 
        #The unique is a sum (addition) of the following codes (in hex): 01 = Tire, 02 = Brakes, 04 = Drive train, 08 = Transmission, 10 = Engine, 20 = Turbo, 40 = Nitro, therefore a sum of "7F" arises for all installed Unique.
        # If car does not have for example engine ultimate in bin files of game but you insert 04 00 00 00 game will crash.
        #01 00 00 00 
        #01 00 00 00 
        #01 00 00 00 
        #01 00 00 00 
        #01 00 00 00 
        #01 00 00 00 
        #03 00 00 00 
        #in reverse order - this will mean that when we will add an value it will be like '00 00 00 04' so need to reverse to '04 00 00 00'
        hTires = hCurrTunningSlot + 0x118
        bTires = inptr.read(0x4)
        hBrakes = inptr.tell()
        bBrakes = inptr.read(0x4)
        hDriveTrain = inptr.tell()
        bDriveTrain = inptr.read(0x4)
        hTransmission = inptr.tell()
        bTransmission = inptr.read(0x4)
        hEngine = inptr.tell()
        bEngine = inptr.read(0x4)
        hTurbo = inptr.tell()
        bTurbo = inptr.read(0x4)
        hNitro = inptr.tell()
        bNitro = inptr.read(0x4)
        
        # 7F 00 00 00
        hJunkman = inptr.tell()
        bJunkman = inptr.read(0x4)
        
        # for the next iteration need to move cursor to the (198 hex)
        inptr.seek(hCurrTunningSlot)
        inptr.read(0x198)

        #Create new object Tunning Slot
        new_tunning_slot = TunningSlot(
        {"Value": bTunningSlot, "hLocation": hTunningSlotLocation},
        {"Value": bRoofScoop, "hLocation": hRoofScoop},
        {"Value": bHood, "hLocation": hHood},
        {"Value": bRims, "hLocation": hRims},
        {"Value": bPaint, "hLocation": hPaint},
        {"Value": bVinyl, "hLocation": hVinyl},
        {"Value": bRimColor, "hLocation": hRimColor},
        #"Performance": {}
        {"Value": bTires, "hLocation": hTires},
        {"Value": bBrakes, "hLocation": hBrakes},
        {"Value": bDriveTrain, "hLocation": hDriveTrain},
        {"Value": bTransmission, "hLocation": hTransmission},
        {"Value": bEngine, "hLocation": hEngine},
        {"Value": bTurbo, "hLocation": hTurbo},
        {"Value": bNitro, "hLocation": hNitro},
        {"Value": bJunkman, "hLocation": hJunkman},
        False)
        Tunning_Slot_List.append(new_tunning_slot)
                
    #Add tunning slot to the Car if Car have it
    for tunning_slot in Tunning_Slot_List:
        for car in Car_List:
            if [key.hex() for key in car.TunningSlot.keys()][0] == tunning_slot.TunningSlot["Value"].hex()[:2]:
                for k,v in car.TunningSlot.items():
                    car.TunningSlot[k] = tunning_slot


def get_tunningslots1():
    print()    
    print("Tunning Slots: (There is room for 75 Tunning Slots total)")
    print("(formula - 00006B65+(XX*198), where XX is TunningSlot from 'Player Cars')")
    c = 1
    for i in Tunning_Slot_List:    
        print("{:02d}".format(c), end=" ")
        i.pretty_print_tunningslot()
        c = c + 1

def read_career_slots_from_savefile1():
    
    global Career_Slot_List
    Career_Slot_List = []
    
    #0x6B65 - location of first Tunning Slot
    #formula - (first address of the career slot "0000E2ED") + (slot length "38"  * slot number "00")
    #0000E2ED + 00*38 = 0000E2ED (location of first career slot)
    #24 cars maximum in garage, so 24 max career slot
    #25-th is empty slot "ffcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd0000000000000000000000000000000000000000000000000000000000000000"
    #new car slot        "17cd0300000000000000cdcd0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    #An entry is 56 bytes (38 hex) long.
    #In Career Slot there are kept the Heat Level, Impound Strikes, Bounty, Infractions, etc. for each car
    inptr.seek(0xE2ED)
    for i in range(0,25):

        hCareerSlot = inptr.tell()
        
        #An slot is 56 bytes (38 hex) long
        bCareerSlot = inptr.read(0x2)
        #IF slot starts with "FF" then is an empty so break the loop
        if(bCareerSlot.hex()[:2] == "ff"):
            break	
        
        #Impound Strykes(it can have values between 3 and 5)
        hImpound = inptr.tell()
        #reversed order of bytes
        bImpound = inptr.read(0x2)
        
        hUnused1 = inptr.tell()
        bUnused1 = inptr.read(0x8)
        
        hHeatLevel = inptr.tell()
        #floating hex in reversed order of bytes
        #struct.unpack('!f', bytes.fromhex('0000803f'))[0]
        #1.0
        #example: 1.0 convertedd in hex = 3f800000, but in binary is displayed as 0000803f
        #1.0 = 3f800000 in reversed will be 0000803f
        #2.0 = 40000000 in reversed will be 00000040
        #3.0 = 40400000 in reversed will be 00004040
        #4.0 = 40800000 in reversed will be 00008040
        #5.0 = 40A00000 in reversed will be 0000A040
        #Note: The highest heat level you can reach depends from where you are in the career. If you put it at a higher value than you are supposed to, it will be automatically changed to the maximum allowed.
        bHeatLevel = inptr.read(0x4)
        
        hBounty = inptr.tell()
        #reversed order of bytes
        #example: 4.100.000 convertedd in hex = 3e8af000, but in binary is displayed as a08f3e00
        #(1 << 32) - 1 = 4294967295 (equal FFFFFFFF hex is MAx)
        bBounty = inptr.read(0x4)
        
        hInfractions = inptr.tell()
        #reversed order of bytes
        #meaning: 0f00(15 evades) 0200(2 busted) (0100 0100 0100 0100 0000 0100 0100 0100)unserved infraction    (0600 0600 0600 1000 0000 0700 0e00 0900)served infraction
        bInfractions = inptr.read(0x24)
        
        new_career_slot = CareerSlot(
        {"Value": bCareerSlot, "hLocation": hCareerSlot},
        {"Value": bImpound, "hLocation": hImpound},
        {"Value": bUnused1, "hLocation": hUnused1},
        {"Value": bHeatLevel, "hLocation": hHeatLevel},
        {"Value": bBounty, "hLocation": hBounty},
        {"Value": bInfractions, "hLocation": hInfractions},
        )
        Career_Slot_List.append(new_career_slot)
    
    #Add career slot to cars
    for career_slot in Career_Slot_List:
        for car in Car_List:
            if [key.hex()[:2] for key in car.CareerSlot.keys()][0] == career_slot.CareerSlot["Value"].hex()[:2]:
                for k,v in car.CareerSlot.items():
                    car.CareerSlot[k] = career_slot


def get_career_slots1():
    print()
    c = 1
    for i in Career_Slot_List:
        print("{:02d}".format(c), end=" ")
        i.pretty_print_careerslot()
        c = c + 1
        

def read_bonus_markers_from_savefile1():
    #save editor by Xie Hui gives error when limits is more than 35 so need to check if it gives error when there is more from 0 to 35 
    #Bonus Marker Slot is 12 bytes long (C hex)
    global Marker_List
    Marker_List = []
    
    inptr.seek(0x5739)
    for i in range(63):
        MarkerName = ""
        hMarkerLocation = hex(inptr.tell())
        bMarker = inptr.read(0xC)
        for marker in MarkerNameList:
            if marker['bMarker'].casefold() == str(bMarker.hex()).casefold():
                MarkerName = marker['MarkerName']
        #print("{:02d}: MarkerName:{:20s} Marker:{} hLocation:{}".format(i+1, MarkerName, bMarker.hex(), hMarkerLocation, ))

        Marker_List.append(
        {"MarkerNum": i,
        "hMarkerLocation": hMarkerLocation,
        "bMarker": bMarker,
        "MarkerName": MarkerName,
        "MarkerCount": 0,
        })


def get_markers1():
    print("Bonus marker: (There is room for 63 Markers total)")
    for i in Marker_List:
        #print(i)
        print("{:02d} MarkerName:{:20s} Marker:{} hLocation:{}".format(i["MarkerNum"]+1, i["MarkerName"], i["bMarker"].hex(), i["hMarkerLocation"], ))
    

def set_markers1():
    
    inptr.seek(0x5739)
    for i in MarkerNameList:
        #print((int(i["bMarker"],16)).to_bytes(12, byteorder="big", signed=False))
        for j in range(3):
            inptr.write((int(i["bMarker"],16)).to_bytes(12, byteorder="big", signed=False))
    
    read_bonus_markers_from_savefile1()
    get_markers1()
    
    print("Done!")


def none_to_string(var):
    if var == None:
        return ""
    else:
        return var

def print_list_as_3_columns(items):
    import itertools
    myList = []
    N = 3  # desired number of parts
    c = 1
    for i in items:
        myList.append("{:02d} {}".format(c, i.CarName))
        c = c + 1    

    col_initial = len(items) // 3
    remainder = len(items) % 3
    z = 0
    col_list = [col_initial, col_initial, col_initial]
    # divide list into 3 unequal lenght, first 2 columns will be bigger if remainder is not 0
    for i in range(1, len(list(range(1,remainder+1))) % col_initial + 1):
        col_list[i-1] = col_list[i-1] + 1 
           
    for i in itertools.zip_longest(myList[:col_list[0]], myList[col_list[0]:col_list[0]+col_list[1]], myList[col_list[0]+col_list[1]:col_list[0]+col_list[1]+col_list[2]]):
        print("{:33s} {:32s} {}".format(none_to_string(i[0]), none_to_string(i[1]), none_to_string(i[2])))

    
def get_car1(items):
    print()
    #c = 1
    #for i in items:
    #    print(c, " - ", i.CarName)
    #    c = c + 1 
    
    print_list_as_3_columns(items)
    
    try:
        car_option = int(input("Select Car: "))
    except ValueError:
        print("Invalid Option. Returning to Menu!")
        return

    #print(' '.join(["".join((key,':',value)) for key, value in Car_List[int(car_option)-1].items()]))
    #print(["".join((key,':',value)) for key, value in Car_List[int(car_option)-1].items()])
    #print(Car_List[int(car_option)-1].CarName)
    
    return Car_List[int(car_option)-1]


def get_tunning1(items):
    print()
    c = 1
    for i in Tunning_Slot_List:
        print("{:02d}".format(c), i.TunningSlot["Value"].hex())
        c = c + 1
   
    try:
        tun_option = int(input("Select Tunning Slot: "))
    except ValueError:
        print("Invalid Option. Returning to Menu!")
        return
       
    return Tunning_Slot_List[int(tun_option)-1]


def change_car_vinyl1(car, vinyl="ffff"):

    print()
    tunning_slot = [v for k,v in car.TunningSlot.items()][0]
    print("{} Tunning Slot: '{}' '{}'".format(car.CarName, tunning_slot.TunningSlot["Value"].hex(), hex(tunning_slot.TunningSlot["hLocation"])))
    yn = input("Do you want to change '{}' - Vinyl '{}' to '{}' ? (y/n): ".format(car.CarName, tunning_slot.Vinyl["Value"].hex(), vinyl))
    if yn == "y":
        inptr.seek(tunning_slot.Vinyl["hLocation"])
        binstr = binascii.unhexlify(vinyl)
        inptr.write(binstr)
        inptr.seek(tunning_slot.Vinyl["hLocation"])
        print("'{}' Vinyl changed from '{}' to '{}' ".format(car.CarName, tunning_slot.Vinyl["Value"].hex(), inptr.read(0x2).hex()))

        print("Done!")
        
def change_car_category1(car):
    # change CarCategory „20“ to a 21, so that the car will be available on both categories.
    # change CarCategory of bonus car "08" -> "01" or "02"
    
    print("Car category (01 = Stock, 02 = Career, 04 = My cars, 08 = Bonus cars, 42 = Cars you won)")
    if car.bCarCategory.hex()[:2] in ["04", "08", "20", "21", "42"]:
        print(car.CarName, "car category is: ", car.bCarCategory.hex()[:2])
        inptr.seek(car.hCarLocation)
        #12*xx position to move in hex is C 
        inptr.seek(0xC, 1)

        opt_t = input("Choose new car category \n1 stock \n2 career \n3 my cars \n20 disable special \n21 enable special in career \npress enter to not change (1/2/3/20/21): ")
        if opt_t == str(1) and car.bCarCategory.hex()[:2] not in ["20", "21"]:
            inptr.write((0x1).to_bytes(1, byteorder="little", signed=False))        
        elif opt_t == str(2) and car.bCarCategory.hex()[:2] not in ["20", "21"]:
            inptr.write((0x2).to_bytes(1, byteorder="little", signed=False))
        elif opt_t == str(3) and car.bCarCategory.hex()[:2] not in ["20", "21"]:
            inptr.write((0x4).to_bytes(1, byteorder="little", signed=False))
        elif opt_t == str(3) and car.bCarCategory.hex()[:2] not in ["20", "21"]:
            inptr.write((0x4).to_bytes(1, byteorder="little", signed=False))
        elif opt_t == str(20) and car.bCarCategory.hex()[:2] in ["20", "21"]:
            inptr.write((0x20).to_bytes(1, byteorder="little", signed=False))
        elif opt_t == str(21) and car.bCarCategory.hex()[:2] in ["20", "21"]:
            inptr.write((0x21).to_bytes(1, byteorder="little", signed=False))  
            
        if opt_t in [str(1), str(2), str(3), str(20), str(21)]:
            inptr.seek(car.hCarLocation)
            inptr.seek(0xC, 1)
            changed_t = inptr.read(0x1).hex()
            if car.bCarCategory.hex()[:2] != str(changed_t):
                print(car.CarName, "category changed from '{}' to '{}'".format(car.bCarCategory.hex()[:2], changed_t))
            else:
                print(car.CarName, "category not changed" )
    
            print("Done!")
    
    else:
        print( "Cannot change car category for Player or Stock car '{}'".format(car.CarName,))


def change_tunning_slot_career_my_cars1(bonus_car):
    #This function will create new Tunning Slot for Player Car (Garage) and fill it with existing tunning slot from bonus or other if they are not empty
    #You should have a car like the one of the corresponding Bonus Car in My Cars or in Career, for the which you should copy the corresponding Tuning Slot on.
    
    tunning_slot_bonus = None # will store tunning slot of bonus car
    tunning_slot_player = None # will store tunning slot of player car
    player_car = None
    tun_list = []
    player_car_list = []
    
    print()

    if bool([v for k,v in bonus_car.TunningSlot.items()][0]):
        tunning_slot_bonus = [v for k,v in bonus_car.TunningSlot.items()][0]
    else:
        print("Bonus car '{}' doesnt have TunningSlot.".format(bonus_car.CarName))
        return

    # verify if selected car exist in garage 
    for i in Car_List:        
        if i.bCarCode == bonus_car.bCarCode and i.CarType == "PlayerCar":
            player_car_list.append(i)

    if len(player_car_list) == 0:
        print("No similar car model in garage! Please go to career and buy it from store!")
        return
    #if there are more similar car model in garage    
    elif len(player_car_list) > 1:
        print("There are more similar car model in garage:")
        t_count = 0
        for p in player_car_list:
            t_count = t_count + 1
            print(t_count, p.CarName)
        try:
            car_option = int(input("Select Car: "))
        except ValueError:
            print("Invalid Option. Returning to Menu!")
            return
            
        if t_count >= car_option:
            player_car = player_car_list[car_option-1]
    else:
        player_car = player_car_list[0]  
       
    print("Bonus  '{}' car Tunning Slot: '{}' '{}' ".format(bonus_car.CarName, tunning_slot_bonus.TunningSlot["Value"].hex()[:2], hex(tunning_slot_bonus.TunningSlot["hLocation"])))
    if bool([v for k,v in player_car.TunningSlot.items()][0]):
        tunning_slot_player = [v for k,v in player_car.TunningSlot.items()][0].TunningSlot["Value"]
        print("Player '{}' car Tunning Slot: '{}' '{}' ".format(player_car.CarName, tunning_slot_player.TunningSlot["Value"].hex()[:2], hex(tunning_slot_player.TunningSlot["hLocation"])))
    else:
        print("Player '{}' car does not have Tunning Slot.".format(player_car.CarName,))
        tunning_slot_player = None
    
    #This variable will store start adress of free Tunning Slot that is located after last Tunning Slot that is not empty
    hLocation = None
    
    #0x6B65 - location of first Tunning Slot
    #0xE2EC - last location alocated for Tunning Slot
    #0 - 74 locations alocated in total so (75 slots)
    # 1 slot = 198 hex
    # last 4 hex of 198 hex looks like this XXFCFCFC - where XX is Slot Number that will be stored in Car Slot 
    inptr.seek(0x6B65)
    for i in range(75):
        hLocation = inptr.tell()
        #we dont need 194 hex but need last 4 hex from 198 hex
        inptr.read(0x194)       
        bTunningSlot = inptr.read(0x4)
        if(bTunningSlot.hex() == "ffcdcdcd"):
            #print(i, bTunningSlot.hex(), hex(hLocation), hex(inptr.tell()))#break
            break
        elif i == 73:
            # 73 is becouse 74 is last empty Tunning Slot that we will use to replace removed slots
            print("There are no more available Tunning Slots. Please remove unused Tunning Slots. Exiting.")
            fix_and_exit()
            pass#print(i, bTunningSlot.hex(), hex(inptr.tell()))
    
    yn = input("Do you want to change '{}' Tunning Slot from '{}' to '{}' (y/n): ".format(player_car.CarName, [k for k,v in player_car.TunningSlot.items()][0].hex(), tunning_slot_bonus.TunningSlot["Value"].hex()[:2]))
    if yn == "y":
        # seek to the tunning slot bonus location
        #inptr.seek(int(tunning_slot_bonus["hTunningSlotLocation"], 16))
        # copy the bonus tunning slot 404 Bytes (194 hex) without XXCDCDCD part, to the player tunning slot
        #bTemp = inptr.read(0x194)
        # gives error savegame so i use bytearray

        bTemp_bonus = bytearray_data[tunning_slot_bonus.TunningSlot["hLocation"]:tunning_slot_bonus.TunningSlot["hLocation"] + int("0x194", 16)]
        inptr.seek(hLocation)
        #write bytes at the current location
        inptr.write(bTemp_bonus)

        # Increment Bonus Car TunninSlot by one (0x5 + 1) (will look like '05CDCDCD') and write it after 194 (hex)
        #print(int(Tunning_Slot_List[-1].TunningSlot["Value"].hex()[:2], 16) + 1)
        inptr.write((int(Tunning_Slot_List[-1].TunningSlot["Value"].hex()[:2], 16) + 1).to_bytes(1, byteorder="little", signed=False))
        
        inptr.seek(hLocation)
        bTemp_player = inptr.read(0x194)
        bTunningSlot_player = inptr.read(0x4)
        #print(bTemp_player.hex())
        inptr.seek(tunning_slot_bonus.TunningSlot["hLocation"])
        bTemp_bonus = inptr.read(0x194)
        bTunningSlot_bonus = inptr.read(0x4)
        
        print("Tunning Slot copied from location '{}' to '{}'".format(hex(tunning_slot_bonus.TunningSlot["hLocation"]), hex(hLocation)))
        print("Player Car Old TunningSlot: {} \nPlayer Car New TunningSlot: {}".format([k for k,v in player_car.TunningSlot.items()][0].hex(), bTunningSlot_player.hex()))

        #we need to replace bTunningSlot first
        inptr.seek(player_car.hCarLocation)
        inptr.read(0x10)
        inptr.write((int(bTunningSlot_player.hex()[:2], 16)).to_bytes(1, byteorder="little", signed=False))
        
        print("Done!")
        
    else:
        if tunning_slot_player != None:
            print("Try in Hex Editor manually")
            print("Go to location of tunning slot of bonus car, and copy (194 hex) from the position: '{}'".format(hex(tunning_slot_bonus.TunningSlot["hLocation"])))
            print("Then go to location of tunning slot of player car: '{}' . Then select (194 hex) and paste copied code.  ".format(hex(tunning_slot_player.TunningSlot["hLocation"])))  
        

def remove_tunning_slot1(tunning_slot):
    #1.get last empty tunning slot
    #2.copy empty tunning slot to the location that need to be removed
    print()
    #This variable will store start adress of free Tunning Slot that is located after last Tunning Slot that is not empty
    hLocation = None
    
    inptr.seek(0x6B65)
    for i in range(75):
        hLocation = inptr.tell()
        #we dont need 194 hex but need last 4 hex from 198 hex
        inptr.read(0x194)       
        bTunningSlot = inptr.read(0x4)
        if i == 74 and (bTunningSlot.hex() == "ffcdcdcd"):
            # 73 is becouse 74 is last empty Tunning Slot that we will use to replace removed slots
            pass
        elif i < 74 and (bTunningSlot.hex() == "ffcdcdcd"):
            break
        elif i == 74 and (bTunningSlot.hex() != "ffcdcdcd"):
            print("Last Empty Slot is damaged. Please Remove tunning slot with Hex Editor!")
            fix_and_exit() 
    
    for i in Car_List:
        if [v for k,v in i.TunningSlot.items()][0] == {}:
            pass
        elif [v for k,v in i.TunningSlot.items()][0].TunningSlot["Value"] == tunning_slot.TunningSlot["Value"]:
            print("Tunning Slot '{}' is used by '{}'".format(tunning_slot.TunningSlot["Value"].hex(), i.CarName,))
            print("Exiting")
            return
            
    yn = input("Do you want to remove Tunning Slot '{}' from location '{}' ?(y/n): ".format(tunning_slot.TunningSlot["Value"].hex(), hex(hLocation)))
    if yn == "y":
        
        #we write (198 hex) not only 194 hex, becouse we need to empty tunning number
        bTemp = bytearray_data[hLocation:hLocation + int("0x198", 16)]
        inptr.seek(tunning_slot.TunningSlot["hLocation"])
        inptr.write(bTemp)
        print("Tunning Slot '{}' emptied!".format(tunning_slot.TunningSlot["Value"].hex()))
        
        print("Done!")
        
    else:
        print("Try in Hex Editor manually")
        print("Go to location of last empty tunning slot, and copy (198 hex) from the position: '{}'".format(hex(hLocation)))
        print("Then go to location of tunning slot that need to remove: '{}' . Then select (198 hex) and paste copied code.  ".format(hex(tunning_slot.TunningSlot["hLocation"]))) 
    

def add_car_to_career_garage1(item):
        
    hCarLocation = None
    
    # find first empty location
    inptr.seek(0x5BC5)
    for i in range(1,200):
        hCarLocation = hex(inptr.tell())
        # there are (14 hex) for each entry
        bSlotNumber = inptr.read(0x4)
        if(bSlotNumber.hex() == "ffffffff"):
            #if find FFFFFFF then there are no more cars in Player Career Garage
            break
        bCarCode = inptr.read(0x8)
        bCarCategory = inptr.read(0x4)
        bTunningSlot = inptr.read(0x1)
        bCareerSlot = inptr.read(0x3)

    inptr.seek(int(hCarLocation, 16))
    bSlotNumber = inptr.read(0x4)
    bCarCode = inptr.read(0x8)
    bCarCategory = inptr.read(0x4)
    bTunningSlot = inptr.read(0x1)
    bCareerSlot = inptr.read(0x3)
    
    tunning_slot_bonus = None # will store tunning slot of bonus car
    tunning_slot_player = None # will store tunning slot of player car
    bonus_car = None
    player_car = None
     
    bonus_car = item
    
    #need to add career slot
    #new car slot - "17cd0300000000000000cdcd0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    #else go to garage and remove some cars
    if len(Career_Slot_List) <= 23 and len(Career_Slot_List) != 0:         
        print("Total amount of Career Slots: '{}' ".format(len(Career_Slot_List)))            
        print("Get last used Career Slot: '{}' at location '{}'".format(str(hex(int(Career_Slot_List[-1].CareerSlot["Value"].hex()[:2], 16))[2:]), hex(Career_Slot_List[-1].CareerSlot["hLocation"])))
        
        inptr.seek(Career_Slot_List[-1].CareerSlot["hLocation"] + int("0x38", 16))
        print("Add new Career Slot: '{}' at location '{}'".format(hex(int(Career_Slot_List[-1].CareerSlot["Value"].hex()[:2], 16) + 1)[2:] , hex(inptr.tell())))

        new_career_slot = binascii.unhexlify("{:02x}".format(int(hex_decode(Career_Slot_List[-1].CareerSlot["Value"].hex()[:2])[0].hex(),16) + int("01",2)) +  "cd0300000000000000cdcd0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")

        inptr.write(new_career_slot)
    elif len(Career_Slot_List) == 0:
        print("There are '0' created Career Slots. Please go to your career and buy a car from store.(Bug in case ExtraOptions is installed)")
        return
    else:
        print("There are no available Career Slots. Please go to you career garage and remove a car.")
        return

    CarName = bonus_car.CarName
    CarType = "PlayerCar"
    bSlotNumber = hex(int(Car_List[-1].bSlotNumber.hex()[:2], 16) + 1)[2:] +  "000000"
    bCarCode = bonus_car.bCarCode
    bCarCategory = "02000f00"
    bTunningSlot = "ff"
    bCareerSlot =  "{:02x}".format(int(hex_decode(Career_Slot_List[-1].CareerSlot["Value"].hex()[:2])[0].hex(),16) + int("01",2)) + "cdcd"
    
    yn = input("Do you want to add '{}' '{}' to career garage (y/n): ".format(bonus_car.CarType, CarName))
    if yn == "y":
        print("Add new Car:", bSlotNumber, bCarCode.hex(), bCarCategory, bTunningSlot + bCareerSlot, "at location:", hCarLocation)
        newCar = binascii.unhexlify(bSlotNumber + bCarCode.hex() + bCarCategory + bTunningSlot + bCareerSlot)
        inptr.seek(int(hCarLocation, 16))
        inptr.write(newCar)
        #ffffffff 0000000000000000 00000000 ffffcdcd
        #63000000 eaa5c042eaa5c042 02000f00 3112cdcd        
        
        print("'{}' added to garage cars but without tunning slot.".format(CarName))
        
        #Refresh data from savefile
        #Get last tunning slot that is not empty and place the next empty slot
        read_cars_from_savefile1()
        read_tunningslots_from_savefile1()
        read_career_slots_from_savefile1()
        
        
        if bool([v for k,v in bonus_car.TunningSlot.items()][0]):
            print()
            print("Changing Tunning Slot")
            change_tunning_slot_career_my_cars1(bonus_car)
            
        # #bonus car can not have tunning slot
        # #and player car car can not have tunning slot becouse is setted to "ff"
        # for i in Tunning_Slot_List:
            # # if dict is empty - this is in case tunning slot have value "ff"
            # if bool([v for k,v in bonus_car.TunningSlot.items()][0]):
                # if i.TunningSlot["Value"] == [v for k,v in bonus_car.TunningSlot.items()][0].TunningSlot["Value"]:
                    # tunning_slot_bonus = i
                    # print(i)                    

        #if tunning_slot_bonus == None:
        #    print("Prototype Car doesnt have Tunning Slot. Go to change tunning slot option from menu.")
        #    return
            
        # print("Prototype Car '{}' tunning slot location: '{}'".format(bonus_car.CarName, hex(tunning_slot_bonus.TunningSlot["hLocation"]), ))

        # zz = binascii.unhexlify([v for k,v in Car_List[-1].TunningSlot.items()][0].TunningSlot["Value"] + "CDCDCD")
        # bTemp = bytearray_data[tunning_slot_bonus.TunningSlot["hLocation"]:tunning_slot_bonus.TunningSlot["hLocation"] + int("0x194", 16)]
        # print(bTemp + zz)
        # # instead of 0x194 need 0x198, becouse need to append after XXCDCDCD
        # inptr.seek(tunning_slot_player.TunningSlot["hLocation"] + int("0x198", 16))
        # inptr.write(bTemp + zz)       


def add_cars_to_shop1(car_shop):
    #0 - 30 - Bonus Cars
    #31 - 80 - Stock Cars
    #81 - 131 - Carrer Cars (50 its good )
    #131 - Reserved for non garage cars
    #200 - XXXX - the last free location
    
    #20 bytes for a car is (14 in hex)
    #hCarLocation = int("0x5BC5", 16) + 131 * 20
    #print(hex(hCarLocation))
    #inptr.seek(hCarLocation)
    #bCar = inptr.read(0x14)
           
    # get last car in Car List and add to hCarlocation 20 bytes (14 hex)
    hCarLocation = Car_List[-1].hCarLocation + 20
    bSlotNumber = str(hex(int(Car_List[-1].bSlotNumber.hex()[:2], 16) + 1))[2:] + "000000"
    bCarCode = car_shop.bCarCode
    bCarCategory = "01000f00" # 01 - means stock
    bTunningSlot = "ff" # ff - means that car do not have tunning slot so it will use default     
    bCareerSlot = "ffcdcd" # ff - means career number of car, but becouse it is not used if have value 'ff'
    
    print()
    for i in Car_List:
        if [v for k,v in i.CareerSlot.items()][0] != {} or [v for k,v in i.TunningSlot.items()][0] != {}:
            pass
        elif i.bCarCode == bCarCode and i.bCarCategory == bCarCategory and [v for k,v in i.TunningSlot.items()][0].TunningSlot["Value"].hex()[:2] == bTunningSlot and [v for k,v in i.CareerSlot.items()][0].CareerSlot["Value"].hex()+"cd" == bCareerSlot and int(bSlotNumber[:2],16) > 81:
            print( i.CarName, "already exist on shop.")
            return
       
    inptr.seek(hCarLocation)
    bCar = inptr.read(0x14)
    #if str(bCar.hex()).casefold() == "ffffffff000000000000000000000000ffffcdcd".casefold():
    if str(bCar.hex()).casefold()[:8] == "ffffffff".casefold():    
        print("There is available location for car: ", bCar.hex(), "hCarLocation:", hex(hCarLocation))
    else:
        print(bCar.hex(), "There is no available location for car.")

    #5B000000 AF2DC3C1 6D807CD3 01000F00 FFFFCDCD
    #01000F00 - 01 make available car in stock
    print("New Car data will look like this: ", bSlotNumber, bCarCode.hex(), bCarCategory, bTunningSlot + bCareerSlot, "hCarLocation:", hex(hCarLocation))
    newCar = binascii.unhexlify(bSlotNumber + bCarCode.hex() + bCarCategory + bTunningSlot + bCareerSlot)
    #print(newCar.hex())

    yn = input("Do you want to add '{}' to the shop?(y/n): ".format(car_shop.CarName))
    if yn == "y":  
        inptr.seek(hCarLocation)
        inptr.write(newCar)
        inptr.seek(hCarLocation)
        print("Result is: ", inptr.read(0x14).hex())
        
        print("Done!")

    #in future here will need to be added tunning slot for bonus cars, becouse in shop car is with no tunnig slot, simple


def remove_car_from_shop():
    pass
    

def get_heat_level1(car=None):
    #HeatLevel is in reversed order
    if car.CarType == "PlayerCar":
        career_slot = [v for k,v in car.CareerSlot.items()][0]
        heat_level = struct.unpack('!f', career_slot.HeatLevel["Value"])[0]
        if heat_level < 1.0:
            heat_level = 1.0
        print("'{}' heat level is: {:.2f}".format(car.CarName, heat_level))      
    else:
        print("'{}' is not a Career Car so it doesnt have heat level".format(car.CarName))
        return   
    
    return heat_level


def set_heat_level1(car=None):
    #HeatLevel is in reversed order
    
    get_heat_level1(car)
    
    if car.CarType == "PlayerCar":
        career_slot = [v for k,v in car.CareerSlot.items()][0]

        #1.0 = 3f800000 in reversed will be 0000803f
        #2.0 = 40000000 in reversed will be 00000040
        #3.0 = 40400000 in reversed will be 00004040
        #4.0 = 40800000 in reversed will be 00008040
        #5.0 = 40A00000 in reversed will be 0000A040  
        
        c = 1
        for i in range(5):
            print("{}".format(c), "{:.2f}".format(i + 1))
            c = c + 1 
        try:
            heat_level_option = int(input("Select heat level: "))
        except ValueError:
            print("Invalid Option. Returning to Menu!")
            return
        
        if heat_level_option <= 5:
            
            inptr.seek(career_slot.HeatLevel["hLocation"])
            #convert float to reversed bytes, for that i used "!f" not "f"
            inptr.write(struct.pack("!f", float(heat_level_option)))
            print("Done!")
        else:
            print("Invalid Option. Returning to Menu!")
    else:
        print("'{}' is not a Career Car so it doesnt have heat level".format(car.CarName))
        return


def get_bounty1(car=None):
    #Bounty is in reversed order
    if car.CarType == "PlayerCar":
        career_slot = [v for k,v in car.CareerSlot.items()][0]
        bounty = struct.unpack('i', career_slot.Bounty["Value"])[0]
        print("'{}' bounty is:".format(car.CarName), "{:,}".format(bounty).replace(",", "."))
    else:
        print("'{}' is not a Career Car so it doesnt have bounty".format(car.CarName))
        return
        
    return bounty


def set_bounty1(car=None):
    #Bounty is in reversed order
    
    get_bounty1(car)
    
    if car.CarType == "PlayerCar":
        career_slot = [v for k,v in car.CareerSlot.items()][0]
        Obounty = struct.unpack('i', career_slot.Bounty["Value"])[0]
        try:
            bounty = int(input("Set Bounty: "))
        except:
            print("Invalid value. Returning to Menu!")
            return
        print("Writing modified bounty... ", end="")
        if (bounty > ((1 << 31) - 1)):
            Obounty = ((1 << 31) - 1)
        if (bounty == 0):
            bounty = Obounty
        elif (bounty == -1):
            bounty = 0
        inptr.seek(career_slot.Bounty["hLocation"])
        inptr.write((bounty).to_bytes(4, byteorder="little", signed=False)) # not writing
        print("Done!")
        
        read_career_slots_from_savefile1()
        get_bounty1(car)
    else:
        print("'{}' is not a Career Car so it doesnt have bounty".format(car.CarName))
        return


def is_valid_savefile():
    #Open the File and Check if it is valid i.e. 20CM
    inptr.seek(0x0)
    bMAGIC = inptr.read(4)
    MAGIC = int.from_bytes(bMAGIC, byteorder="little")
    if (MAGIC != 0x4D433032):
        print("Not a Need for Speed: Most Wanted file...")
        inptr.close()
        sys.exit(2)
    inptr.seek(0)


def backup_savefile():
    #Check for backup paremeter then make a backup
    
    if not exists(sys.argv[1] + ".bak1"):
        print("Making backup of the original File... ", end="")
        outptr = open(sys.argv[1] + ".bak1", "wb")
        for line in inptr:
            outptr.write(line)
        outptr.close()
        print("Done!")


def get_savefile_info():
    #Getting Safe File Info
    print()
    inptr.seek(0x5A31)
    bName = inptr.read(8)
    print("Account Info: ")
    Name = (bName).decode("utf-8")
    print("Name: {}".format(Name))
    inptr.seek(0x4039)
    bOMoney = inptr.read(4)
    OMoney = int.from_bytes(bOMoney, byteorder="little")
    print("Money: {}".format(OMoney))


def set_money():
    #Set the money
    #"0" - will not change the money and will keep the current number of money
    #"-1" - will do that (negative one)
    
    inptr.seek(0x4039)
    bOMoney = inptr.read(4)
    OMoney = int.from_bytes(bOMoney, byteorder="little")
    print("Money: {}".format(OMoney))    
    
    inptr.seek(0x4039)
    try:
        Money = int(input("Give Money value: "))
    except:
        Money = 0
        print("No value given. Leave default.")
    else:
        print("Writing modified money '{}'... ".format(Money), end="")
    # (1 << 31) - means 32 byte integer
    if (Money > ((1 << 31) - 1)):
    	Money = ((1 << 31) - 1)
    if (Money == 0):
    	Money = OMoney
    elif (Money == -1):
    	Money = 0
    
    inptr.write((Money).to_bytes(4, byteorder="little", signed=False)) # not writing
    print("Done!")


def get_car_bounty():
    #At 0xE2ED, first car is found
    #If it is sold then its ID is FF else it starts from 00 upward
    #Bounty of that car is found 0xF after ID
    #Next Car is found 0x37 from ID
    inptr.seek(0xE2ED)
    while(1):
        bCar = inptr.read(1)
        Car = int.from_bytes(bCar, byteorder="little")
        if (Car == 0xFF):
            inptr.seek(0x37, 1)
            continue
        else:
            break
    inptr.seek(0xF, 1)
    bOBounty = inptr.read(4)
    print(bOBounty)
    OBounty = int.from_bytes(bOBounty, byteorder="little")
    print("Bounty(1st Car only): {}".format(OBounty))
    print()


def set_car_bounty():
    #Change the bounty of first car
    #"0" will not change the bounty and will keep the current bounty
    #"-1" will do that (negative one)
    
    get_car_bounty()
    
    inptr.seek(0xE2ED)
    while(1):
    	bCar = inptr.read(1)
    	Car = int.from_bytes(bCar, byteorder="little")
    	if (Car == 0xFF):
    		inptr.seek(0x37, 1)
    		continue
    	else:
    		break
    inptr.seek(0xF, 1)
    bBounty = input("Modified Bounty: ")
    print("Writing modified bounty... ", end="")
    Bounty = int(bBounty)
    if (Bounty > ((1 << 31) - 1)):
    	Bounty = ((1 << 31) - 1)
    if (Bounty == 0):
    	Bounty = OBounty
    elif (Bounty == -1):
    	Bounty = 0
    inptr.write((Bounty).to_bytes(4, byteorder="little", signed=False)) # not writing
    print("Done!")


def fix_savefile_checksum():
    #EA used md5 of the portion 0x34 to F8FC for checking the validity of the savefile, calculating the modified md5
    print()
    print("Calculating newer hash... ", end="")
    inptr.seek(0x34)
    HASH = int(hashlib.md5(inptr.read(0xF828)).hexdigest(), 16)
    print("Done!")
    
    #Storing the new md5 at the end
    print("Changing hash in the file's content... ", end="")
    inptr.seek(0xF85C)
    inptr.write((HASH).to_bytes(16, byteorder="big", signed=False))
    print("Done!")
    inptr.close()
 

def fix_and_exit():
    fix_savefile_checksum()
    print("Exiting!")
    sys.exit()
    

def my_search():
    #100 hex after xxcdcdcd
    #10 hex of data to read

    inptr.seek(0x6B65)

    for i in range(75):
        hTunningSlotLocation = inptr.tell()
        hCurrTunningSlot = inptr.tell()
        test = inptr.read(0x106)
        test_data = inptr.read(0xA)
        test = inptr.read(0x84)
        tunning_slot = inptr.read(0x4)

        #inptr.seek(hRoofScoop)
        
        for i in Car_List:
            if [k for k,v in i.TunningSlot.items()][0].hex() == tunning_slot.hex()[:2] and [k for k,v in i.TunningSlot.items()][0].hex() != "ff":
                print("{} {} {}".format(test_data.hex(), i.CarName, tunning_slot.hex(), ) )
        

def menu1():
    while(1):
        
        #new stuff
        read_cars_from_savefile1()
        read_tunningslots_from_savefile1()
        read_career_slots_from_savefile1()
        read_bonus_markers_from_savefile1()
        
        
        #my_search()
        
        
        
        print()
        print("Menu")
        print("1. Get Cars")
        print("2. Get Tuning Slots")
        print("3. Get Career Slots")
        print("4. Get Bonus Markers")
        print("5. Add Car to Shop")
        print("6. Add Car to Career Garage")
        print("7. Change Car Category")
        print("8. Change Tunning Slot of Career Cars or My Cars")
        print("9. Remove Tunning Slot")
        #print("11. Change Car Vinyl")
        print("10. Set Money")
        print("11. Set Heat Level")
        print("12. Set Bounty")
        print("13. Set all Markers to 3")
        print("0. Exit! and Fix SaveFile Checksum")
        
        try:
            option = int(input("Choose option: "))
        except ValueError:
            print("Invalit Option. Exiting!")
            fix_and_exit()
            
        if option == 1:
            get_cars1()
        elif option == 2:
            get_tunningslots1()
        elif option == 3:
            get_career_slots1()
        elif option == 4:
            get_markers1()
        elif option == 5:
            car = get_car1(Car_List)
            if car != None:
                add_cars_to_shop1(car)
        elif option == 6:
            car = get_car1(Car_List)
            if car != None:
                add_car_to_career_garage1(car)
        elif option == 7:
            car = get_car1(Car_List)
            if car != None:
                change_car_category1(car)
        elif option == 8:
            car = get_car1(Car_List)
            if car != None:
                change_tunning_slot_career_my_cars1(car) #4
        elif option == 9:
            tun = get_tunning1(Tunning_Slot_List)
            if tun != None:
                #tun.print_tunningslot()
                remove_tunning_slot1(tun)
        elif option == 10:
            set_money()
        elif option == 11:
            car = get_car1(Car_List)
            if car != None:
                set_heat_level1(car)
        elif option == 12:
            car = get_car1(Car_List)
            if car != None:
                set_bounty1(car)
        elif option == 13:
            set_markers1()
            
        #elif option == 11:
        #    car = get_car1(Car_List)
        #    if car != None:
        #        change_car_vinyl1(car, "3f12")

        elif option == 0 or option > 12:
            fix_and_exit()
       

if __name__ == "__main__":
    #Checking the arguments
    if (len(sys.argv) != 2 ):
        print("Need for Speed: Most Wanted SaveFile Editor v1.1.0 by Dragneel1234 changed by me")
        print()
        print("Usage:")
        print("{} SaveFile".format(sys.argv[0]))
        print()
        sys.exit(1)    
    
    is_valid_savefile()
    backup_savefile()
    get_savefile_info()
    
    menu1()
    fix_and_exit()
    #fix_savefile_checksum()
    
