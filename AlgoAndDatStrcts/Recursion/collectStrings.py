# collectStrings
# Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.



def collectStrings(obj):
    strings = []  # Lista para acumular las cadenas
    if obj == {} or obj == []:  # Verifica si es un diccionario o una lista vacía
        return strings  # Retorna una lista vacía
    
    for key, value in obj.items():  # Itera sobre las claves y valores del diccionario
        if isinstance(value, dict):  # Si el valor es un diccionario, llama recursivamente
            strings.extend(collectStrings(value))
        elif isinstance(value, list):  # Si el valor es una lista, itera sobre los elementos
            for item in value:
                strings.extend(collectStrings(item))
        elif isinstance(value, str):  # Si el valor es una cadena, agrégalo a la lista
            strings.append(value)
    
    return strings  # Retorna la lista de cadenas encontradas








obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
print(collectStrings(obj)) # ['foo', 'bar', 'baz']