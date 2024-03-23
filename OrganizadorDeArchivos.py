#Importacion de os para obtener informacion de las rutas y las carpetas que se obtienen
import os
#Shutil para hacer las acciones de mover las carpteas
import shutil

extensiones = {}
predeterminadas = "otros"
print("Bienvenido a el organizador de archivos \n")
while True:
    #Ruta donde se encuentra su carpeta
  
    try:
        base_directory = input("""
                         Introduzca el directorio donde se encuentra la carpeta que quiere organizar, Ejemplo: 
                         "\033[1m C:\mi_carpeta \033[0m" \n
                         """)
        if not base_directory.strip():
            #Lanza un value error si la ruta esta en blanco
            raise ValueError()
        
        file_name = input(f"Introduzca el nombre de la carpeta dentro de su directorio \033[1m {base_directory} \033[0m \n")
        os.listdir(os.path.join(base_directory,file_name))
        abs_file_name = os.path.join(base_directory,file_name)

   
    except FileNotFoundError:
        #La carpeta no se encontro en la ruta dada
        print(f"No se ha encontrado su carpeta \033[1m{file_name}\033[0m , en el directorio \033[1m{base_directory}\033[0m  por favor asegurarse de colocarla correctamente \n")
    except ValueError:
        print("Debe de colocar una ruta")
    except OSError:
        print(f"El nombre de archivo, el nombre de directorio o la sintaxis de la ruta no son correctos: {base_directory}, {file_name}")
    else:
        print(f"Perfecto la carpeta que vamos a organizar es: \033[1m{file_name}\033[0m  y su ruta es \033[1m{abs_file_name}\033[0m  \n")
        try:
            if len(os.listdir(abs_file_name)) == 0:
                raise ValueError()
        except ValueError:
            print(f"No hay archivos en la carpeta a orgarnizar en la carpeta actual {file_name}")
            
        else:
            while True:
                try:
                    extension = input("Introduzca la extension que desea orgarnizar Ejemplo: .png, escribir exit si no desea agregar mas extensiones \n ")
                    if  not "." in extension and not extension  == 'exit':
                        raise SyntaxError()
                    extensiones[extension] = extension.replace(".","")

                    if extension.lower() == 'exit':
                        try:
                            with os.scandir(abs_file_name) as archivos:
                                print(f"Los archivos organizados seran almacenados en sus respectivas carpetas en la ruta actual {abs_file_name} \n")

                                for archivo in archivos:
                                    ruta_archivo = os.path.abspath(archivo.path)
                                    if os.path.isfile(archivo):
                                        #El _ sirve para no tener que declarar un valor con nombre, y ext almacena la extesion que obtiene de ese archivo 
                                        _,ext = os.path.splitext(archivo.name)
                                        #Si encuentra la carpeta de la extension se ira a esa, sino se ira a predeterminadas
                                        name_file = extensiones.get(ext.lower(), predeterminadas)
                                        #Ruta de cada extension para cada archivo
                                        archivo_destino_ruta = os.path.join(abs_file_name,name_file)
                                        
                                        #Si no existe esa carpeta para esa extension en la ruta, se creara
                                        if not os.path.exists(archivo_destino_ruta):
                                            os.makedirs(archivo_destino_ruta)
                                    shutil.move(ruta_archivo, archivo_destino_ruta)
                                print(f"Ha finalizado la organizacion de los archivos de la ruta: {abs_file_name} \n")
                        except NameError:
                            
                            print(f"No se ha podido econtrar archivos con las extensiones indicadas {extensiones} en la ruta {abs_file_name}\n")
                            exit()
                    
                        
                except SyntaxError:
                    print("La extension colocada no es valida \n")