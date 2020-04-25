# Tony_Win_Music_Scraping

![Tony Awards](sebastien-cordat-uJ97JHFKquM-unsplash.jpg)



## Goal ##

- Fully automate workflow from searching for an album, to seeing its stats in a dashboard


## Project Plan ##
1. Gathering album level and track level data on Tony winning albums
2. Compile above information into best aggregated data set
3. Put data in Tableau and analyze tracks over time
4. Put an application around the scripts so albums can be searched for and that dataset can be produced for research.
5. Add additional fields from IBDB *(5 and 6 may occur in reverse order depending on what is most important*)
6. Build that application out so there are embedded analytics and dashboards update automatically when datasets are produced


### Resources used ###

##### Spotify Web Development #####

If you need a refreshed on how Spotify structures its process of public data sharing, visit their [Developer page.](https://developer.spotify.com/documentation/) and check out how to retrieve album data from Spotify using their [Web API.](https://developer.spotify.com/documentation/web-api/reference/albums/get-albums-tracks/)

##### Packages #####
Developers have made it very easy to retrieve data from Spotify's Web APIs through the [Spotipy package.](https://github.com/plamere/spotipy)
