var map;
var service;
var markers = [];
var marker ;
var Favorite = document.getElementById('Favorite');
var selectedLocation = null;

function initMap() {
    var center = new google.maps.LatLng(25.042007, 121.525612);
    map = new google.maps.Map(document.getElementById('map'), {
        center: center,
        zoom: 15
    });

    map.addListener('click', function() {
        clearPlaceInfo();
    });
    
}

function placeMarker(location) {
    if (marker) {
      marker.setPosition(location);
    } else {
      marker = new google.maps.Marker({
        position: location,
        map: map
      });
    }
  }



function searchPlaces() {
    var searchInput = document.getElementById('searchInput').value;
    var request = {
        location: map.getCenter(),
        radius: '500',
        query: searchInput
    };
    
    service = new google.maps.places.PlacesService(map);
    service.textSearch(request, displayResults);
}

function displayResults(results, status) {
    var placesList = document.getElementById('placesList');
    placesList.innerHTML = '';

    if (status == google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            var place = results[i];
            var listItem = document.createElement('li');
            listItem.textContent = place.name + ' - ' + place.formatted_address;

            // 檢查是否有聯絡電話
            if (place.formatted_phone_number) {
                listItem.textContent += ' - 聯絡電話: ' + place.formatted_phone_number;
            } else {
                listItem.textContent += ' - 聯絡電話: 未提供';
            }

            var marker = new google.maps.Marker({
                map: map,
                position: place.geometry.location,
                title: place.name
            });

            marker.addListener('click', function() {
                showPlaceInfo(place);
            });

            markers.push(marker);

            placesList.appendChild(listItem);
        }

        // 如果有搜尋結果，設定地圖中心和縮放級別以顯示第一個結果
        map.setCenter(results[0].geometry.location);
        map.setZoom(15);
    } else {
        placesList.innerHTML = '未找到相符的店家。';
    }
}

function clearPlaceInfo() {
    var placeInfoDiv = document.getElementById('placeInfo');
    placeInfoDiv.innerHTML = ''; // 清空信息
}

// 新增搜尋位置的功能
function searchLocation() {
    var searchLocationInput = document.getElementById('searchLocationInput').value;
    var geocoder = new google.maps.Geocoder();

    geocoder.geocode({ 'address': searchLocationInput }, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK && results.length > 0) {
            var location = results[0].geometry.location;
            map.setCenter(location);
            map.setZoom(15); // 調整縮放級別以顯示選定位置
        } else {
            alert('找不到該位置');
        }
    });
}      











