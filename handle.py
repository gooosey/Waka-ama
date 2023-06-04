import os
import csv

# Function to read the raw data from the race results files
def read_race_results(folder_path):
    race_results = []
    files = os.listdir(folder_path)
    
    for file in files:
        if file.endswith(".lif"):
            with open(os.path.join(folder_path, file), "r") as f:
                race_data = f.read()
                race_results.append(race_data)
    
    return race_results

# Function to assign points based on placements
def assign_points(placements):
    points = [8, 7, 6, 5, 4, 3, 2, 1]
    points_assigned = []
    
    for i, place in enumerate(placements):
        if i < len(points):
            points_assigned.append(points[i])
        else:
            points_assigned.append(1)
    
    return points_assigned

# Function to analyze the race results and determine the winning regional association
def analyze_race_results(race_results):
    regional_points = {}
    
    for race in race_results:
        # Process the race data and extract relevant information
        # (e.g., regional association and placement)
        # Replace this with your own implementation
        
        regional_association = "Sample Regional Association"
        placements = [1, 2, 2, 4, 5, 5]  # Sample placements
        
        # Assign points based on placements
        points_assigned = assign_points(placements)
        
        # Update regional points
        if regional_association in regional_points:
            regional_points[regional_association] += sum(points_assigned)
        else:
            regional_points[regional_association] = sum(points_assigned)
    
    # Sort regional associations based on total points in descending order
    sorted_regional_points = sorted(regional_points.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_regional_points

# Function to generate the output .csv file
def generate_output_csv(sorted_regional_points, output_file):
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Regional Association", "Points"])
        
        for regional_association, points in sorted_regional_points:
            writer.writerow([regional_association, points])

# Main program
def main():
    folder_path = "resources"
    output_file = "output.csv"
    
    # Read the raw race results
    race_results = read_race_results(folder_path)
    
    # Analyze the race results
    sorted_regional_points = analyze_race_results(race_results)
    
    # Generate the output .csv file
    generate_output_csv(sorted_regional_points, output_file)
    
    print("Analysis completed. Results saved to", output_file)

if __name__ == "__main__":
    main()
