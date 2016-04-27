rm errors.txt
rm log.txt
rm traceback.txt

rm -rf tmp/
rm -rf game/cache/

find . -name "*.rpyc" -exec rm -rf {} \;