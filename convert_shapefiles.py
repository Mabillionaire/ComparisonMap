#!/usr/bin/env python3
"""
Shapefile to GeoJSON Converter for School Boundaries GIS Viewer

This script helps convert ESRI Shapefiles (.shp) to GeoJSON format
for easier integration with the web application.

Requirements:
- Python 3.6+
- geopandas
- pandas

Install dependencies:
pip install geopandas pandas

Usage:
python convert_shapefiles.py input_shapefile.shp output_geojson.json
"""

import sys
import json
import geopandas as gpd
from pathlib import Path

def convert_shapefile_to_geojson(input_path, output_path):
    """
    Convert a shapefile to GeoJSON format.
    
    Args:
        input_path (str): Path to input .shp file
        output_path (str): Path to output .json file
    """
    try:
        print(f"Loading shapefile: {input_path}")
        
        # Read the shapefile
        gdf = gpd.read_file(input_path)
        
        print(f"Shapefile loaded successfully!")
        print(f"Number of features: {len(gdf)}")
        print(f"Geometry types: {gdf.geometry.geom_type.unique()}")
        print(f"Columns: {list(gdf.columns)}")
        
        # Convert to GeoJSON
        geojson_data = gdf.to_json()
        
        # Parse and pretty-print the JSON
        parsed_json = json.loads(geojson_data)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(parsed_json, f, indent=2, ensure_ascii=False)
        
        print(f"GeoJSON saved to: {output_path}")
        print(f"File size: {Path(output_path).stat().st_size / 1024:.1f} KB")
        
        # Show sample of the data
        print("\nSample feature properties:")
        if len(gdf) > 0:
            sample_props = gdf.iloc[0].drop('geometry').to_dict()
            for key, value in sample_props.items():
                print(f"  {key}: {value}")
        
        return True
        
    except Exception as e:
        print(f"Error converting shapefile: {e}")
        return False

def convert_multiple_shapefiles(input_dir, output_dir):
    """
    Convert multiple shapefiles in a directory.
    
    Args:
        input_dir (str): Directory containing .shp files
        output_dir (str): Directory to save .json files
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists():
        print(f"Input directory does not exist: {input_dir}")
        return
    
    output_path.mkdir(exist_ok=True)
    
    # Find all .shp files
    shapefiles = list(input_path.glob("*.shp"))
    
    if not shapefiles:
        print(f"No .shp files found in {input_dir}")
        return
    
    print(f"Found {len(shapefiles)} shapefiles to convert:")
    
    for shp_file in shapefiles:
        print(f"\nProcessing: {shp_file.name}")
        
        # Create output filename
        output_file = output_path / f"{shp_file.stem}.json"
        
        # Convert the file
        success = convert_shapefile_to_geojson(str(shp_file), str(output_file))
        
        if success:
            print(f"✓ Successfully converted {shp_file.name}")
        else:
            print(f"✗ Failed to convert {shp_file.name}")

def create_web_app_data(geojson_path, output_js_path):
    """
    Create JavaScript data file for the web application.
    
    Args:
        geojson_path (str): Path to GeoJSON file
        output_js_path (str): Path to output JavaScript file
    """
    try:
        # Read GeoJSON
        with open(geojson_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)
        
        # Convert to web app format
        boundaries = []
        
        for feature in geojson_data['features']:
            # Extract coordinates and convert to lat/lng format
            if feature['geometry']['type'] == 'Polygon':
                coords = feature['geometry']['coordinates'][0]
                # Convert from [lng, lat] to [lat, lng] for Leaflet
                latlng_coords = [[coord[1], coord[0]] for coord in coords]
                
                # Extract name from properties
                properties = feature['properties']
                name = (properties.get('NAME') or 
                       properties.get('NAME_1') or 
                       properties.get('SCHOOL_NAME') or 
                       properties.get('DISTRICT') or 
                       'Unnamed Boundary')
                
                boundaries.append({
                    'name': name,
                    'coordinates': latlng_coords,
                    'properties': properties
                })
        
        # Create JavaScript code
        js_code = f"""// Auto-generated from {Path(geojson_path).name}
// Generated on: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

const boundariesData = {json.dumps(boundaries, indent=2, ensure_ascii=False)};

// Use this data in your web application by replacing the sample data arrays
// Example:
// boundariesA = boundariesData;
// boundariesB = boundariesData; // or load a different dataset
"""
        
        # Write JavaScript file
        with open(output_js_path, 'w', encoding='utf-8') as f:
            f.write(js_code)
        
        print(f"JavaScript data file created: {output_js_path}")
        print(f"Contains {len(boundaries)} boundaries")
        
        return True
        
    except Exception as e:
        print(f"Error creating JavaScript data: {e}")
        return False

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nExamples:")
        print("  python convert_shapefiles.py school_boundaries.shp school_boundaries.json")
        print("  python convert_shapefiles.py --batch input_folder output_folder")
        print("  python convert_shapefiles.py --web school_boundaries.json boundaries_data.js")
        return
    
    if sys.argv[1] == '--batch':
        if len(sys.argv) != 4:
            print("Usage: python convert_shapefiles.py --batch input_folder output_folder")
            return
        convert_multiple_shapefiles(sys.argv[2], sys.argv[3])
    
    elif sys.argv[1] == '--web':
        if len(sys.argv) != 4:
            print("Usage: python convert_shapefiles.py --web input.json output.js")
            return
        create_web_app_data(sys.argv[2], sys.argv[3])
    
    else:
        if len(sys.argv) != 3:
            print("Usage: python convert_shapefiles.py input.shp output.json")
            return
        convert_shapefile_to_geojson(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
