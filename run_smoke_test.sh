#!/bin/bash

# Generate test data
printf "Idiot/Fyodor Dostoyevsky/9780850670356/1971\nMoby Dick/Herman Melville/9781974305032/1981\n" > generated_data.txt

echo "EXECUTING BOOKMASTER SMOKE TEST"

# Execute happy path smoke test
python bookmaster.py generated_data.txt << EOF
1
2
Test1/Test User1/12345/1960
Y
2
Test2/Test User2/55555/1975
Y
2
Last Test/Yet Another Author/56789/1985
Y
1
Q
EOF

EXPECTED_OUTPUT=$(printf "Test1/Test User1/12345/1960\nIdiot/Fyodor Dostoyevsky/9780850670356/1971\nTest2/Test User2/55555/1975\nMoby Dick/Herman Melville/9781974305032/1981\nLast Test/Yet Another Author/56789/1985")
ACTUAL_OUTPUT=$(cat generated_data.txt | tr -d '\r')

# Output file for manual inspection
echo "OUTPUT FILE:"
echo "$ACTUAL_OUTPUT"

echo "TEST RESULT:"
# Check and report result
if [ "$EXPECTED_OUTPUT" == "$ACTUAL_OUTPUT" ]; then
    echo "***** Smoke test - PASS *****"
else
    echo "***** Smoke test - FAIL *****"
    echo "Result file did not match expected result:"
    echo "$EXPECTED_OUTPUT"
fi

echo "SMOKE TEST END"