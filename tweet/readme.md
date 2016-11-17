# Description

This will post a quote on twitter

# Usage

Get all the dependencies

    git clone git@github.com:infinite-Joy/bots.git
    cd bots/tweet
    git clone git@github.com:codebox/bayesian-classifier.git

the bot depends on both python2 and python3

    virtualenv venv35 -p python3.5
    cd bots/tweet

    source venv35/bin/activate
    pip install -r requirements.txt
    deactivate

    cd ../..
    virtualenv venv27 -p python2.7
    cd bots/tweet

    source venv27/bin/activate
    pip install -r requirements.txt
    deactivate

Set the twitter auth ids into a keys.yaml file. Yaml file in the following format
    
    data:
        consumer_key: ""
        consumer_secret: ""
        access_token_key: ""
        access_token_secret: ""

Then run the bash script

    ./tweet.sh


# Explanation

Right now how it works is that:

1. it pulls a quote using the AntJan api
2. gives an index to the quote to check if its programming type or not based bayes theorem. The model has been trained on a set of programming and non programming quotes. The training set is very small (about 38) and so what I doing is that if the index is more than 20 than I am saying that the quote is good which is not at all reliable.
3. Check if the index is more than 20 tweet it.

    
