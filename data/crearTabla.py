def crearTabla(tabla,nombre):
    archivoHTML=tabla.to_html()
    archivo=open(f"./tablas/{nombre}.html","W")
    archivo.write(archivoHTML)            
    archivo.close()
