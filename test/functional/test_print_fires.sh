test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
cd ../../

run get_column_basic python print_fires.py --file_name test/functional/test.csv --country "United States of America" --fires_column 4
assert_in_stdout [1999,
assert_exit_code 0

run get_column_mean python print_fires.py --file_name test/functional/test.csv --country "United States of America" --fires_column 4 --operation mean
assert_in_stdout 1928.23
assert_exit_code 0

run get_column_mean python print_fires.py --file_name test/functional/test.csv --country "United States of America" --fires_column 4 --operation var
assert_exit_code 2

run get_column_median python print_fires.py --file_name test/functional/test.csv --country "United States of America" --fires_column 4 --operation median
assert_in_stdout 1558
assert_exit_code 0

run get_column_std python print_fires.py --file_name test/functional/test.csv --country "United States of America" --fires_column 4 --operation std
assert_in_stdout 1007.7
assert_exit_code 0

run get_column_filename_error python print_fires.py --file_name ttest.csv --country "United States of America" --fires_column 4
assert_exit_code 1

run get_column_nan python print_fires.py --file_name test/functional/test.csv --country "Bermuda" --fires_column 11
assert_in_stdout "No value"
