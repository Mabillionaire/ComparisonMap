L.Control.Compare = L.Control.extend({
    options: {
        position: 'topleft'
    },

    onAdd: function (map) {
        this.map = map;
        this.position = 0.5;
        
        // Create container
        this.container = L.DomUtil.create('div', 'leaflet-compare');
        this.container.style.position = 'absolute';
        this.container.style.top = '0';
        this.container.style.left = '0';
        this.container.style.right = '0';
        this.container.style.bottom = '0';
        this.container.style.pointerEvents = 'none';
        this.container.style.zIndex = '1000';
        this.container.style.width = '100%';
        this.container.style.height = '100%';
        
        // Create divider
        this.divider = L.DomUtil.create('div', 'leaflet-compare-divider', this.container);
        
        // Create range input
        this.range = L.DomUtil.create('input', 'leaflet-compare-range', this.container);
        this.range.type = 'range';
        this.range.min = 0;
        this.range.max = 1;
        this.range.step = 'any';
        this.range.value = this.position;
        this.range.style.width = '100%';
        this.range.style.position = 'absolute';
        this.range.style.top = '50%';
        this.range.style.left = '0';
        this.range.style.transform = 'translateY(-50%)';
        
        // Add events
        this.addEvents();
        
        // Initial update
        this.updateClip();
        
        // Add container to map pane
        const mapPane = this.map.getPanes().overlayPane;
        mapPane.appendChild(this.container);
        
        return this.container;
    },

    onRemove: function (map) {
        this.removeEvents();
        if (this.container && this.container.parentNode) {
            this.container.parentNode.removeChild(this.container);
        }
        this.map = null;
    },

    addEvents: function () {
        this.range.addEventListener('input', this.updateClip.bind(this));
        this.range.addEventListener('mousedown', this.cancelMapDrag.bind(this));
        this.range.addEventListener('mouseup', this.uncancelMapDrag.bind(this));
        this.range.addEventListener('touchstart', this.cancelMapDrag.bind(this));
        this.range.addEventListener('touchend', this.uncancelMapDrag.bind(this));
        
        this.map.on('move', this.updateClip, this);
    },

    removeEvents: function () {
        this.range.removeEventListener('input', this.updateClip.bind(this));
        this.range.removeEventListener('mousedown', this.cancelMapDrag.bind(this));
        this.range.removeEventListener('mouseup', this.cancelMapDrag.bind(this));
        this.range.removeEventListener('touchstart', this.cancelMapDrag.bind(this));
        this.range.removeEventListener('touchend', this.cancelMapDrag.bind(this));
        
        this.map.off('move', this.updateClip, this);
    },

    cancelMapDrag: function () {
        this.map.dragging.disable();
        if (this.map.tap) this.map.tap.disable();
    },

    uncancelMapDrag: function () {
        this.map.dragging.enable();
        if (this.map.tap) this.map.tap.enable();
    },

    updateClip: function () {
        if (!this.map) return;
        
        const mapSize = this.map.getSize();
        const rangeValue = parseFloat(this.range.value);
        const dividerX = mapSize.x * rangeValue;
        
        // Update divider position
        this.divider.style.left = `${dividerX}px`;
        
        // Apply clipping to map panes
        if (this.map.getPane("left") && this.map.getPane("right")) {
            // Apply clipping to left pane (current boundaries)
            this.map.getPane("left").style.clipPath = `inset(0 ${100 - (rangeValue * 100)}% 0 0)`;
            
            // Apply clipping to right pane (proposed boundaries)
            this.map.getPane("right").style.clipPath = `inset(0 0 0 ${rangeValue * 100}%)`;
        }
    },

    setPosition: function (position) {
        this.position = position;
        if (this.range) {
            this.range.value = position;
            this.updateClip();
        }
        return this;
    },

    getPosition: function () {
        return this.range ? parseFloat(this.range.value) : this.position;
    }
});

L.control.compare = function (leftLayers, rightLayers, options) {
    return new L.Control.Compare(options);
};
