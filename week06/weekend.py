"""
Life Expectancy Data Analyzer

This program analyzes life expectancy data from OurWorldInData.org.
Additional features:
1. Allows user to input a country and see its min, max, and average life expectancy
2. Calculates the largest life expectancy drop for any country between consecutive years
"""

def main():
    min_life = float('inf')
    max_life = float('-inf')
    min_country = ""
    min_year = ""
    max_country = ""
    max_year = ""
    
    year_data = {}
    
    country_data = {}
    
    largest_drop = 0
    drop_country = ""
    drop_year1 = ""
    drop_year2 = ""
    prev_data = {}
    
    with open("life-expectancy.csv") as f:
        next(f)
        
        for line in f:
            parts = line.strip().split(',')
            country = parts[0]
            code = parts[1]
            year = int(parts[2])
            life_exp = float(parts[3])
            
            if life_exp < min_life:
                min_life = life_exp
                min_country = country
                min_year = year
                
            if life_exp > max_life:
                max_life = life_exp
                max_country = country
                max_year = year
                
            if year not in year_data:
                year_data[year] = []
            year_data[year].append((country, life_exp))
            
            if country not in country_data:
                country_data[country] = []
            country_data[country].append((year, life_exp))
            
            if country in prev_data:
                prev_life = prev_data[country]
                if prev_life - life_exp > largest_drop:
                    largest_drop = prev_life - life_exp
                    drop_country = country
                    drop_year1 = year - 1
                    drop_year2 = year
            prev_data[country] = life_exp
    
    print(f"The overall max life expectancy is: {max_life} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")
    print()
    
    year_input = int(input("Enter the year of interest: "))
    
    if year_input in year_data:
        countries = year_data[year_input]
        life_exps = [x[1] for x in countries]
        avg_life = sum(life_exps) / len(life_exps)
        
        min_country_year = min(countries, key=lambda x: x[1])
        max_country_year = max(countries, key=lambda x: x[1])
        
        print(f"\nFor the year {year_input}:")
        print(f"The average life expectancy across all countries was {avg_life:.2f}")
        print(f"The max life expectancy was in {max_country_year[0]} with {max_country_year[1]:.3f}")
        print(f"The min life expectancy was in {min_country_year[0]} with {min_country_year[1]:.3f}")
    else:
        print(f"No data available for year {year_input}")
    
    country_input = input("\nEnter a country to analyze (or press Enter to skip): ")
    if country_input in country_data:
        data = country_data[country_input]
        years = [x[0] for x in data]
        life_exps = [x[1] for x in data]
        
        min_year_country = min(data, key=lambda x: x[1])
        max_year_country = max(data, key=lambda x: x[1])
        avg_life_country = sum(life_exps) / len(life_exps)
        
        print(f"\nLife expectancy data for {country_input}:")
        print(f"Minimum: {min_year_country[1]:.2f} in {min_year_country[0]}")
        print(f"Maximum: {max_year_country[1]:.2f} in {max_year_country[0]}")
        print(f"Average: {avg_life_country:.2f} over {len(years)} years")
    elif country_input:
        print(f"No data available for country {country_input}")
    
    if largest_drop > 0:
        print(f"\nLargest life expectancy drop: {largest_drop:.2f} years")
        print(f"Country: {drop_country} between {drop_year1} and {drop_year2}")

if __name__ == "__main__":
    main()