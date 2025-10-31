import matplotlib.pyplot as plt
import numpy as np
import json
import os
import re  # Importamos la biblioteca de expresiones regulares para limpiar el JSON

# LECTURA Y EXTRACCIÓN DE DATOS DEL JSON 
nombre_archivo_json = "barrios_madrid_oct25_fixed.json"

try:
    # LIMPIAR el JSON (quitar comentarios)
    print(f"Abriendo y limpiando el archivo: {nombre_archivo_json}")
    with open(nombre_archivo_json, 'r', encoding='utf-8') as f:
        contenido_con_comentarios = f.read()
    
    # Usar RegEx para quitar comentarios 
    contenido_limpio = re.sub(r"//.*", "", contenido_con_comentarios)
    
    # Cargar el string limpio como JSON
    datos_leidos = json.loads(contenido_limpio)
    print(f"Archivo JSON limpiado y cargado con éxito. {len(datos_leidos)} barrios encontrados.")

    # Agrupar los datos por 'distrito'
    datos_por_distrito = {}
    
    for barrio in datos_leidos:
        distrito = barrio.get('distrito')
        precio = barrio.get('precioMedio')
        
        # Nos aseguramos de tener ambos datos para este barrio
        if distrito and precio is not None:
            if distrito not in datos_por_distrito:
                datos_por_distrito[distrito] = []
            
            # Añadimos el precio a la lista de su distrito
            datos_por_distrito[distrito].append(precio)
    
    if not datos_por_distrito:
        print("No se encontraron datos válidos de 'distrito' y 'precioMedio'.")
    else:
        # Preparar datos para Matplotlib
        
        # Obtenemos los nombres de las distritos
        etiquetas_distritos = list(datos_por_distrito.keys())
        
        # Obtenemos la lista de listas de precios
        datos_para_plot = list(datos_por_distrito.values())
        
        print(f"Datos agrupados para {len(etiquetas_distritos)} distritos.")

        # CREAR EL GRÁFICO 
        fig, ax = plt.subplots(figsize=(16, 8))

        # Creamos el gráfico de violín
        ax.violinplot(
            datos_para_plot,
            showmedians=True,  # Muestra la mediana
            showextrema=True   # Muestra máximos/mínimos
        )

        # AÑADIR TÍTULOS Y ETIQUETAS
        ax.set_title('Distribución del Precio Medio del Alquiler por Distrito')
        ax.set_ylabel('Precio Medio (€)')
        ax.set_xlabel('Distrito')
        
        # Asignamos las etiquetas correctas a cada violín
        ax.set_xticks(np.arange(1, len(etiquetas_distritos) + 1))
        
        # Añadimos las etiquetas de texto, rotadas 90 grados para que no se solapen
        ax.set_xticklabels(etiquetas_distritos, rotation=45)

        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Ajustamos el layout para que no se corten las etiquetas
        plt.tight_layout()

        # GUARDAR Y MOSTRAR EL GRÁFICO
        nombre_grafico = "violin_precio_por_distrito.png"
        plt.savefig(nombre_grafico)
        print(f"Gráfico guardado como: {nombre_grafico}")
        
except FileNotFoundError:
    print(f"\nError: No se pudo encontrar el archivo '{nombre_archivo_json}'.")
    print("Asegúrate de que el script tiene permisos para crear y leer archivos.")
except json.JSONDecodeError as e:
    print(f"\nError al decodificar el JSON (incluso después de limpiar): {e}")
    print("Puede que el archivo tenga otro error de formato.")
except KeyError as e:
    print(f"\nError: No se encontró la clave {e} en el archivo JSON.")
    print("Verifica que la estructura del JSON es la esperada.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")