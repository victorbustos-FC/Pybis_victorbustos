# *insertar código de la libreria*

class tools:
  # 1. fun para generar info
  def generar_df_ventas(fecha, bool_tabla):
    import pandas as pd
    import random as r
    import sqlite3 as sql
    # ============================================================================
    # PARTE I: GENERAR LA INFO/INSUMO
    # ============================================================================
    abcdario = [
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
      'U', 'V', 'W', 'X', 'Y', 'Z'
      ]

    papelerias = [
      'Xochimilco', 'Cuemanco', 'Coapa', 'Milpa Alta',
      'CU', 'Zócalo', 'Narvarte', 'Santa Fé', 'Polanco',
      'Centro'
      ]

    lineas = [
        'Cuadernos', 'Libretas', 'Lápices', 'Plumones', 'Borradores', 'Sacapuntas',
        'Laptops', 'Tablets', 'Mochilas', 'Bolsas', 'Cajas', 'Pegamento', 'Tijeras',
        'Monitores', 'Teclados', 'Mouse', 'Audífonos', 'Cables', 'Cargadores', 'Baterías',
        'Pc', 'Uniformes', 'Pinturas', 'Pinceles', 'Papel', 'Cartulinas'
        ]

    # =========================== Parte II ==========================
    # Definimos listas vacias que posteriormente iremos llenando
    # con los datos de cada venta mediante la funcion append()
    # y el bucle for

    fechas = []
    productos = []
    claves = []
    cantidades = []
    precios = []
    totales = []
    sucursales = []

    # ========================= Parte III ==========================
    # Repetimos un bucle for 1000 veces, donde en cada iteracion
    # o cada vuelta, agregamos un nuevo elemento a cada lista
    for i in range(1, r.randint(1000, 50000)):
      # Zona de definicion de variables
        producto = r.choice(lineas)
        clave = r.choice(abcdario) + r.choice(abcdario) + r.choice(abcdario) + '-' + str(r.randint(1, 9)) + str(r.randint(1, 9)) + str(r.randint(1, 9))
        cantidad = r.randint(1, 50)
        precio = round(r.randint(1, 10000) * r.random(), 2)
        total = round(precio * cantidad, 2)
        sucursal = r.choice(papelerias)

        # Agregamos los datos a las listas
        fechas.append(fecha)
        productos.append(producto)
        claves.append(clave)
        cantidades.append(cantidad)
        precios.append(precio)
        totales.append(total)
        sucursales.append(sucursal)

    # ========================= Parte IV ==========================
    # Definimos un diccionario donde las claves seran los nombres
    # de las columnas y los valores seran las listas que llenamos
    dict_pre_ventas = {
        # clave: valores asociados
        #      : listas
        "Fecha": fechas,
        "Producto": productos,
        "Clave": claves,
        "Cantidad": cantidades,
        "Precio": precios,
        "Total": totales,
        "Sucursal": sucursales
    }

    # ========================== Parte V ==========================
    # Creamos el dataframe con la funcion de pandas pd.DataFrame()
    df = pd.DataFrame(dict_pre_ventas)
    print(f"Información del {fecha} generada con éxito")

    # ============================================================================
    # PARTE II: SUBIR LA INFO-SQL
    # ============================================================================
    # connect: te crea la base de datos o se conecta si ya existe
    # 1. Conectarte a la base de datos
    conexion = sql.connect("Ventas.db")

    # Crearemos la tabla por primera vez
    if bool_tabla == True:
      # 2. .to_sql
      df.to_sql(name="Ventas_2025", if_exists="replace", con=conexion)
    # vamos a apilar dataframes
    else:
      df.to_sql(name="Ventas_2025", if_exists="append", con=conexion)

    # 3. Cerramos la conexion
    conexion.close()
    print(f"Información subida del {fecha} a la BBDD con éxito")

  # 2. fun init
  def inicializador(fecha):
    tools.generar_df_ventas(fecha, True)

  # 3. fun rango fechas
  # None -nada explicito-vacio explicito
  def rango_fechas(fecha1, fecha2=None):
    import pandas as pd

    # rango_fechas(fecha1) ---> por defecto fecha2 == None
    # =========================================================
    # Estamos en el caso en que solo queremos generar una fecha
    if fecha2 == None:
      tools.generar_df_ventas(fecha1, False)
    # =========================================================
    # fecha2 es diferente de None
    # El usuario si le pasouna fecha
    # rango_fechas("2025-08-01", "2025-08-31")
    else:
      # Generamos el resto de los dias
      rango_fechas = pd.date_range(start=fecha1, end=fecha2, freq="d")
      for fecha in rango_fechas:
        tools.generar_df_ventas(fecha, False)

  def consulta(sentencia_sql):
    import sqlite3 as sql
    import pandas as pd
    # 1. Conexion a la base de datos
    conexion = sql.connect("Ventas.db")

    # Realizamosla consulta SQL
    df_consulta = pd.read_sql_query(sentencia_sql, conexion)

    # Cerrar la conexion
    conexion.close()

    # ======================================================
    return df_consulta