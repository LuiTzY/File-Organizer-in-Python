import os
import shutil
from concurrent.futures import ThreadPoolExecutor

extensiones = {
    '.jpg': 'Imagenes',
    '.jpeg': 'Imagenes',
    '.png': 'Imagenes',
    '.mp4': 'videos',
    '.mp3': 'videos',
    '.mov': 'videos',
    '.mkv': 'videos',
    '.webm': 'videos',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.py': 'python'
}
predeterminadas = 'otros'
archivos_recuperados = "D:\\Seagate_archivos\\"
def organizar_archivos(carpeta_index):
    ruta_absoluta = os.path.abspath(f"D:/recup_dir.{carpeta_index}")
    with os.scandir(ruta_absoluta) as archivos:
        for archivo in archivos:
            print(f"Se ha inciado a organizar los archivos de la carpeta: {ruta_absoluta} \n")
            ruta_archivo = os.path.abspath(archivo.path)

            if os.path.isfile(ruta_archivo):
                _, extension = os.path.splitext(archivo.name)
                nombre_carpeta = extensiones.get(extension.lower(), predeterminadas)
                archivo_destino_ruta = os.path.join(archivos_recuperados, nombre_carpeta)

                if not os.path.exists(archivo_destino_ruta):
                    os.makedirs(archivo_destino_ruta)

                destino_archivo = os.path.join(archivo_destino_ruta, archivo.name)
                if os.path.exists(destino_archivo):
                    c = 1
                    nuevo_nombre = f'archivo_renombrado{c}{extension}'
                    while os.path.exists(os.path.join(archivo_destino_ruta, nuevo_nombre)):
                        c += 1
                        nuevo_nombre = f'archivo_renombrado{c}{extension}'
                    destino_archivo = os.path.join(archivo_destino_ruta, nuevo_nombre)

                shutil.move(ruta_archivo, destino_archivo)
                shutil.rmtree(ruta_absoluta)
                print(f"Se han movido con exito los archivos de la carpeta {ruta_absoluta}: Eliminando carpeta {ruta_absoluta}\n")

                
with ThreadPoolExecutor(max_workers=8) as executor:
    executor.map(organizar_archivos, range(1, 1101))

