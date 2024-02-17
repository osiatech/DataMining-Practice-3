
import pandas as Pandas;
import matplotlib.pyplot as Matplotlib;

wins = [98, 92, 115, 102, 120];
loses = [55, 74, 88, 65, 87];
teams = ['New York Yankees', 'Chicago Cubs', 'Texas Rangers', 'Astros Houston', 'Dodgers Angeles'];

dataFrame = Pandas.DataFrame({'Wins': wins, 'Loses': loses}, index = teams);

axis = dataFrame.plot.bar(rot = 10); #Aca se ejecuta el metodo plot en el atributo bar.
#rot es un atributo el cual rota los labels, en este caso los nombres de los equipos.
#tambien podemos utilizar el atributo stacked = True, el cual coloca las dos barras en una sola, osea en este caso tenemos una barra que indica las wins y otra que indica las loses, entonces usando el atributo stacked, las loses aparecerian en la misma bar que las wins, aparecerian arriba.

#tambien podemos utilizar el atributo subplots = True para dividir el grafico en varias partes, en nuestro caso el grafico se estaria diviendo en dos, uno que indicaria las wins y otro que indicaria las loses.

Matplotlib.show();

