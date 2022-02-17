#asignamos el proyecto como un repositorio de git
git init

#creamos un ambiente virtualizado
py -m venv mi-espacio

#creamos archivo .gitignore para que omita los archivos del espacio virtualizado ya que ocupan mucho espacio

#Activamos el espacio virtualizado
mi-espacio/Scripts/activate

#instalar paquetes para hacer scrapping
py -m pip install requests lxml autopep8