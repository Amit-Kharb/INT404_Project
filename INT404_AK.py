##################################################
#                                           ######
#               INT404 Project              ######
#       Intelligent System For Tourists     ######
#                                           ######
# Submitted To :    Ms Jasleen Kaur         ######
# Submitted By :    Amit Kharb      (20)    ######
#                   Ritik Chaudhary (21)    ######
#                   Zafar Alam      (19)    ######
# Section : K18NZ                           ######
#                                           ######
##################################################
#                                           ######
# Ques - 51                                 ######
# This program contains a set of questions  ######
# which the user has to reply. Based on the ######
# answer provided by the user, an           ######
# intelligent system returns best results.  ######
#                                           ######
##################################################
#                                           ######
#   To execute the program :                ######
#   Use Python IDLE or Jupyter Notebook     ######
#   Program made in Python 3.8.1            ######
#                                           ######
##################################################

def Religious_Places() :
    budget=int(input("Enter Your Budget For The Trip : "))
    if budget<1000:
        print("\nYour Budget Is Too Low For This Trip")
        print("Increase Your Budget At Least Upto 1000 Or Above")
        print("Try Again")
        main_loop()
    elif budget>=1000 and budget<2000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Konark Sun Temple,Orissa")
        print("2.Bodhgaya,Bihar")
        print("Enjoy Your Trip ")
    elif budget>=2000 and budget<4000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Haridwar,Uttarakhand")
        print("2. Varanasi,Uttar Pradesh")
        print("3. GoldenTemple,Punjab")
        print("Enjoy Your Trip ")
    elif budget>=4000 and budget<6000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Pushkar,Rajasthan")
        print("2. Rajrappa,Jharkhand")
        print("Enjoy Your Trip ")
    elif budget>=6000 and budget<8000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Vaidyanath Dham,Jharkhand")
        print("2. Kedarnath,UttaraKhand ")
        print("Enjoy Your Trip ")
    elif budget>=8000 and budget<10000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Rameshwaram,Tamil Nadu")
        print("2.Vaishno Devi,Jammu & Kashmir")
        print("Enjoy Your Trip ")
    else:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Shree Siddhivinayak Temple,Maharastra")
        print("2.Amarnath Cave,Jammu & Kashmir")
        print("Enjoy Your Trip ")

##################################################
        
def Hill_Stations():
    budget=int(input("Enter Your Budget For The Trip : "))
    if budget<2000:
        print("\nYour Budget Is Too Low For This Trip")
        print("Increase Your Budget At Least Upto 2000 Or Above")
        print("Try Again")
        main_loop()
    elif budget>=2000 and budget<5000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Parasnath Hill,Jharkhand")
        print("2. Dharamkot,Himachal Pradesh")
        print("Enjoy Your Trip ")
    elif budget>=5000 and budget<8000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Ooty,Tamil Nadu")
        print("2. Darjeeling,West Bengal")
        print("Enjoy Your Trip ")
    elif budget>=8000 and budget<11000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Netarhat,Jharkhand")
        print("2. Mussoorie,Uttarakhand")
        print("Enjoy Your Trip ")
    else:
        print("\nYou Can Visit Any Of The Following Places")
        print("1.Kullu,Himachal Pradesh")
        print("2.Leh Ladakh,Ladakh")
        print("3. Manali,Himachal Pradesh")
        print("Enjoy Your Trip ")

##################################################
        
def Historical_Places():
    budget=int(input("Enter Your Budget For The Trip : "))
    if budget<3000:
        print("\nYour Budget Is Too Low For This Trip")
        print("Increase Your Budget At Least Upto 3000 Or Above")
        print("Try Again")
        main_loop()
    elif budget>=3000 and budget<5500:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Taj Mahal,Uttar Pradesh")
        print("2. Qutub Minar,Delhi")
        print("Enjoy Your Trip ")
    elif budget>=5500 and budget<7000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Nalanda University,Bihar")
        print("2. Jallianwala Bagh,Punjab")
        print("Enjoy Your Trip ")
    elif budget>=7000 and budget<10000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Jaisalmer Fort, Rajasthan")
        print("2. Ajanta & Allora Caves,Maharastra")
        print("3. Jaipur,Rajasthan(The Pink City)")
        print("Enjoy Your Trip ")
    else:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Jodhpur,Rajsthan(The Blue City)")
        print("2. Chittorgarh,Rajasthan")
        print("Enjoy Your Trip ")

##################################################
        
def National_Parks():
    budget=int(input("Enter Your Budget For The Trip : "))
    if budget<3500:
        print("\nYour Budget Is Too Low For This Trip")
        print("Increase Your Budget At Least Upto 3500 Or Above")
        print("Try Again")
        main_loop()
    elif budget>=3500 and budget<6000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Bandipur National Park,Karnataka")
        print("2. National Zoological Park,Delhi")
        print("Enjoy Your Trip ")
    elif budget>=6000 and budget<9000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Van Vihar,Madhya Pradesh")
        print("2. Betla,Jharkhand")
        print("Enjoy Your Trip ")
    elif budget>=9000 and budget<11000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Sunderbans,West Bengal")
        print("2. Chandoli National Park,Maharastra")
        print("Enjoy Your Trip ")
    else:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Dachigam National Park,Jammu & Kashmir")
        print("2. Kaziranga National Park,Assam")
        print("Enjoy Your Trip ")

##################################################

def Wildlife_Sancturies():
    budget=int(input("Enter Your Budget For The Trip : "))
    if budget<3300:
        print("\nYour Budget Is Too Low For This Trip")
        print("Increase Your Budget At Least Upto 3300 Or Above")
        print("Try Again")
        main_loop()
    elif budget>=3300 and budget<6000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Krishna Wildlife Sanctuary,Andhra Pradesh")
        print("2. Gautam Buddha Wildlife Sanctuary,Bihar")
        print("Enjoy Your Trip ")
    elif budget>=6000 and budget<9000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Malabar Wildlife Sanctuary,Kerala")
        print("2. Manali Wildlife Sanctuary,Himachal Pradesh")
        print("Enjoy Your Trip ")
    elif budget>=9000 and budget<11000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Karakoram Wildlife Sanctuary,Ladakh")
        print("2. Dalma Wildlife Sanctuary,Jharkhand")
        print("Enjoy Your Trip ")
    else:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Gir Forest,Gujarat")
        print("2. Sita Mata Wildlife Sanctuary,Rajasthan")
        print("Enjoy Your Trip ")

##################################################

def Lakes():
    budget=int(input("Enter Your Budget For The Trip :"))
    if budget<3200:
        print("\nYour Budget Is Too Low For This Trip")
        print("Increase Your Budget At Least Upto 3200 Or Above")
        print("Try Again")
        main_loop()
    elif budget>=3200 and budget<6000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Kanwar Lake,Bihar")
        print("2. Vastrapur Lake,Gujarat")
        print("Enjoy Your Trip ")
    elif budget>=6000 and budget<9000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Blue Bird Lake,Haryana")
        print("2. Suraj Tal Lake,Himachal Pradesh")
        print("Enjoy Your Trip ")
    elif budget>=9000 and budget<11000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Chilika Lake,Orissa")
        print("2. Pushkar Sarovar,Rajasthan")
        print("Enjoy Your Trip ")
    else:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Dal Lake,Jammu & Kashmir")
        print("2. Pangong Tso,Ladakh")
        print("Enjoy Your Trip ")

##################################################

def Beaches():
    budget=int(input("Enter Your Budget For The Trip : "))
    if budget<3700:
        print("\nYour Budget Is Too Low For This Trip")
        print("Increase Your Budget At Least Upto 3700 Or Above")
        print("Try Again")
        main_loop()
    elif budget>=3700 and budget<6000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Juhu Beach,Maharastra")
        print("2. Colva Beach,Goa")
        print("Enjoy Your Trip ")
    elif budget>=6000 and budget<8000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Panambur Beach,Karnataka")
        print("2. Varkala Beach,Kerala")
        print("Enjoy Your Trip ")
    elif budget>=8000 and budget<10000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Digha Sea Beach,West Bengal")
        print("2. Puri Beach,Orissa")
        print("Enjoy Your Trip ")
    else:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Tenneti Park Beach,Andhra Pradesh")
        print("2. Pamban Beach,Tamil Nadu")
        print("Enjoy Your Trip ")

##################################################

def Haunted_Places():
    budget=int(input("Enter Your Budget For The Trip : "))
    if budget<2500:
        print("\nYour Budget Is Too Low For This Trip")
        print("Increase Your Budget At Least Upto 2500 Or Above")
        print("Try Again")
        main_loop()
    elif budget>=2500 and budget<5000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Dumas Beach,Gujarat")
        print("2. Agrasen Ki Bauli,New Delhi")
        print("Enjoy Your Trip ")
    elif budget>=5000 and budget<8000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Shaniwarwada,Pune")
        print("2.Kuldhara,Rajasthan")
        print("Enjoy Your Trip ")
    elif budget>=8000 and budget<10000:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Lambi Dehar Mines,Uttarakhand")
        print("2. National Library Of India,West Bengal")
        print("Enjoy Your Trip ")
    else:
        print("\nYou Can Visit Any Of The Following Places")
        print("1. Bangarh Fort,Rajasthan")
        print("2. Kuldhara,Rajasthan")
        print("Enjoy Your Trip ")

##################################################

def default():
    print("\n")
    print("Do you want to run the program again?")
    print("Press 0 for No")
    print("Press 1 for Yes")
    d=int(input(""))
    if d==0:
        print("Thank You for using our services")
        print("Have a Nice Day")
        exit
    elif d==1:
        main_loop()
    else:
        default()

##################################################

def main_loop():
    print("\n")
    print("*************************************************")
    print("*************************************************")
    print("******** Intelligent System For Tourists ********")
    print("*************************************************")
    print("*************************************************")
    print("\n")
    print("Press 1. For Religious Places")
    print("Press 2. For Hill Stations")
    print("Press 3. For Historical Places")
    print("Press 4. For National Parks")
    print("Press 5. For Wildlife Sanctuaries")
    print("Press 6. For Lakes")
    print("Press 7. For Beaches")
    print("Press 8. For Haunted Places")
    print("\n")
    c=int(input("Enter Your Choice : "))
    if c==1:
        Religious_Places()
    elif c==2:
        Hill_Stations()
    elif c==3:
        Historical_Places()
    elif c==4:
        National_Parks()
    elif c==5:
        Wildlife_Sancturies()
    elif c==6:
        Lakes()
    elif c==7:
        Beaches()
    elif c==8:
        Haunted_Places()
    else:
        print("Your Choice Is Not In The List Try Again")
        main_loop()
    default()

##################################################

main_loop()

##################################################
##                       End                    ##
##################################################
