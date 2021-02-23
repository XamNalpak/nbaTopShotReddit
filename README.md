# NBA Top Shot Reddit API
## Written and maintained by XamPak


This is a fully packaged ready to run script to pull data from the 'new' section of the Nba Top Shot reddit feed

# Use cases

I hope for this script to used in a fashion to help people better understand the market and what drives the prices of these cards along with their intrinsic value.

Obviously more data would be needed to answer this question but I believe this would be a good addition to any reasearch of NBA top shot and the rise of NFT's.

## Packages used
- pandas
- praw
- datetime/time

## Features

- pulls in data regarding nba top shot
    - sorts in the data to only pull in posts with same day as you run the code
    - drops duplicate posts from the same day keeping the most up to date entry
    - counts the number of entries before and after the pull

# Instructions
 You first must activate the virtual environment
 (for windows)
 
```sh
nts\Scripts\activate
```

> The program is designed for you to already have a
>  'nbatop.csv' file in the same directory as your
> script. Initially there will be an empty file
>  downloaded with this script from github.
> 
> 
> 

After activating your virtual environment you just go to your cmd and run
```sh
python main.py
```
You should then see output of the number of entries read, entries found and entries ended with.

## License

MIT
