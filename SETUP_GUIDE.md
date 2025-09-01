# 🚀 Setup Guide - School Boundaries GIS Viewer

This guide will walk you through setting up and using the School Boundaries GIS Viewer application.

## 📋 Prerequisites

### For Basic Usage (HTML Only)
- Any modern web browser (Chrome, Firefox, Safari, Edge)
- No additional software installation required

### For Shapefile Processing
- Python 3.6 or higher
- pip (Python package installer)

## 🎯 Quick Start (5 minutes)

### Option 1: Basic Demo
1. **Open the application**: Double-click `index.html` or open it in your browser
2. **View the demo**: The app will show sample school boundaries
3. **Use the slider**: Move the slider to see the blending effect between datasets
4. **Explore the map**: Click on boundaries for information, zoom, and pan

### Option 2: Load Your Own Data
1. **Open the shapefile loader**: Open `shapefile-loader.html` in your browser
2. **Load sample data**: Click "Load Sample Data" to see the demo
3. **Load your shapefiles**: Use the file upload areas to load your .shp files
4. **Compare boundaries**: Use the slider to blend between your datasets

## 🛠️ Advanced Setup

### Installing Python Dependencies

If you want to convert shapefiles to GeoJSON format:

```bash
# Install required packages
pip install -r requirements.txt

# Or install individually
pip install geopandas pandas shapely fiona pyproj
```

### Converting Shapefiles

#### Single File Conversion
```bash
python convert_shapefiles.py input.shp output.json
```

#### Batch Conversion
```bash
python convert_shapefiles.py --batch input_folder output_folder
```

#### Create JavaScript Data
```bash
python convert_shapefiles.py --web input.json boundaries_data.js
```

## 📁 File Structure

```
gis-school-boundaries-app/
├── index.html                 # Basic demo application
├── shapefile-loader.html      # Advanced app with file loading
├── convert_shapefiles.py      # Python conversion script
├── requirements.txt           # Python dependencies
├── README.md                  # Comprehensive documentation
└── SETUP_GUIDE.md            # This setup guide
```

## 🔧 Configuration Options

### Customizing the Map

#### Change Basemap
In the HTML files, find this line:
```javascript
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 19
}).addTo(map);
```

Replace with other basemaps:
- **CartoDB**: `https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png`
- **ESRI**: `https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}`
- **Stamen**: `https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png`

#### Change Default View
Modify the map initialization:
```javascript
const map = L.map('map').setView([YOUR_LAT, YOUR_LNG], YOUR_ZOOM);
```

### Customizing Colors and Styling

#### Boundary Colors
Change the color scheme in the CSS:
```css
/* Dataset A (Red) */
.legend-color[style*="red"] { background: #your-color !important; }

/* Dataset B (Blue) */
.legend-color[style*="blue"] { background: #your-color !important; }
```

#### UI Theme
Modify the header gradient:
```css
.header {
    background: linear-gradient(135deg, #your-color1 0%, #your-color2 100%);
}
```

## 📊 Data Integration Methods

### Method 1: Direct Shapefile Loading (Recommended)
- Use `shapefile-loader.html`
- Drag and drop .shp files directly
- No conversion needed
- Real-time processing

### Method 2: GeoJSON Conversion
- Convert shapefiles to GeoJSON using the Python script
- Replace sample data in the HTML files
- Better performance for large datasets
- More control over data formatting

### Method 3: API Integration
- Set up a backend service
- Serve data via REST API
- Real-time updates
- Database integration

## 🎨 Customization Examples

### Adding New Controls
```javascript
// Add a layer toggle
const layerToggle = L.control.layers(null, {
    'Dataset A': layerA,
    'Dataset B': layerB,
    'Blended': blendedLayer
}).addTo(map);
```

### Custom Blending Algorithm
```javascript
function customBlending(coordsA, coordsB, blendRatio) {
    // Implement your own blending logic
    // Example: weighted average, interpolation, etc.
    return blendedCoords;
}
```

### Additional Map Features
```javascript
// Add scale bar
L.control.scale().addTo(map);

// Add fullscreen control
L.control.fullscreen().addTo(map);

// Add measure tool
L.control.measure().addTo(map);
```

## 🚨 Troubleshooting

### Common Issues

#### Map Not Loading
- Check browser console for errors
- Ensure internet connection (for basemap tiles)
- Verify Leaflet.js is loading correctly

#### Shapefiles Not Loading
- Ensure all required files (.shp, .shx, .dbf) are present
- Check file permissions
- Verify shapefile format is valid

#### Performance Issues
- Reduce dataset size
- Implement clustering for large datasets
- Use GeoJSON instead of direct shapefile loading

#### Browser Compatibility
- Use Chrome, Firefox, Safari, or Edge
- Internet Explorer is not supported
- Ensure JavaScript is enabled

### Error Messages

#### "No .shp file found"
- Ensure you're selecting the .shp file
- Check file extension is correct
- Try dragging and dropping the entire shapefile folder

#### "Error parsing shapefile"
- Verify shapefile is not corrupted
- Check if all required files are present
- Try converting to GeoJSON first

#### "Map container not found"
- Ensure the HTML file is properly loaded
- Check for JavaScript errors
- Verify DOM is ready before initializing map

## 🔍 Testing Your Setup

### Test Checklist
- [ ] Basic HTML app opens without errors
- [ ] Map displays correctly with basemap
- [ ] Sample data loads and displays
- [ ] Slider controls work smoothly
- [ ] File upload accepts .shp files
- [ ] Python conversion script runs successfully
- [ ] Custom data displays correctly
- [ ] Mobile responsiveness works

### Performance Testing
- Load datasets of various sizes
- Test slider responsiveness
- Check memory usage
- Verify smooth panning/zooming

## 📚 Additional Resources

### Documentation
- [Leaflet.js Documentation](https://leafletjs.com/reference.html)
- [Shapefile.js Documentation](https://github.com/mbostock/shapefile)
- [GeoPandas Documentation](https://geopandas.org/)

### Sample Data Sources
- [Natural Earth Data](https://www.naturalearthdata.com/)
- [US Census Bureau](https://www.census.gov/geographies/mapping-files.html)
- [OpenStreetMap](https://www.openstreetmap.org/)

### GIS Tools
- [QGIS](https://qgis.org/) - Open source GIS software
- [GDAL](https://gdal.org/) - Geospatial data abstraction library
- [PostGIS](https://postgis.net/) - Spatial database extension

## 🆘 Getting Help

### Before Asking for Help
1. Check the browser console for error messages
2. Verify all files are in the correct locations
3. Test with the sample data first
4. Check the troubleshooting section above

### Support Channels
- Check the README.md for detailed documentation
- Review the code comments for implementation details
- Test with different browsers and devices
- Verify your data format matches the expected structure

---

## 🎉 You're Ready!

Once you've completed the setup, you'll have a fully functional GIS web application that can:
- Display interactive maps with school boundaries
- Compare different boundary datasets
- Blend between datasets with a smooth slider
- Load real shapefile data
- Work on desktop and mobile devices

**Happy Mapping! 🗺️**
