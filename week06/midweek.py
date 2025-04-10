def main():
    # Initialize variables to track min and max life expectancy
    min_life = float('inf')
    max_life = float('-inf')

    # Open and read the life expectancy data file
    with open('life-expectancy.csv', 'r') as file:
        # Skip the header line
        next(file)
        
        # Process each line in the file
        for line in file:
            # Split the line into parts
            parts = line.strip().split(',')
            
            # Extract the life expectancy value (4th column)
            try:
                life_expectancy = float(parts[3])
            except (IndexError, ValueError):
                continue  # Skip lines with invalid data
                
            # Update min and max values
            if life_expectancy < min_life:
                min_life = life_expectancy
            if life_expectancy > max_life:
                max_life = life_expectancy

    # Display results
    print(f"The lowest life expectancy in the dataset is: {min_life}")
    print(f"The highest life expectancy in the dataset is: {max_life}")

if __name__ == "__main__":
    main()