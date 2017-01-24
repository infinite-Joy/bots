cd bots
source venvpy35/bin/activate
cd tweet

python get_quotes.py > programming_quote.txt

echo "tweet procured"

cat programming_quote.txt
quote=$(cat programming_quote.txt)

cd ../..

cd bayesian-classifier

deactivate

python bayes.py classify ../bots/tweet/programming_quote.txt programming non_programming > programming_index.txt

echo "classification done"

cat programming_index.txt
index=$(cat programming_index.txt | grep -o '[0-9][0-9]')

echo "index is ${index}"

cd ..

if [ "${index}" -gt 20 ]; then
	cd bots
	source venvpy35/bin/activate
	cd tweet
	python tweet.py "${quote}"

fi
