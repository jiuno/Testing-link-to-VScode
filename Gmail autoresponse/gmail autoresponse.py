import pyperclip
#Menu para ver los mails a generar
print(
"========================\n"
"Que mail queres generar?\n"
"========================\n"
"[1] Aysa Silvia\n"
"[2] Expensas Bazurco\n"
"[3] Expensas MDQ\n")

mail = int(input("Seleccionar opción: "))
if mail == 1:
    #Mail Aysa Silvia
    #Destinatario
    mail = "silium21@yahoo.com.ar"
    pyperclip.copy(mail)
    print(mail)
    input("Pega el mail y apreta enter para continuar")
    #Asunto
    Mes1= input("1 Mes del tramo: ")
    Mes2= input("2 Mes del tramo: ")
    a = str(input("Que tramo es? 1 o 2: " ))
    asunto  = "Factura y comprobante AySA Tramo " + str(a) + " de 2 " + str(Mes1) + " - " + str(Mes2)
    print(asunto)
    pyperclip.copy(asunto)
    #Cuerpo
    input("Anda a pegar el asunto y presiona enter para continuar")
    cuerpo1 =("Hola Silvia \n"
    "\n"
    "Te adjuntamos la factura de AySA y el comprobante de pago.\n"
    "\n"
    "Saludos!")
    print("\n"+ cuerpo1)
    pyperclip.copy(cuerpo1)
    print("\n"+
    "Pega el cuerpo y terminaste!")
elif mail == 2:
    #Mail expensas Bazurco
    #Destinatario
    import pyperclip
    mail2 = "pagoexpensas@admvaroca.com"
    pyperclip.copy(mail2)
    print(mail2)
    input("Pega el mail y apreta enter para continuar")
    #Asunto
    asunto  = "Maria A Cabril Unidad: 0008-1 D, Bazurco 2509/100"
    print(asunto)
    pyperclip.copy(asunto)
    input("Anda a pegar el asunto y presiona enter para continuar")
    #Cuerpo
    mes_bazurco = input("Mes del período: ")
    venc_bazurco = input("Vencimiento (dd/mm/aaaa): ")
    cuerpo2 =("Buenos días,\n"
    "\n"
    "Envío adjunto el comprobante del pago de Expensas correspondiente al periodo del mes de " + str(mes_bazurco) + " (Vencimiento "+ str(venc_bazurco)+")2 ""\n"
    "\n"
    "Saludos!")
    print("\n"+ cuerpo2)
    pyperclip.copy(cuerpo2)
    print("\n"+
    "Pega el cuerpo y terminaste!")
    
else:
    print("Aun estoy en desarrollo :(")


