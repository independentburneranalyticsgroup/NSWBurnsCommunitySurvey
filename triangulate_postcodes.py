import pandas as pd
import numpy as np
from collections import defaultdict
import json

def load_data():
    """Load the survey data and postcode data"""
    print("Loading data...")
    # Load survey data
    survey_df = pd.read_csv('map/NSW_Burns_Survey_cleaned.csv')
    print(f"Survey data shape: {survey_df.shape}")
    
    # Load postcode data
    postcodes_df = pd.read_csv('map/au_postcodes.csv')
    print(f"Postcode data shape: {postcodes_df.shape}")
    
    return survey_df, postcodes_df

def extract_postcodes(survey_df):
    """Extract postcodes and count respondents per postcode"""
    # Get the qid231_text column which contains postcodes
    postcode_column = survey_df['qid231_text']
    
    print(f"Total rows in postcode column: {len(postcode_column)}")
    print(f"Non-null values: {postcode_column.notna().sum()}")
    
    # Count respondents per postcode (including duplicates)
    postcode_counts = defaultdict(int)
    valid_postcodes = []
    
    for postcode in postcode_column:
        if pd.notna(postcode) and postcode != '':
            try:
                # Convert to integer postcode
                postcode_int = int(float(postcode))
                postcode_counts[postcode_int] += 1  # Count each respondent
                valid_postcodes.append(postcode_int)
            except (ValueError, TypeError):
                continue
    
    print(f"Found {len(valid_postcodes)} total postcode entries")
    print(f"Found {len(postcode_counts)} unique postcodes")
    print(f"Sample postcodes: {list(postcode_counts.keys())[:10]}")
    
    return postcode_counts

def find_postcode_coordinates(postcode_counts, postcodes_df):
    """Find coordinates for each postcode and calculate centers"""
    print("Finding coordinates for each postcode...")
    
    results = {}
    total_locations = 0
    
    for postcode, respondent_count in postcode_counts.items():
        print(f"Processing postcode {postcode}...")
        
        # Find all locations for this postcode
        postcode_locations = postcodes_df[postcodes_df['postcode'] == postcode]
        
        if len(postcode_locations) > 0:
            # Extract coordinates
            coordinates = []
            for _, row in postcode_locations.iterrows():
                if pd.notna(row['latitude']) and pd.notna(row['longitude']):
                    coordinates.append([row['latitude'], row['longitude']])
            
            if coordinates:
                # Calculate center point
                lats = [coord[0] for coord in coordinates]
                lngs = [coord[1] for coord in coordinates]
                center_lat = np.mean(lats)
                center_lng = np.mean(lngs)
                
                results[postcode] = {
                    'state': postcode_locations.iloc[0]['state_name'] if len(postcode_locations) > 0 else 'Unknown',
                    'num_locations': len(coordinates),
                    'center_latitude': center_lat,
                    'center_longitude': center_lng,
                    'all_coordinates': coordinates,
                    'respondent_count': respondent_count  # Add respondent count
                }
                
                total_locations += len(coordinates)
                print(f"  Found {len(coordinates)} locations, center at ({center_lat}, {center_lng}), {respondent_count} respondents")
            else:
                print(f"  No coordinates found for postcode {postcode}")
        else:
            print(f"  No coordinates found for postcode {postcode}")
    
    return results, total_locations

def main():
    """Main function to triangulate postcode locations"""
    print("Starting postcode triangulation...")
    
    # Load data
    survey_df, postcodes_df = load_data()
    
    # Extract postcodes and count respondents
    postcode_counts = extract_postcodes(survey_df)
    
    # Find coordinates for each postcode
    results, total_locations = find_postcode_coordinates(postcode_counts, postcodes_df)
    
    # Calculate statistics
    total_postcodes = len(results)
    total_respondents = sum(postcode_counts.values())
    avg_locations_per_postcode = total_locations / total_postcodes if total_postcodes > 0 else 0
    
    # Group by state
    state_counts = defaultdict(int)
    for postcode, data in results.items():
        state_counts[data['state']] += 1
    
    print("\n" + "="*50)
    print("POSTCODE TRIANGULATION SUMMARY")
    print("="*50)
    print(f"Total postcodes processed: {total_postcodes}")
    print(f"Total respondents: {total_respondents}")
    print(f"Total locations found: {total_locations}")
    print(f"Average locations per postcode: {avg_locations_per_postcode:.1f}")
    print(f"Average respondents per postcode: {total_respondents / total_postcodes:.1f}")
    
    print("\nPostcodes by state:")
    for state, count in sorted(state_counts.items()):
        print(f"  {state}: {count}")
    
    print("\nSample results:")
    for i, (postcode, data) in enumerate(list(results.items())[:10]):
        print(f"  Postcode {postcode} ({data['state']}): {data['num_locations']} locations, {data['respondent_count']} respondents, center at ({data['center_latitude']}, {data['center_longitude']})")
    
    # Save results
    with open('postcode_centers.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to postcode_centers.json")
    print(f"\nSuccessfully processed {total_postcodes} postcodes with {total_respondents} total respondents!")

if __name__ == "__main__":
    main() 