
from sklearn import datasets as Datasets;
import pandas as Pandas;
import matplotlib.pyplot as Matplotlib;

irisData = Datasets.load_iris(); #este metodo carga el dataset de iris completo, incluyendo la metadata que se encuentra en dicho dataset.

irisData = Pandas.DataFrame(Datasets.load_iris().data); #Aca lo que hicimos es que en vez de cargar el dataset de iris completo, lo que hicimos fue que lo agregamos como un objeto del tipo DataFrame. la propiedad data al final del metodo lo que indica es que del dataset de iris solo queremos obtener los valores o datos asociados con dicha propiedad, en este caso los datos asociados a la propiedad data.

#RECORDAR que en el dataset de iris se encuentran varias propiedades, incluyendo: data, target y target_names, etc, cada una de esas propiedades contiene los valores o atributos de todos los objetos de datos
print(type(irisData));

irisData = Pandas.DataFrame(Datasets.load_iris().data
                            ,columns = ['Sepal Length', 'Sepal Width'
                                        ,'Petal Length', 'Petal Width']);
#columns es un parametro, no una variable. Es un parametro que le podemos pasar a un determinado objeto. Aca lo valores agregados en el array son agregado en los parametros de columnas.

print(irisData);

print(irisData.to_string()); #Aca lo que ocurre es que antes de imprimirse el dataset convertimos la data que contiene la variable irisData a string, digase que hacemos una conversion de DataFrame a string. Al hacer lo ya mencionado anteriormente, se deja de impirmir un objeto del tipo DataFrame, y se imprimir un objeto del tipo string, por lo tanto se muestra el dataset completo, en vez de mostrarse de manera resumida.

#En pocas palabras al invocar el metodo to_string logramos visualizar el dataset completo.
print('\n');

irisPath = 'Iris Dataset\\iris.csv';
irisData = Pandas.read_csv(irisPath);
print(irisData.to_string());

print(irisData.shape); #este atributo lo que hace es que devuelve las formas o las dimensiones del dataset. En este caso el input seria: (150, 5)
#el 150 indica la cantidad de registros y el 5 indica la cantidad e columnas.

print(irisData.info); #este atribut retorna informacion general del dataset.

print(irisData.describe()); #este metodo retorna los estadisticos basicos y las principales medidas estadisticas del dataset

print(irisData['sepal_width'].describe()); #Aca se especifica que le queremos aplicar el metodo describe solamente al atributo sepal_width.

print(irisData.head()); #este metodo por defecto retorna los primeros 5 registros del dataset, esto signifca que si se le pasa un valor numerico como argumento, dicho valor indicaria la cantidad de registros a retornar.

print(irisData.tail()); #por defecto retorna los ultimos 5 registros del dataset. en el caso de que reciba un argumento, el argumento estaria indicando la cantidad de registros a retornar.

print(irisData.isna()); #retorna cuales registros contienen valores nulos. True si es nulo, False si no lo es.

print(irisData.isnull()); # lo mismo que isna() method

print(irisData.groupby('species').size()); #Aca se agruparon los datos del dataset apartir del atributo species y de esa agrupacion se retorna el tamaño de cada grupo.

print(irisData['species'].value_counts()); #este metodo cuenta la cantidad de valores de un determinado atributo (columna) dentro de un dataset.

fillNullValues = irisData.fillna('99'); #este metodo coloca 99 en todos aquellos valores que poseen valor nulo.

setosa = irisData[irisData['species'] == 'setosa']; #Aca lo que hicimos es que en vez de obtener todos los valores del dataset, estamos especificando que solo queremos obtener aquellos donde el atributo o columna species es igual a setosa. Osea del dataset solo estamos obteniendo aquellos valores donde el atributo species de dichos valores es igual a setosa
print(setosa);
vesicolor = irisData[irisData['species'] == 'versicolor'];
virginica = irisData[irisData['species'] == 'virginica'];

subplot = Matplotlib.subplot(); #se crea un subplot para combinar las 3 graficas en el mismo plano cartesiano.

setosaGraphic = setosa.plot(x = 'sepal_length', y = 'sepal_width', kind = 'scatter', color = 'red', ax = subplot); #de esta manera podemos crear una grafica en un plano cartesiano sobre el conjunto de datos. En este caso solo se toma en cuenta los valores que son iguales a setosa dentro del atributo species, y solo se avalua el sepal length y el sepal width.
# Matplotlib.show(); #haciendo uso de este metodo es que podemos general o ver el grafico.
vesicolorGraphic = vesicolor.plot(x = 'sepal_length', y = 'sepal_width', kind = 'scatter', color = 'orange', ax = subplot);
virginicaGraphic = virginica.plot(x = 'sepal_length', y = 'sepal_width', kind = 'scatter', color = 'green', ax = subplot);



Matplotlib.show();