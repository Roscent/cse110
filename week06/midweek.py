def main():
    min_life = float('inf')
    max_life = float('-inf')

    with open('life-expectancy.csv', 'r') as file:
        next(file)
        
        for line in file:
            parts = line.strip().split(',')
            
            try:
                life_expectancy = float(parts[3])
            except (IndexError, ValueError):
                continue  
            
            if life_expectancy < min_life:
                min_life = life_expectancy
            if life_expectancy > max_life:
                max_life = life_expectancy

    print(f"The lowest life expectancy in the dataset is: {min_life}")
    print(f"The highest life expectancy in the dataset is: {max_life}")

if __name__ == "__main__":
    main()