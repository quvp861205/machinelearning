import re

# la funcion la podemos definir en el notebook y usar directamente
def get_text(file):
  '''Read Text from file'''
  text = open(file).read()
  text = re.sub(r'<.*?>', ' ', text)
  text = re.sub(r'\s+', ' ', text)
  return text