for i in {00..36}
do
  echo $i
  python3 evacuation.py < tests/$i
  cat tests/$i.a
  echo 
done
