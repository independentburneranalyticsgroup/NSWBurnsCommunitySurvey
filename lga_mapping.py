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

def map_postcodes_to_lgas(postcode_counts, postcodes_df):
    """Map postcodes to LGAs and aggregate data"""
    print("Mapping postcodes to LGAs...")
    
    # Create a mapping from postcode to LGA
    postcode_to_lga = {}
    lga_data = defaultdict(lambda: {
        'respondent_count': 0,
        'postcodes': set(),
        'coordinates': [],
        'state': None
    })
    
    # First pass: create postcode to LGA mapping
    for _, row in postcodes_df.iterrows():
        postcode = row['postcode']
        if pd.notna(postcode):
            postcode_int = int(postcode)
            # Extract LGA from place_name (this is a simplified approach)
            place_name = row['place_name']
            state = row['state_name']
            
            # For now, we'll use the first part of place_name as LGA
            # In a real implementation, you'd want a proper LGA mapping
            lga = place_name.split(',')[0].strip() if ',' in place_name else place_name
            
            postcode_to_lga[postcode_int] = {
                'lga': lga,
                'state': state,
                'lat': row['latitude'],
                'lng': row['longitude']
            }
    
    # Second pass: aggregate data by LGA
    for postcode, respondent_count in postcode_counts.items():
        if postcode in postcode_to_lga:
            lga_info = postcode_to_lga[postcode]
            lga_name = lga_info['lga']
            
            lga_data[lga_name]['respondent_count'] += respondent_count
            lga_data[lga_name]['postcodes'].add(postcode)
            lga_data[lga_name]['coordinates'].append([lga_info['lat'], lga_info['lng']])
            lga_data[lga_name]['state'] = lga_info['state']
    
    return lga_data

def calculate_lga_centers(lga_data):
    """Calculate center points for each LGA"""
    print("Calculating LGA centers...")
    
    results = {}
    
    for lga_name, data in lga_data.items():
        if len(data['coordinates']) > 0:
            # Calculate center point
            lats = [coord[0] for coord in data['coordinates']]
            lngs = [coord[1] for coord in data['coordinates']]
            center_lat = np.mean(lats)
            center_lng = np.mean(lngs)
            
            results[lga_name] = {
                'state': data['state'],
                'num_postcodes': len(data['postcodes']),
                'center_latitude': center_lat,
                'center_longitude': center_lng,
                'all_coordinates': data['coordinates'],
                'respondent_count': data['respondent_count'],
                'postcodes': list(data['postcodes'])
            }
            
            print(f"  LGA {lga_name} ({data['state']}): {data['respondent_count']} respondents, {len(data['postcodes'])} postcodes, center at ({center_lat:.4f}, {center_lng:.4f})")
    
    return results

def main():
    """Main function to create LGA-based mapping"""
    print("Starting LGA-based mapping...")
    
    # Load data
    survey_df, postcodes_df = load_data()
    
    # Extract postcodes and count respondents
    postcode_counts = extract_postcodes(survey_df)
    
    # Map postcodes to LGAs
    lga_data = map_postcodes_to_lgas(postcode_counts, postcodes_df)
    
    # Calculate LGA centers
    results = calculate_lga_centers(lga_data)
    
    # Calculate statistics
    total_lgas = len(results)
    total_respondents = sum(data['respondent_count'] for data in results.values())
    total_postcodes = sum(data['num_postcodes'] for data in results.values())
    
    # Group by state
    state_counts = defaultdict(int)
    for lga_name, data in results.items():
        state_counts[data['state']] += 1
    
    print("\n" + "="*50)
    print("LGA-BASED MAPPING SUMMARY")
    print("="*50)
    print(f"Total LGAs processed: {total_lgas}")
    print(f"Total respondents: {total_respondents}")
    print(f"Total postcodes covered: {total_postcodes}")
    print(f"Average respondents per LGA: {total_respondents / total_lgas:.1f}")
    
    print("\nLGAs by state:")
    for state, count in sorted(state_counts.items()):
        print(f"  {state}: {count}")
    
    print("\nSample results:")
    for i, (lga_name, data) in enumerate(list(results.items())[:10]):
        print(f"  LGA {lga_name} ({data['state']}): {data['num_postcodes']} postcodes, {data['respondent_count']} respondents, center at ({data['center_latitude']:.4f}, {data['center_longitude']:.4f})")
    
    # Save results
    with open('lga_centers.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to lga_centers.json")
    print(f"\nSuccessfully processed {total_lgas} LGAs with {total_respondents} total respondents!")

if __name__ == "__main__":
    main() 