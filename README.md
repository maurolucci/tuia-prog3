# TP-Programacion-III
### Instrucciones para la primera parte (**SIN CONDA**)
1. Abrir la carpeta `tp-pathfinding` con VSCode
2. Instalar con la terminal (si no lo tenes) el paquete para entornos virtuales `pip install virtualenv`
3. Crear un entorno virtual con `python -m venv ./.venv`
4. Ejecutar a traves en la consola `source ./.venv/Scripts/activate`
5. Instalar las dependencias en el venv: `pip install -r ./requirements.txt`
6. Ejecutar el juego con `python run.pyw`
7. Para salir del entorno escribir en la consola `deactivate`
8. Agregar

### Instrucciones para la primera parte (**CON CONDA (creo)**)
#### Creación Entorno Virtual:

Ejecutamos los siguientes comandos en orden:
1. `cd .\tuia-prog3\tp-pathfinding\` — Cambia al directorio del proyecto.
2. `python -m venv ./.venv` — Crea un entorno virtual en la carpeta `.venv`. El punto (`.`) al inicio de la carpeta `.venv` la convierte en una carpeta oculta**.**
3. `Set-ExecutionPolicy Unrestricted -Scope CurrentUser` — Permite ejecutar scripts en PowerShell cambiando la política de ejecución. Sin este comando no es posible activar el entorno. Si no se ejecuta este comando, no será posible ejecutar el siguiente.
4. `.\.venv\Scripts\Activate` — Activa el entorno virtual. Para confirmar que se ha activado correctamente, debe aparecer `(.venv)` al inicio de la línea de comandos en la terminal. Para desactivar el entorno virtual ejecuta el comando `deactivate` para confirmar esto debe desaparecer `(.venv)` al inicio de la línea de comandos.
5. `pip install -r .\requirements.txt` — Instala las dependencias listadas en el archivo `requirements.txt`.
6. Ahora sí, estamos listos para ejecutar el programa principal.