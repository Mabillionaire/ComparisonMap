#!/usr/bin/env python3
"""
Convert GeoJSON files to JavaScript files for use with script tags.
This avoids CORS issues when loading GeoJSON files locally.
"""

import json
import os

def convert_geojson_to_js(geojson_file, js_file, variable_name):
    """Convert a GeoJSON file to a JavaScript file."""
    try:
        # Read the GeoJSON file
        with open(geojson_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Create JavaScript content
        js_content = f"var {variable_name} = {json.dumps(data, indent=2)};"
        
        # Write the JavaScript file
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"✓ Converted {geojson_file} to {js_file}")
        print(f"  Variable name: {variable_name}")
        print(f"  Features: {len(data.get('features', []))}")
        
    except Exception as e:
        print(f"✗ Error converting {geojson_file}: {e}")

def main():
    """Main conversion function."""
    print("Converting GeoJSON files to JavaScript...")
    print("=" * 50)
    
    # Convert 2024 boundaries
    convert_geojson_to_js(
        "ND_SchoolDistrict_2024_WGS84.geojson",
        "nd_2024_boundaries.js",
        "ND_SchoolDistrict_2024_WGS84"
    )
    
    # Convert 2025 boundaries
    convert_geojson_to_js(
        "ND_SchoolDistrict_2025_WGS84.geojson",
        "nd_2025_boundaries.js",
        "ND_SchoolDistrict_2025_WGS84"
    )
    
    print("=" * 50)
    print("Conversion complete!")
    print("\nNow you can use these JavaScript files in your HTML:")
    print('<script src="nd_2024_boundaries.js"></script>')
    print('<script src="nd_2025_boundaries.js"></script>')

if __name__ == "__main__":
    main()
