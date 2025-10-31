import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re

# --- DATASET ---
# https://www.kaggle.com/datasets/michelhatab/hotel-reviews-bookingcom

# --- CONFIGURACIÓN ---
nombre_archivo_csv = 'booking_reviews.csv'
nombre_columna_texto = 'review_title'
limite_filas = 50000
# ---------------------


try:
    # Cargar el archivo CSV en un DataFrame de pandas
    df = pd.read_csv(nombre_archivo_csv, low_memory=False)

    # Comprobar si la columna existe
    if nombre_columna_texto not in df.columns:
        print(f"Error: La columna '{nombre_columna_texto}' no se encontró en el CSV.")
        print(f"Columnas disponibles: {list(df.columns)}")
    else:
        text_completo = " ".join(str(item) for item in df[nombre_columna_texto].dropna())        
        #text_completo = " ".join(str(item) for item in df[nombre_columna_texto].head(limite_filas).dropna())
        text = text_completo.lower()
        
        # Eliminamos puntuación y números (dejamos solo letras y espacios)
        texto_limpio = re.sub(r'[^a-z\s]', '', text)

        if not text.strip():
            print("La columna está vacía o solo contiene valores nulos. No se puede generar la nube de palabras.")
        else:
            # Crear el objeto wordcloud
            wordcloud = WordCloud(width=800, height=800, background_color="white", collocations=False, min_font_size=10).generate(texto_limpio)

            # Mostrar la imagen generada:
            # Ajustamos el tamaño de la figura para que se vea mejor
            plt.figure(figsize=(10, 10)) 
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.margins(x=0, y=0)
            
            # Guardar la imagen en un archivo PNG
            nombre_archivo_salida = "wordcloud_booking.png"
            plt.savefig(nombre_archivo_salida, bbox_inches='tight', pad_inches=0)
            print(f"La nube de palabras se ha guardado como '{nombre_archivo_salida}'")
            
            plt.show()

except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{nombre_archivo_csv}'.")
    print("Asegúrate de que el archivo esté en la misma carpeta que el script o proporciona la ruta completa.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")