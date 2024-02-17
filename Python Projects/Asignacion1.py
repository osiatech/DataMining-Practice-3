
import pandas as Pandas;
import matplotlib.pyplot as Matplotlib;

filePath = 'CSV Files\\netflix_titles.csv';
netflixTitlesData = Pandas.read_csv(filePath);

#print(netflixTitlesData);
#print(netflixTitlesData.head(10));
#print(netflixTitlesData.tail(15));
#print(netflixTitlesData.describe());
fillNullValues = netflixTitlesData.fillna('0');

#filteredData = netflixTitlesData[netflixTitlesData['release_year'] >= 2010 &(netflixTitlesData['release_year'] <= 2021)];

#Labels:
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'];


#**************************** Movies ****************************************

movies_2010 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2010)];

movies2010_Counted = movies_2010['release_year'].value_counts().iloc[0];

movies_2011 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2011)];

movies2011_Counted = movies_2011['release_year'].value_counts().iloc[0];

movies_2012 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2012)];

movies2012_Counted = movies_2012['release_year'].value_counts().iloc[0];

movies_2013 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2013)];

movies2013_Counted = movies_2013['release_year'].value_counts().iloc[0];

movies_2014 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2014)];

movies2014_Counted = movies_2014['release_year'].value_counts().iloc[0];

movies_2015 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2015)];

movies2015_Counted = movies_2015['release_year'].value_counts().iloc[0];

movies_2016 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2016)];

movies2016_Counted = movies_2016['release_year'].value_counts().iloc[0];

movies_2017 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2017)];

movies2017_Counted = movies_2017['release_year'].value_counts().iloc[0];

movies_2018 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2018)];

movies2018_Counted = movies_2018['release_year'].value_counts().iloc[0];

movies_2019 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2019)];

movies2019_Counted = movies_2019['release_year'].value_counts().iloc[0];

movies_2020 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2020)];

movies2020_Counted = movies_2020['release_year'].value_counts().iloc[0];

movies_2021 = netflixTitlesData[(netflixTitlesData['type'] == 'Movie') & (netflixTitlesData['release_year'] == 2021)];

movies2021_Counted = movies_2021['release_year'].value_counts();
movies2021_Counted = 0;

movies = [movies2010_Counted, movies2011_Counted, movies2012_Counted, movies2013_Counted, movies2014_Counted, movies2015_Counted, movies2016_Counted, movies2017_Counted, movies2018_Counted, movies2019_Counted, movies2020_Counted, movies2021_Counted];


#******************************* TV Shows ****************************************

tvShows_2010 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2010)];

tvShows2010_Counted = tvShows_2010['release_year'].value_counts().iloc[0];

tvShows_2011 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2011)];

tvShows2011_Counted = tvShows_2011['release_year'].value_counts().iloc[0];

tvShows_2012 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2012)];

tvShows2012_Counted = tvShows_2012['release_year'].value_counts().iloc[0];

tvShows_2013 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2013)];

tvShows2013_Counted = tvShows_2013['release_year'].value_counts().iloc[0];

tvShows_2014 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2014)];

tvShows2014_Counted = tvShows_2014['release_year'].value_counts().iloc[0];

tvShows_2015 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2015)];

tvShows2015_Counted = tvShows_2015['release_year'].value_counts().iloc[0];

tvShows_2016 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2016)];

tvShows2016_Counted = tvShows_2016['release_year'].value_counts().iloc[0];

tvShows_2017 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2017)];

tvShows2017_Counted = tvShows_2017['release_year'].value_counts().iloc[0];

tvShows_2018 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2018)];

tvShows2018_Counted = tvShows_2018['release_year'].value_counts().iloc[0];

tvShows_2019 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2019)];

tvShows2019_Counted = tvShows_2019['release_year'].value_counts().iloc[0];

tvShows_2020 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2020)];

tvShows2020_Counted = tvShows_2020['release_year'].value_counts().iloc[0];

tvShows_2021 = netflixTitlesData[(netflixTitlesData['type'] == 'TV Show') & (netflixTitlesData['release_year'] == 2021)];

tvShows2021_Counted = tvShows_2021['release_year'].value_counts();
tvShows2021_Counted = 0;

tvShows = [tvShows2010_Counted, tvShows2011_Counted, tvShows2012_Counted, tvShows2013_Counted, tvShows2014_Counted, tvShows2015_Counted, tvShows2016_Counted, tvShows2017_Counted, tvShows2018_Counted, tvShows2019_Counted, tvShows2020_Counted, tvShows2021_Counted];

#*******************************************************************

dataFrame = Pandas.DataFrame({'Movies': movies, 'TV Shows': tvShows}, index = years);

axis = dataFrame.plot.bar(rot = 10);

Matplotlib.title('Asignacion 3');

Matplotlib.show();


