def mensaje():
    mensaje = """
    ---------------------------------------------
             (0 0) 
      ---oOO- (_) ----oOO---    
   ╔═════════════════════════╗ 
       Mediremos tu IMC
   ╚═════════════════════════╝ 
       -------------------
            |__|__| 
             || || 
            ooO Ooo 
    ---------------------------------------------
    """
    print(mensaje)

  
def calcularIMC(peso_en_libras,altura_en_metros):
    peso_en_libras = float(peso_en_libras)
    altura_en_metros = float(altura_en_metros )
    peso_en_kg =  0.45*peso_en_libras;
    IMC = peso_en_kg/(altura_en_metros*altura_en_metros)
    return IMC

def informe(elIMC):
    if elIMC < 18.5:
        print('Bajo peso')
        print('Comer bastantes proteinas en especial pechuga de pollo y salmon-atun')
        print('Ingerir carbohidratos como panes integrales, el arroz y las pastas')
        print('Consumir varias grasas buenas como el aguacate, lacteos y frutos secos')
        print('Recomendable poder hacer un superhabit calorico')
		
    elif elIMC > 18.5 and elIMC < 24.9:
        print("""
        -------------------------------------
        Peso normal ☜(⌒▽⌒)☞
        -------------------------------------
        """)
        print('Consumir las misma cantidad de calorias')
        print('Comer mas proteinas como carnes')
        print('Moderar los carbohidratos como la pasta')
        print('Y si quires poder hacer un deficit calorico')
		
    elif elIMC > 25 and elIMC < 29.9:
        print("""
        -------------------------------------
        Sobrepeso (´･_･`)
        -------------------------------------
        """)
        print('Consumir cierto porcentaje de proteinas como pechuga de pollo')
        print('Tener una injesta baja en carbohidratos como el pan y el arroz')
        print('Consumir grasas buenas como yogurt griego')
        print('Hacer un deficit calorico moderado')
		
    elif elIMC >= 30 :
        print("""
        -------------------------------------
        Obesidad ಥ﹏ಥ
        -------------------------------------
        """)
        print('Seleccionar varias unidades de carnes megras en general')
        print('No consumir carbohidratos o bajarles cieto grado')
        print('Grasas tratar de que sean de lacteos desnatados y comerlos moderadamente')
        print('Hacer un deficit calorico mas elevado')


      
#LÓGICA DEL PROGRAMA
mensaje()

peso = input('Tu peso en lb: ') 
altura = input('Tu altura en mt: ')

elIMC = calcularIMC(peso, altura)

informe(elIMC)