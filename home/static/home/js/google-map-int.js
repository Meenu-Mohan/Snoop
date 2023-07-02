$(document).ready(function () {
    'use strict';

    var marker;

    function initMap() {
        var map = new google.maps.Map(document.getElementById('loc-mp'), {
            zoom: 13,
            center: {lat: 8.885730, lng: 76.607087}
        });

        marker = new google.maps.Marker({
            map: map,
            draggable: true,
            animation: google.maps.Animation.DROP,
            position: {lat: 8.885730, lng: 76.607087}
        });
        marker.addListener('click', toggleBounce);
    }

    function toggleBounce() {
        if (marker.getAnimation() !== null) {
            marker.setAnimation(null);
        } else {
            marker.setAnimation(google.maps.Animation.BOUNCE);
        }
    }

    google.maps.event.addDomListener(window, 'load', initMap);

});