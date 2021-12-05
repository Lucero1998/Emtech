
from lifeStore_SalesList import lifestore_searches, lifestore_sales, lifestore_products

"""
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

nombre_usuario= input("Ingresa tu nombre de usuario: ")
contra= input("Ingresa tu contraseña: ")
if nombre_usuario == "Admin" and  contra== "1234":
    print("Bienvenido")
    login = True
else:
    print("Usuario o contraseña incorecta") 
    login = False

if login:
  # Crea el diccionario de id -> producto
  productname=dict()
  for product in lifestore_products:
    productname [product[0]]= product[1]

  # Crea el reporte de ventas
  ventas = []
  for venta in lifestore_sales:
    ventas.append(venta[1])

  suma = dict()
  for id in ventas:
    if id in suma:
      suma[id] += 1
    else:
      suma[id] = 1

  suma_ordenada = sorted(suma.items(), key=lambda x:x[1])

  resultado = []
  for s in suma_ordenada[-5:]:
    resultado.append(s[0])

  print('Los 5 ID de los productos con mayores ventas son:', resultado)
  print()

  resultado1 = []
  for s in suma_ordenada[-5:]:
    resultado1.append(productname[s[0]])

  print('Los 5 productos con mayores ventas son: ')
  for r in resultado1:
    print('--', r)
  print()

  #Crea el reporte de busquedas
  busquedas = []
  for busqueda in lifestore_searches:
    busquedas.append(busqueda[1])
    
  suma2 = dict()
  for id in busquedas:
      if id in suma2:
        suma2[id] += 1
      else:
        suma2[id] = 1

  suma2_ordenada = sorted(suma2.items(), key=lambda x:x[1])

  resultado = []
  for s in suma2_ordenada[-10:]:
    resultado.append(s[0])

  print('Los 10 ID de los productos con mayores busquedas son:', resultado)
  print()

  resultado1 = []
  for s in suma2_ordenada[-10:]:
    resultado1.append(productname[s[0]])

  print('Los 10 productos con mayores busquedas son: ')
  for r in resultado1:
    print('--', r)

  categorias = dict()
  for product in lifestore_products:
    id_product = product[0]
    category  = product[3]
    if category in categorias:
      categorias[category].append(id_product)
    else:
      categorias[category] = [id_product]

  venta_por_categoria = dict()
  busquedas_por_categoria = dict()
  for category in categorias: 
    ids = categorias[category]
    ventas = []
    busquedas = []
    for id in ids:
      if id in suma:
        ventas.append([id, suma[id]])
      else:
        ventas.append([id, 0])
      if id in suma2:
        busquedas.append([id, suma2[id]])
      else:
        busquedas.append([id, 0])
    venta_por_categoria[category] = ventas
    busquedas_por_categoria[category] = busquedas

  for category in categorias:
    ventas = sorted(venta_por_categoria[category], key=lambda x:x[1])
    busquedas = sorted(busquedas_por_categoria[category], key=lambda x:x[1])
    print()
    print('Los 5 productos en la categoria de', category, 'con menores ventas son:')
    for v in ventas[:5]:
      print('Veces:', v[1],'ID:', v[0], 'Nombre:', productname[v[0]][:30])
    print('Los 10 productos en la categoria de', category, 'con menores busquedas son:')
    for b in busquedas[:10]:
      print('Veces:', b[1],'ID:', b[0], 'Nombre:', productname[b[0]][:30])

  #Crea listado productos mejores y peores resenias
  resenia = []
  for product in lifestore_sales:
    resenia.append ([product [1], product [2]])

  id_resenia = dict()
  for r in resenia:
    if r[0] in id_resenia:
      id_resenia[ r[0]].append(r[1])
    else:
      id_resenia[r[0]] = [r[1]]


  nuevo_id_resenia=[]
  for id in id_resenia:
    lista_completa = id_resenia[id]
    suma_resenia=0
    cuenta = 0
    for v in lista_completa:
      suma_resenia += v
      cuenta += 1
    nuevo_id_resenia.append([id, suma_resenia/cuenta])
    
  nuevo_id_resenia = sorted(nuevo_id_resenia, key = lambda x:x[1])

  print()
  print("Estos son los productos con peores resenias")
  for id in nuevo_id_resenia[:5]:
    print ("ID:", id[0], "Calificacion:", id[1] )

  print()
  print("Estos son los productos con mejores resenias")
  for id in nuevo_id_resenia[-5:]:
    print ("ID:", id[0], "Calificacion:", id[1] )

  #crear total de ingresos y ventas promedio mensual, total anual y meses con mas ventas al anio

  venta_mensual= dict()
  for info in lifestore_sales:
    fecha = info[3][-7:]
    if fecha in venta_mensual:
      venta_mensual[fecha].append(info[1])
    else:
      venta_mensual[fecha] = [info[1]]

  id_to_precio=dict()
  for producto in lifestore_products:
    id_to_precio[producto[0]]=producto[2]

  total_mes=dict()
  for mes_key in venta_mensual:
    id_ventas_mes_list = venta_mensual[mes_key]
    precios = []
    for id in id_ventas_mes_list:
      precios.append(id_to_precio[id])
    
    suma = 0
    for precio in precios:
      suma += precio

    total_mes[mes_key] = suma
    
  ingresos_ordenados = sorted(total_mes.items(), key=lambda x:x[0])

  print()
  print("Total de ingresos mensuales:")
  for mes in ingresos_ordenados:
    print(mes[0]+':', mes[1])

  ingreso_total = 0
  cuenta = 0
  for mes in total_mes:
    ingreso_total += total_mes[mes]
    cuenta += 1

  print()
  print("Promedio de ingreso mensuales:", ingreso_total/cuenta)

  ingreso_anual =  dict()
  for mes_key in total_mes:
    anio = mes_key[-4:]
    if anio in ingreso_anual:
      ingreso_anual[anio] += total_mes[mes_key]
    else:
      ingreso_anual[anio] = total_mes[mes_key]


  anual_sorted = sorted(ingreso_anual.items(), key= lambda x:x[0])
  print()
  print("Los ingresos anuales son:")
  for anio in anual_sorted:
    print(anio[0]+':', anio[1])


  ingresos_ordenados = sorted(total_mes.items(), key=lambda x:x[1])
  print()
  print("Los meses con mas ventas al año son:")
  for mes in ingresos_ordenados[-3:]:
    print(mes[0]+":", mes[1])