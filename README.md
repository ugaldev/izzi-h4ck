# IZZI-H4CK

Generador de diccionarios para redes wifi IZZI. Hasta el momento solo me ha funcionado en Modems Arris modelo TG2482A.

**Nota:** Recuerda que necesitas capturar el **_handshake_** de la red IZZI para poder hacer uso del diccionario por medio de fuerza bruta

## Importando izzi-h4ck
`$ git clone https://github.com/ugaldev/izzi-h4ck`

## Como usar
**Abre una terminal y ve al directorio izzi-h4ck**

`$ cd izzi-h4ck`

**Importa las librerias necesarias**

`$ pip3 install progress pandas wifi rich colorama netifaces`

**Ejecuta el programa**

`$ python3 izzi-h4ck.py`

**Menu de opciones**

```
┌─────────────────────────────────────────┐
│ [IZZI-H4CK - ugaldev]                   │
│                                         │
│ Creador de diccionarios para redes IZZI │
│                                         │
│ https://github.com/ugaldev/izzi-h4ck    │
│                                         │
└─────────────────────────────────────────┘
 
Nota: Este script es para fines educativos, no me hago responsable del mal uso
      que se le de a los diccionarios generados con este script


 Opciones:
 [1] Buscar redes vulnerables
 [2] Ingresar red manualmente
 
⎼⎼>Opcion:
```

**Opcion 1:** Busca redes vulnerables a este diccionario.

**Opcion 2:** Tienes que agregar el BSSID y SSID manualmente.



