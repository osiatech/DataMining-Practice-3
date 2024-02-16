
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