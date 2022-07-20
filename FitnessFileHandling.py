
clients=[]
i=0

c=None
while(c!='0'):
    print("\n")
    print("===Welcome to EBR Fitness Club===")
    print("Options:\n",
          "[1]Add a member\n",
          "[2]View a member record\n",
          "[3]View all members\n",
          "[4]Delete a member record\n",
          "[5]Delete all member records\n",
          "[6]Save to file\n",
          "[7]Load from file\n",
          "[0]Exit")                      
    c=input("Choice: ")
    if(c=='1'):
        def inc():                 
            global i
            if(i==0):
                i=1
            else:
                i+=1
            return "M"+str(i).zfill(3)
        client=dict()              
        client_id=inc()            
        client_name=input("Enter name: ")
        client_weight=int(input("Enter weight(kg): "))
        client_height=int(input("Enter height(cm): "))
        client_bmi=round(client_weight/(client_height/100) ** 2, 1)
        s=["Underweight", "Normal", "Overweight", "Obese"]
        if(client_bmi<18.5):
            client_status=s[0]
        elif(18.5<=client_bmi<=24.9):
            client_status=s[1]
        elif(25<=client_bmi<=29.9):
            client_status=s[2]
        elif(client_bmi>=30):
            client_status=s[3]
        print("BMI is", client_bmi)
        print("Type is "+client_status)                                     
        client['id']=client_id                   
        client['name']=client_name
        client['weight']=client_weight
        client['height']=client_height
        client['bmi']=client_bmi
        client['status']=client_status
        clients.append(client)
    elif(c=='2'):                   
        temp_product_id=input("Enter product id: ")
        product_id=temp_product_id.upper()
        for s in range(0, len(clients)):
            if(product_id==clients[s]['id']):
                print("===Member Information===")
                print("(",clients[s]['id'],")", clients[s]['name'], clients[s]['weight'],
                      "kg", clients[s]['height'], "cm", "(BMI:", clients[s]['bmi'],"; ",
                      clients[s]['status'], ")")            #output the selected record
                break
        print("No Record... Please try again")
    elif(c=='3'):                   
        if len(clients) == 0:
            print("No Record... Add member first or load from a file")
        else:
            print("===List of members===")
            for s in range(0, len(clients)):
                print("("+clients[s]['id']+")", clients[s]['name'], str(clients[s]['weight']),
                      "kg", str(clients[s]['height']), "cm", "(BMI:", str(clients[s]['bmi']),"; "+
                      clients[s]['status']+ ")")
    elif(c=='4'):                   
        temp_product_id=input("Enter product id: ")
        product_id=temp_product_id.upper()
        for s in range(0, len(clients)):
            if(product_id==clients[s]['id']):
                print("===Member Deleted===")
                print("(",clients[s]['id'],")", clients[s]['name'], clients[s]['weight'],
                      "kg", clients[s]['height'], "cm", "(BMI:", clients[s]['bmi'],"; ",
                      clients[s]['status'], ")")
                clients.pop(s)
                break
        print("No Record... Add member first or load from a file")
    elif(c=='5'):                   
        if len(clients) == 0:
            print("No Record... Add member first or load from a file")
        else:
            clients.clear()
            print("===All Members Deleted===")
    elif(c=='6'):                   
        if len(clients) == 0:
            print("No Record... Add member first or load from a file")
        else:   
            save = open("VibarFile.txt",'w')
            for s in range(0, len(clients)):
                save.write(clients[s]['id']+"<#>"+clients[s]['name']+"<#>"+str(clients[s]['weight'])+
                           "<#>"+str(clients[s]['height'])+"<#>"+str(clients[s]['bmi'])+
                           "<#>"+clients[s]['status']+"\n")
            save.close()
            print("Successfully saved to file "+ "(" + str(len(clients)) + " entries)")
    elif(c=='7'):                   
        clients.clear()
        file = open("VibarFile.txt", "r")
        load = file.readlines()
        for p in load:
            client=dict()
            word = p.rstrip('\n').split("<#>")
            client['id']=word[0]
            client['name']=word[1]
            client['weight']=word[2]
            client['height']=word[3]
            client['bmi']=word[4]
            client['status']=word[5]
            clients.append(client)
        file.close()
        
        if len(clients) == 0:
            print("No Record from a file")
        else:
            print("Successfully load from file "+ "(" + str(len(clients)) + " entries)")
    elif(c=='0'):                   
        print("Thank you for using this program!")
    else:                           
        print("Please input a right option...")



