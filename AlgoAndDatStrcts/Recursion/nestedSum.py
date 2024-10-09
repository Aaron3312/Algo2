
# nestedEvenSum Solution

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

obj3 = {}

def nestedEvenSum(obj, sum=0):
    print(obj)
    if obj == {}:
        return 0
    for i in obj:
        value = obj[i]
        if isinstance(value, dict):
            sum += nestedEvenSum(value)
            print(i)
        elif isinstance(value, int) and value % 2 == 0:
            sum += value
        # Verifica si no es una cadena antes de hacer algo
    return sum


print(nestedEvenSum(obj1))