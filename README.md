# Proyecto Urban Grocers

*SPRINT 7 -- JORGE ALEJANDRO MACARIO COLÍN*

Este es un proyecto de automatización de pruebas API, escrito en Python y creado en PyChram. Para correr las pruebas es necesario instalar los paquetes "request" y "pytest".

*PASOS A SEGUIR:*

1. Abra el proyecto "qa-project-Urban-Grocers-app-es" en PyCharm.
2. Asegúrese de que los paquetes "request" y "pytest" estén descargados y actualizados. De no estar instalados o actualizados, descargue y actualize los 2 paquetes. 
3. Seleccione el archivo "configuration.py" para actualizar la URL por la de un servidor nuevo. 
4. Seleccione el archivo "create_kit_name_kit_test.py" y asegúrese de seleccionar la opción "Current File" en la pestaña superior.
5. Para correr las pruebas abra la terminal y utilice: "pytest create_kit_name_kit_test.py", o haga clic en el botón "Play" junto a "Current File"

*LISTA DE COMPROBACIÓN PARA LA AUTOMATIZACIÓN DE PRUEBAS:*

| № | Descripción                                                      | `kit_body`                                                                | Resultado Esperado (ER)                                                            |
| - | ---------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1 | El número permitido de caracteres (1)                            | `{ "name": "a" }`                                                         | Código de respuesta: 201. `"name"` en la respuesta coincide con el de la solicitud |
| 2 | El número permitido de caracteres (511)                          | `{ "name": "El valor de prueba para esta comprobación será inferior a" }` | Código de respuesta: 201. `"name"` en la respuesta coincide con el de la solicitud |
| 3 | El número de caracteres es menor que la cantidad permitida (0)   | `{ "name": "" }`                                                          | Código de respuesta: 400                                                           |
| 4 | El número de caracteres es mayor que la cantidad permitida (512) | `{ "name": "El valor de prueba para esta comprobación será inferior a” }` | Código de respuesta: 400                                                           |
| 5 | Se permiten caracteres especiales                                | `{ "name": "№%@," }`                                                      | Código de respuesta: 201. `"name"` en la respuesta coincide con el de la solicitud |
| 6 | Se permiten espacios                                             | `{ "name": " A Aaa " }`                                                   | Código de respuesta: 201. `"name"` en la respuesta coincide con el de la solicitud |
| 7 | Se permiten números                                              | `{ "name": "123" }`                                                       | Código de respuesta: 201. `"name"` en la respuesta coincide con el de la solicitud |
| 8 | El parámetro no se pasa en la solicitud                          | `{ }`                                                                     | Código de respuesta: 400                                                           |
| 9 | Se ha pasado un tipo de parámetro diferente (número)             | `{ "name": 123 }`                                                         | Código de respuesta: 400                                                           |



