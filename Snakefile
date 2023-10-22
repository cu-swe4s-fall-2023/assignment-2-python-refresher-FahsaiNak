COUNTRIES = ["United States of America", "China"]
FRIES = [4, 5, 6]

rule all:
  input: expand('hist_{fire}.png', fire=FRIES)

rule load_data:
    output:
        'Agrofood_co2_emission.csv'
    shell:
        'wget -O {output} "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr"'

rule plot_hist:
    input:
        'Agrofood_co2_emission.csv'
    output:
        expand('hist_{fire}.png', fire=FRIES)
    run:
        for fire in FRIES:
            shell(f'python plot_hist.py --file_name {{input}} --country_1 "{COUNTRIES[0]}" --country_2 "{COUNTRIES[1]}" --fire_column {fire} --out_file hist_{fire}.png --title "CO2 emission from fire column {fire}" --x "CO2 emission" --y "Counts"')
