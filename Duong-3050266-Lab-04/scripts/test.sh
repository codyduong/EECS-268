echo '\n\033[1mExercise 1 Tests\033[0m';
python3 -m unittest -v exercise1.tests.tests || python3 -m unittest -v ..exercise1.tests.tests
echo '\n\033[1mExercise 2 Tests\033[0m';
python3 -m unittest -v exercise2.tests.tests || python3 -m unittest -v ..exercise2.tests.tests;
echo '\n\033[1mExercise 3 Tests\033[0m';
python3 -m unittest -v exercise3.tests.tests || python3 -m unittest -v ..exercise3.tests.tests;