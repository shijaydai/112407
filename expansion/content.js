
function sendLocationInfo(latitude, longitude) {
    chrome.runtime.sendMessage({
        type: 'location_info',
        latitude: latitude,
        longitude: longitude
    });
}

function searchPlaces(searchTerm) {
    // 使用Google Maps JavaScript API進行地點搜索
    var request = {
        location: new google.maps.LatLng(25.042007, 121.525612), // 北商座標
        radius: '500',
        query: searchTerm
    };

    var service = new google.maps.places.PlacesService(document.createElement('div'));
    service.textSearch(request, function (results, status) {
        placesList.innerHTML = '';
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            for (var i = 0; i < results.length; i++) {
                var place = results[i];
                var listItem = document.createElement('li');
                listItem.textContent = place.name + ' - ' + place.formatted_address;

                // 獲取經緯度位置
                var latitude = place.geometry.location.lat();
                var longitude = place.geometry.location.lng();

                // 將經緯度位置添加到列表項
                listItem.textContent += ' - 經度: ' + longitude + ', 緯度: ' + latitude;

                placesList.appendChild(listItem);

                // 發送經緯度信息到小視窗
                sendLocationInfo(latitude, longitude);
            }
        } else {
            placesList.innerHTML = '未找到相符的店家。';
        }
    });
}
