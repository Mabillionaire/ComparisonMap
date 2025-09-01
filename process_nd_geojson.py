import json
import math

def web_mercator_to_lat_lng(x, y):
    """Convert Web Mercator coordinates to latitude/longitude."""
    # Web Mercator to lat/lng conversion
    lng = x / 20037508.34 * 180
    lat = math.atan(math.sinh(math.pi * (1 - 2 * y / 20037508.34))) * 180 / math.pi
    return [lat, lng]

def process_geojson_file(file_path, output_name):
    """Process a GeoJSON file and extract boundary data for the comparison tool."""
    
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    boundaries = []
    
    if 'features' in data:
        for feature in data['features']:
            if feature['geometry']['type'] == 'Polygon':
                # Extract coordinates
                coordinates = feature['geometry']['coordinates'][0]  # First polygon
                
                # Convert from Web Mercator to lat/lng for Leaflet
                leaflet_coords = []
                for coord in coordinates:
                    lat_lng = web_mercator_to_lat_lng(coord[0], coord[1])
                    leaflet_coords.append(lat_lng)
                
                # Extract properties
                properties = feature.get('properties', {})
                
                # Create boundary object
                boundary = {
                    "name": properties.get('DistrictNa', properties.get('NAME', properties.get('DISTRICT_NAME', 'Unknown District'))),
                    "coordinates": leaflet_coords,
                    "properties": {
                        "DISTRICT_ID": str(properties.get('DistrictID', properties.get('DISTRICT_ID', properties.get('ID', 'Unknown')))),
                        "DISTRICT_NAME": properties.get('DistrictNa', properties.get('NAME', properties.get('DISTRICT_NAME', 'Unknown District'))),
                        "COUNTY": properties.get('CountyName', properties.get('COUNTY', properties.get('COUNTY_NAME', 'Unknown County')))
                    }
                }
                
                boundaries.append(boundary)
            elif feature['geometry']['type'] == 'MultiPolygon':
                # Handle MultiPolygon geometry
                for polygon_coords in feature['geometry']['coordinates']:
                    # Take the first polygon from MultiPolygon
                    coordinates = polygon_coords[0]
                    
                    # Convert from Web Mercator to lat/lng for Leaflet
                    leaflet_coords = []
                    for coord in coordinates:
                        lat_lng = web_mercator_to_lat_lng(coord[0], coord[1])
                        leaflet_coords.append(lat_lng)
                    
                    # Extract properties
                    properties = feature.get('properties', {})
                    
                    # Create boundary object
                    boundary = {
                        "name": properties.get('DistrictNa', properties.get('NAME', properties.get('DISTRICT_NAME', 'Unknown District'))),
                        "coordinates": leaflet_coords,
                        "properties": {
                            "DISTRICT_ID": str(properties.get('DistrictID', properties.get('DISTRICT_ID', properties.get('ID', 'Unknown')))),
                            "DISTRICT_NAME": properties.get('DistrictNa', properties.get('NAME', properties.get('DISTRICT_NAME', 'Unknown District'))),
                            "COUNTY": properties.get('CountyName', properties.get('COUNTY', properties.get('COUNTY_NAME', 'Unknown County')))
                        }
                    }
                    
                    boundaries.append(boundary)
                    break  # Only take the first polygon from MultiPolygon
    
    print(f"Found {len(boundaries)} school districts")
    
    # Create JavaScript data file
    js_content = f"""// {output_name} - Generated from GeoJSON
const {output_name} = {json.dumps(boundaries, indent=2)};

// Export for use in HTML
if (typeof module !== 'undefined' && module.exports) {{
    module.exports = {output_name};
}}
"""
    
    # Write JavaScript file
    js_filename = f"{output_name}.js"
    with open(js_filename, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Created {js_filename}")
    
    return boundaries

def main():
    """Process both GeoJSON files."""
    
    # Process 2024 (current) boundaries
    current_boundaries = process_geojson_file(
        'ND_SchoolDistrict_2024.geojson', 
        'currentBoundariesData'
    )
    
    # Process 2025 (proposed) boundaries
    proposed_boundaries = process_geojson_file(
        'ND_SchoolDistrict_2025.geojson', 
        'proposedBoundariesData'
    )
    
    # Create a combined data file
    combined_content = f"""// North Dakota School District Boundaries - Combined Data
// Generated from GeoJSON files

// Current boundaries (2024)
const currentBoundariesData = {json.dumps(current_boundaries, indent=2)};

// Proposed boundaries (2025)
const proposedBoundariesData = {json.dumps(proposed_boundaries, indent=2)};

// Export for use in HTML
if (typeof module !== 'undefined' && module.exports) {{
    module.exports = {{
        currentBoundariesData,
        proposedBoundariesData
    }};
}}
"""
    
    with open('nd_boundaries_data.js', 'w', encoding='utf-8') as f:
        f.write(combined_content)
    
    print("\nCreated nd_boundaries_data.js with combined data")
    print(f"Total districts: {len(current_boundaries)} current, {len(proposed_boundaries)} proposed")

if __name__ == "__main__":
    main()
