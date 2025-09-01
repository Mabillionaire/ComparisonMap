# North Dakota School District Boundary Comparison Tool

A professional web application for comparing North Dakota school district boundaries between 2024 and 2025 using an interactive split-screen interface.

## Features

### **Interactive Split-Screen Comparison**
- **Side-by-side view** with draggable slider to compare 2024 vs 2025 boundaries
- **Real-time comparison** as you drag the slider across the map
- **Visual differentiation** with dashed blue lines (2024) and solid red lines (2025)

### **Enhanced Search Functionality**
- **District Search**: Find school districts by name, county, or ID
- **Address & Place Search**: Search for any address, city, landmark, or location in North Dakota
- **Geocoding Integration**: Uses OpenStreetMap Nominatim API for accurate address lookup
- **Smart Results**: Combines district and location results in one search

### **Layer Controls**
- **Independent Toggle**: Turn 2024 and 2025 boundaries on/off independently
- **Visual Indicators**: Color-coded checkboxes matching the boundary styles
- **Real-time Updates**: Instant visibility changes

### **Interactive Information Panel**
- **Hover Details**: Hover over any boundary to see district information
- **Comprehensive Data**: District name, ID, county, county seat, and LEA type
- **Clean Interface**: Information appears in a styled panel below the layer controls

### **Professional Styling**
- **Modern Design**: Clean, professional interface with gradient header
- **Responsive Layout**: Works on desktop and mobile devices
- **Visual Clarity**: Transparent fills with distinct line styles for easy comparison

## Quick Start

### **Option 1: Direct Use**
1. Open `north-dakota-wgs84-script.html` in any modern web browser
2. The application loads automatically with all data pre-configured
3. Start comparing boundaries immediately!

### **Option 2: Web Hosting**
1. Upload all files to any web server
2. Access via web browser
3. Share the URL with others

### **Option 3: GitHub Pages**
1. Enable GitHub Pages in your repository settings
2. Set source to "Deploy from a branch" → "master"
3. Access at `https://yourusername.github.io/ComparisonMap/north-dakota-wgs84-script.html`

## File Structure

```
ComparisonMap/
├── north-dakota-wgs84-script.html    # Main application file
├── leaflet-side-by-side.js           # Split-screen comparison plugin
├── nd_2024_boundaries.js             # 2024 school district data
├── nd_2025_boundaries.js             # 2025 school district data
├── convert_geojson_to_js.py          # Data conversion utility
└── README.md                         # This documentation
```

## Technical Details

### **Technologies Used**
- **Leaflet.js**: Interactive mapping library
- **Leaflet Side-by-Side**: Custom plugin for split-screen comparison
- **OpenStreetMap**: Basemap tiles and geocoding service
- **GeoJSON**: Geospatial data format
- **JavaScript**: Client-side functionality
- **HTML5/CSS3**: Modern web standards

### **Data Sources**
- **2024 Boundaries**: North Dakota Department of Public Instruction
- **2025 Boundaries**: Proposed changes for comparison
- **Geocoding**: OpenStreetMap Nominatim API
- **Basemap**: OpenStreetMap tiles

### **Browser Compatibility**
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+
- Mobile browsers

## How to Use

### **Basic Comparison**
1. **Drag the slider** in the center to compare boundaries
2. **Left side** shows 2024 boundaries (blue dashed lines)
3. **Right side** shows 2025 boundaries (red solid lines)

### **Search Functionality**
1. **Type in the search bar** (top-left)
2. **Search for districts**: "Fargo", "Bismarck High School"
3. **Search for addresses**: "123 Main St, Fargo"
4. **Search for places**: "Fargo Dome", "Grand Forks"
5. **Click results** to zoom to location

### **Layer Controls**
1. **Use checkboxes** (top-right) to toggle boundary visibility
2. **2024 checkbox**: Shows/hides current boundaries
3. **2025 checkbox**: Shows/hides proposed boundaries

### **Information Panel**
1. **Hover over any boundary** to see district details
2. **Information appears** in the panel below layer controls
3. **Move mouse away** to hide the panel

## Customization

### **Styling Changes**
Edit the CSS in `north-dakota-wgs84-script.html`:
- **Colors**: Change boundary colors in `styleCurrent()` and `styleProposed()` functions
- **Line styles**: Modify `dashArray` for different dash patterns
- **Interface**: Update CSS classes for different appearance

### **Data Updates**
1. **Replace GeoJSON files** with new boundary data
2. **Run conversion script**: `python convert_geojson_to_js.py`
3. **Update HTML** to reference new JavaScript files

## Data Conversion

The `convert_geojson_to_js.py` script converts GeoJSON files to JavaScript format for easy web loading:

```bash
python convert_geojson_to_js.py
```

This creates:
- `nd_2024_boundaries.js` - 2024 district data
- `nd_2025_boundaries.js` - 2025 district data

## Deployment Options

### **GitHub Pages**
- Free hosting for public repositories
- Automatic HTTPS
- Custom domain support

### **Netlify**
- Drag and drop deployment
- Automatic builds from Git
- Form handling and serverless functions

### **Vercel**
- Zero-config deployment
- Automatic scaling
- Global CDN

### **Traditional Web Hosting**
- Upload files via FTP/SFTP
- Works with any web server
- No special configuration needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues:
1. Check the [Issues](https://github.com/Mabillionaire/ComparisonMap/issues) page
2. Create a new issue with detailed description
3. Include browser version and error messages

## Acknowledgments

- **Leaflet.js** community for the excellent mapping library
- **OpenStreetMap** contributors for free map data
- **North Dakota Department of Public Instruction** for boundary data
- **Nominatim** for geocoding services

---

**Built for North Dakota education planning**