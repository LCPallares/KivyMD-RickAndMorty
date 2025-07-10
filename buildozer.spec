[app]

# (str) Título de tu aplicación.
title = RickMortyApp

# (str) Nombre del paquete (debe ser en minúsculas y sin espacios).
package.name = rickmortyapp

# (str) Dominio del paquete (usado para identificar tu app, puedes cambiarlo si tienes un dominio propio).
package.domain = org.lcpallares.rickmortyapp

# (str) Directorio raíz de tu código fuente, donde se encuentra main.py. '.' significa el directorio actual.
source.dir = .

# (list) Extensiones de archivos a incluir.
# Asegúrate de incluir todas las extensiones que uses: .py, .kv, imágenes, fuentes, bases de datos.
source.include_exts = py,png,jpg,kv,db,ttf,otf,svg,atlas

# (list) Lista de directorios a excluir.
# Es importante excluir directorios de desarrollo para reducir el tamaño del APK.
source.exclude_dirs = tests, bin, venv, drive, .git, .vscode, __pycache__, .kivy

# (str) Versión de la aplicación.
version = 0.1

# (list) Requisitos de la aplicación.
# Asegúrate de listar TODAS las librerías de Python que tu app utiliza.
# Hemos ajustado las versiones de Kivy y KivyMD para una mejor compatibilidad.
# 'sqlite3' no es necesario si usas el módulo estándar de Python.
# 'Werkzeug' se mantiene porque lo usas para hashing de contraseñas.
# Añadimos 'certifi' y 'idna' que 'requests' a veces necesita en Android.
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow==10.3.0,requests,certifi,idna,Werkzeug, markupsafe 

# (str) Archivo de presplash. Asegúrate de que exista en la ruta especificada.
presplash.filename = assets/images/icon.png

# (str) Archivo de ícono de la aplicación. Asegúrate de que exista en la ruta especificada.
icon.filename = assets/images/icon.png

# (list) Orientaciones de pantalla soportadas.
orientation = portrait

#
# Android specific
#

# (bool) Indica si la aplicación debe ser fullscreen (sin barra de estado).
fullscreen = 0

# (list) Permisos de Android.
# android.permission.INTERNET es esencial para tu app (API REST).
# android.permission.WRITE_EXTERNAL_STORAGE con maxSdkVersion=18 es para Android antiguos,
# para versiones modernas, el acceso al almacenamiento privado de la app no requiere permisos especiales.
# Si necesitas acceder a carpetas públicas (Galería, Descargas), la estrategia de permisos es más compleja
# y depende de la versión de Android (READ_MEDIA_IMAGES, etc., o MANAGE_EXTERNAL_STORAGE).
# Por ahora, nos enfocamos en lo esencial para evitar crasheos por permisos faltantes pero no necesarios.
android.permissions = android.permission.INTERNET

# (int) API de Android objetivo. Se recomienda usar una API reciente.
# API 31 es Android 12. Puedes probar con 33 (Android 13) si lo deseas, pero 31 es un buen punto de partida.
android.api = 35

# (int) API mínima de Android que tu APK/AAB soportará.
android.minapi = 21

# (int) Versión del SDK de Android a usar. Generalmente coincide con android.sdk = 20
android.sdk = 20

# (str) Versión del NDK de Android a usar.
android.ndk = 25b

# (int) API del NDK de Android a usar. Debe coincidir con android.minapi.
android.ndk_api = 21

# (bool) Si es True, Buildozer aceptará automáticamente las licencias del SDK.
android.accept_sdk_license = True

# (list) Arquitecturas de Android para las que se construirá la aplicación.
# arm64-v8a y armeabi-v7a cubren la mayoría de los dispositivos modernos.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Permite el respaldo automático de la aplicación (Android API >=23).
android.allow_backup = True



# --- Opciones de Python-for-Android (p4a) ---
# Estas opciones generalmente no necesitan ser modificadas a menos que tengas necesidades específicas.

# (str) Tipo de bootstrap para Android. sdl2 es el predeterminado y el más común para Kivy.
p4a.bootstrap = sdl2

# (str) Arguments adicionales a pasar a python-for-android.toolchain
# A veces útil para depuración o configuraciones avanzadas.
# p4a.extra_args = --debug # Puedes descomentar esto para más logs de p4a durante la construcción.

# --- iOS specific ---
# (Generalmente no se modifica si solo te enfocas en Android por ahora)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/ios-control/ios-deploy
ios.ios_deploy_branch = master
ios.codesign.allowed = false



[buildozer]

# (int) Nivel de log (0 = solo errores, 1 = info, 2 = depuración con salida de comandos).
# Recomiendo '2' para depurar, luego puedes bajarlo a '1' o '0'.
log_level = 2

# (int) Muestra advertencia si buildozer se ejecuta como root.
warn_on_root = 1

# --- Fin de la configuración buildozer.spec ---
