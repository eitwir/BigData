rm -r -f "result"

python get-movies.py "$@"

cat result/*


