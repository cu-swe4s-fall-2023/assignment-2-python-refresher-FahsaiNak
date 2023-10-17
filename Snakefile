COUNTRIES = ["United States of America", "China"]

rule all:
  input: 'hist.png'

rule load_data:
    output:
        'Agrofood_co2_emission.csv'
    shell:
        'wget -O Agrofood_co2_emission.csv "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr"'

rule get_data:
    input:
        'Agrofood_co2_emission.csv'
    output:
        expand('{country}.txt', country=COUNTRIES)
    run:
        for country in COUNTRIES:
            shell(f'python get_data.py --file_name "{{input}}" --country "{country}" --fire_column 5 --out_file "{country}".txt')

rule plot_hist:
    input:
        expand('{country}.txt', country=COUNTRIES)
    output:
        'hist.png'
    shell:
        'python hist.py --data_file_1 "{input[0]}" --data_file_2 "{input[1]}" --out_file {output} --title "CO2 emission from Crop Residues in China and USA" --x "CO2 emission" --y "Counts"'
