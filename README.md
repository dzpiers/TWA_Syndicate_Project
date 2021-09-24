# TWA Syndicate Project
Syndicate project for text and web analysis. Syndicate 4, module 3.

## Data
In this folder we have all of the CSVs used for our assignment. The CSVs used in our analysis were the ones titled "XXXXs.csv", each between 700 and 1000 songs in length.  
For general word trends, these CSVs were used individually to collate by decade results.  
For the classifier, these CSVs were also used separately but in addition to this, a label was added when calling each one in to reflect the decade of music.  
For the LDA models, each model was constructed based off of one CSV.  
For the lyric similarity this was again done by decade using each CSV individually to get decade specific results.  
For the lyric complexity, this was done using all the CSVs combined into one dataset.  

However in a few cases we used the genre-specific datasets were mentioned, the files named "XXXXs_genre.csv" were used.  
For the wordclouds, lyric similarity and lyric complexity we combined the genre CSVs by genre to create three further datasets for our analysis, one for each genre.  

Each CSV contains the song name, artist name, album name, release date, length (in ms) and most importantly, the lyrics without any preprocessing. These datasets were created based off of Spotify playlists, curated by Spotify themselves as detailed in our essay. Essentially, Spotify has playlists by decade and the playlists titled "top hits of [year]" which were used to create the CSVs titled "XXXXs.csv". There are also top hits by genre for each year which were used to create our genre specific playlists althought these don't appear every year for every genre, only around the time the said genre started to become popular.  

This data was created via the code in the folder Lyric Scraping, detailed below.  

## Lyric Scraping
These files utilise the Spotify and Genius APIs. By specifying a Spotify playlist and user who created that playlist (by inputting their URIs), a list of ids for that playlist is created. From that list of ids (or multiple lists of ids), a dataset is created and then exported to a csv file. Instructions of how to use the code are in the comments. The files, getTrackData.py and getLyrics.py require the input of your API tokens and secrets (ours were removed for security reasons) and the file output.py can be used to create the data. Note that the URIs used for our assignment has been commented out. Feel free to use the code as you like on any Spotify playlist, the instructions should be reasonably clear.

## Classifier Results and classifier_code.iypnb
The classifier code reads in the popular music CSVs from the Data folder, applies pre-processing and stemming, then builds an unordered multinomial logit model based on it (also known as a multi-class logistic regression model). This uses various libraries, imported in the first cell. After the multinomial logit model was built, the parameters from the model are saved into a CSV file. There will be one parameter per class per word in the vocabulary, and these parameters are interrogated for insights. These CSV files are saved in the Results folder. To run the code, simply run all cells in order.

## LDA
This folder contains the results of our LDA models in HTML files, one for each decade. These are interactive files made with the help of pyLDAvis module as described in our report. Make sure to adjust the slider for lambda in the top right to get more interpretable results.

## Wordcloud
This folder contains the results of the wordclouds made with the module wordcloud as pngs.

## analysis.ipynb
This file contains the all of our analysis, except our classifier analysis. Each section of code is labelled with examples of how to use it.

## Note
This code has also been uploaded to [Dhruv's github](https://github.com/dzpiers/TWA_Syndicate_Project) (so please don't ping us for plagerising ourselves).