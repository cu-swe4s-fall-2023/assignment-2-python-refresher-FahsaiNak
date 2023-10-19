test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
cd ../../

run test_plot_hist python plot_hist.py --file_name test/functional/test.csv --country_1 "United States of America" --country_2 "China" --fire_column 5 --out_file test/functional/hist_5.png --title "CO2 emission from fire column 5" --x "CO2 emission" --y "Counts"
assert_equal test/functional/hist_5.png $( ls test/functional/hist_5.png )
assert_exit_code 0

run test_plot_hist_err python plot_hist.py --file_name test/functional/ttest.csv --country_1 "United States of America" --country_2 "China" --fire_column 5 --out_file hist_5.png --title "CO2 emission from fire column 5" --x "CO2 emission" --y "Counts"
assert_exit_code 1
