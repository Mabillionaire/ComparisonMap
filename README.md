# 🏫 School Boundaries GIS Viewer

A modern, interactive web application for comparing and visualizing different school boundary datasets using a slider function and interactive mapping.

## ✨ Features

- **Interactive Map**: Built with Leaflet.js for smooth, responsive mapping
- **Dual Dataset Comparison**: View two different school boundary datasets simultaneously
- **Slider Control**: Smoothly blend between datasets with a real-time slider
- **Modern UI**: Beautiful, responsive design with gradient headers and smooth animations
- **Basemap Integration**: OpenStreetMap navigation basemap for context
- **Mobile Responsive**: Works seamlessly on desktop and mobile devices
- **Real-time Updates**: Instant visual feedback as you adjust the slider

## 🚀 Quick Start

1. **Open the Application**: Simply open `index.html` in any modern web browser
2. **Use the Slider**: Move the slider to blend between Dataset A (red) and Dataset B (blue)
3. **Explore the Map**: Click on boundaries for detailed information
4. **Navigate**: Use standard map controls (zoom, pan, etc.)

## 🛠️ Technical Details

### Built With
- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with flexbox, gradients, and responsive design
- **JavaScript (ES6+)**: Modern JavaScript with async/await support
- **Leaflet.js**: Open-source mapping library for interactive maps
- **OpenStreetMap**: Free, open-source mapping tiles

### Architecture
- **Modular Design**: Clean separation of concerns between UI, data, and mapping
- **Layer Management**: Efficient handling of multiple map layers
- **Event-Driven**: Responsive slider controls with real-time updates
- **Error Handling**: Graceful error handling and user feedback

## 📊 Data Integration

### Current Sample Data
The application currently includes sample school boundary data for demonstration:
- **Dataset A**: Sample school districts in New York and Los Angeles areas
- **Dataset B**: Slightly modified boundaries to show differences

### Integrating Real Shapefile Data

To use your actual school boundary shapefiles, you have several options:

#### Option 1: Convert to GeoJSON (Recommended)
1. Convert your shapefiles to GeoJSON format using QGIS, GDAL, or online converters
2. Replace the `sampleBoundariesA` and `sampleBoundariesB` arrays in the JavaScript code
3. Update the coordinate data with your actual boundary coordinates

#### Option 2: Use Shapefile.js
1. Include the `shapefile.js` library in your HTML
2. Load shapefiles directly in the browser
3. Parse and convert to GeoJSON format for Leaflet

#### Option 3: Server-Side Processing
1. Set up a backend service (Node.js, Python, etc.)
2. Convert shapefiles on the server
3. Serve GeoJSON data via API endpoints

### Data Format Example
```javascript
const realBoundariesA = [
    {
        name: "Your School District Name",
        coordinates: [
            [latitude1, longitude1],
            [latitude2, longitude2],
            [latitude3, longitude3],
            [latitude1, longitude1] // Close the polygon
        ]
    }
    // ... more boundaries
];
```

## 🎨 Customization

### Styling
- **Colors**: Modify CSS variables for custom color schemes
- **Layout**: Adjust CSS grid and flexbox properties for different layouts
- **Typography**: Update font families and sizes in the CSS

### Functionality
- **Blending Algorithm**: Customize the `createBlendedPolygon` function for different blending methods
- **Additional Controls**: Add more interactive elements like layer toggles or filters
- **Data Sources**: Integrate with external APIs or databases

## 🌐 Browser Compatibility

- **Chrome**: 60+ ✅
- **Firefox**: 55+ ✅
- **Safari**: 12+ ✅
- **Edge**: 79+ ✅
- **Internet Explorer**: Not supported ❌

## 📱 Mobile Features

- Responsive design that adapts to screen size
- Touch-friendly slider controls
- Optimized map interactions for mobile devices
- Collapsible UI elements for small screens

## 🔧 Development

### Local Development
1. Clone or download the project files
2. Open `index.html` in your browser
3. Use browser developer tools for debugging
4. Modify the JavaScript code for custom functionality

### Testing
- Test slider functionality across different browsers
- Verify mobile responsiveness
- Check map performance with large datasets
- Validate error handling

## 📈 Performance Considerations

- **Large Datasets**: For datasets with many boundaries, consider implementing clustering
- **Smooth Blending**: The current blending algorithm is simple; consider more sophisticated geometry operations for complex boundaries
- **Memory Management**: Clear unused layers to prevent memory leaks
- **Tile Loading**: Optimize basemap tile loading for better performance

## 🚀 Future Enhancements

- **Advanced Blending**: Implement more sophisticated boundary blending algorithms
- **Data Export**: Add functionality to export blended boundaries
- **Layer Management**: Allow users to toggle individual datasets on/off
- **Historical Comparison**: Add timeline functionality for temporal boundary changes
- **3D Visualization**: Extend to 3D mapping capabilities
- **Real-time Data**: Integrate with live data feeds

## 🤝 Contributing

Feel free to contribute improvements, bug fixes, or new features:
1. Fork the project
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For questions or issues:
1. Check the browser console for error messages
2. Verify your data format matches the expected structure
3. Ensure all dependencies are loading correctly
4. Test in different browsers to isolate issues

## 🎯 Use Cases

- **School District Planning**: Compare proposed vs. current boundaries
- **Educational Research**: Analyze boundary changes over time
- **Community Engagement**: Visualize boundary proposals for public input
- **Administrative Decision Making**: Support boundary-related policy decisions
- **GIS Education**: Teaching tool for geographic information systems

---

**Happy Mapping! 🗺️**
