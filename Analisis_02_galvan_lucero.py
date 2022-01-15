import csv
import locale

locale.setlocale( locale.LC_ALL, '' )

with open("synergy_logistics_database.csv", "r") as archivo_csv:
  lector = csv.reader(archivo_csv)

  demanda = {}
  value = {}

  for linea in lector:
    if linea[9] == 'total_value':
      continue

    key = linea[2] + '-' + linea[3]
    if key in demanda:
      demanda[key] += 1
      value[key] += int(linea[9])
    else:
      demanda[key] = 0
      value[key] = int(linea[9])

  orden = sorted(demanda.items(), key=lambda x:x[1])

  print('Las 10 rutas con mas demanda:')
  for ruta in orden[-10:]:
    print(ruta[0], ruta[1], locale.currency(value[ruta[0]], grouping=True)) 

  print()
  print('Las 10 rutas con mayor valor:')
  orden = sorted(value.items(), key=lambda x:x[1])
  for ruta in orden[-10:]:
    print(ruta[0], demanda[ruta[0]], locale.currency(ruta[1], grouping=True)) 

with open("synergy_logistics_database.csv", "r") as archivo_csv:
  lector = csv.reader(archivo_csv)

  transporte = {}
  valorportransporte = {}

  for linea in lector:
    if linea[9] == 'total_value':
      continue

    key = linea[7]
    if key in transporte:
      transporte[key] += 1
      valorportransporte[key] += int(linea[9])
    else:
      transporte[key] = 0
      valorportransporte[key] = int(linea[9])

  print()
  
  print('Transporte y demanda:')
  for key in transporte:
    print(key, transporte[key])

  print()
  print('Transporte y valor:')
  for key in valorportransporte:
    print(key, locale.currency(valorportransporte[key], grouping=True))

with open("synergy_logistics_database.csv", "r") as archivo_csv:
  lector = csv.reader(archivo_csv)

  total_value_exp = 0
  total_value_imp = 0
  country_value_exp = {}
  country_value_imp = {}
  for linea in lector:
    if linea[9] == 'total_value':
      continue
   
    if linea[1] == 'Exports':
      total_value_exp += int(linea[9])
      if linea[2] in country_value_exp:
        country_value_exp[linea[2]] += int(linea[9])
      else:
        country_value_exp[linea[2]] = int(linea[9])
    else:
      total_value_imp += int(linea[9])
      if linea[2] in country_value_imp:
        country_value_imp[linea[2]] += int(linea[9])
      else:
        country_value_imp[linea[2]] = int(linea[9])

  sorted_exp = sorted(country_value_exp.items(), key=lambda x:int(x[1]), reverse=True)
  sorted_imp = sorted(country_value_imp.items(), key=lambda x:int(x[1]), reverse=True)

  accumulated_value_exp = 0
  print('Los paises que acumulan el 80% de valor en exportaciones son:')
  i = 0
  while accumulated_value_exp/total_value_exp < 0.8:
    current = sorted_exp[i]
    accumulated_value_exp += current[1]
    print(current[0], current[1])
    i += 1

  accumulated_value_imp = 0
  print()
  print('Los paises que acumulan el 80% de valor en importaciones son:')
  i = 0
  while accumulated_value_imp/total_value_imp < 0.8:
    current = sorted_imp[i]
    accumulated_value_imp += current[1]
    print(current[0], current[1])
    i += 1