
from sklearn import datasets as Datasets;
import pandas as Pandas;
import matplotlib.pyplot as Matplotlib;

filePath = 'CSV Files\\avocado.csv';
avocadoData = Pandas.read_csv(filePath);



#print(avocadoData.info);
#print(avocadoData.head(100));
#print(avocadoData.tail(20));

#minPrice = avocadoData['AveragePrice'].min();
#maxPrice = avocadoData['AveragePrice'].max();
#avgPrice = avocadoData['AveragePrice'].mean();

#print(f'El precio minimo del conjunto de datos es: {minPrice}');
#print(f'El maximo precio del conjunto de datos es: {maxPrice}');
#print(f'El precio promedio del conjunto de datos es: {avgPrice}');

albany = avocadoData[avocadoData['region'] == 'Albany'];
westTexNewMexico = avocadoData[avocadoData['region'] == 'WestTexNewMexico'];

subplot = Matplotlib.subplot();

albanyGraphic = albany.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'blue', ax = subplot);

westTexNewMexicoGraphic = westTexNewMexico.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'red', ax = subplot);

Matplotlib.show();

