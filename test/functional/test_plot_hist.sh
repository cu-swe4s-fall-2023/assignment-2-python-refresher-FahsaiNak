test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
cd ../../

run get_data_USA python get_data.py --file_name test/functional/test.csv --country "United States of America" --fire_column 5 --out_file test/functional/USA.txt
assert_equal test/functional/USA.txt $( ls test/functional/USA.txt )
assert_exit_code 0

run get_data_China python get_data.py --file_name test/functional/test.csv --country "China" --fire_column 5 --out_file test/functional/China.txt
assert_equal test/functional/China.txt $( ls test/functional/China.txt )
assert_exit_code 0

run get_data_filename_error python get_data.py --file_name ttest.csv --country "United States of America" --fire_column 5 --out_file USA.txt
assert_exit_code 1

run plot_hist python hist.py --data_file_1 test/functional/China.txt --data_file_2 test/functional/USA.txt --out_file test/functional/China-USA.png --title "CO2 emission from Crop Residues in China and USA" --x "CO2 emission" --y "Counts"
assert_equal test/functional/China-USA.png $( ls test/functional/China-USA.png )
assert_exit_code 0

run plot_hist_filename_error python hist.py --data_file_1 test/functional/Thailand.txt --data_file_2 test/functional/USA.txt --out_file test/functional/China-USA.png --title "CO2 emission from Crop Residues in China and USA" --x "CO2 emission" --y "Counts"
assert_exit_code 1
