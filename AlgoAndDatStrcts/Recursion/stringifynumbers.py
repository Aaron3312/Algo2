def stringifyNumbers(obj):
    if isinstance(obj, dict):
        return {key: stringifyNumbers(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [stringifyNumbers(item) for item in obj]
    elif isinstance(obj, bool):  # Maneja explícitamente los booleanos
        return obj  # Devuelve el booleano sin convertir
    elif isinstance(obj, (int, float)):
        return str(obj)
    else:
        return obj

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
print(stringifyNumbers(obj))
 
