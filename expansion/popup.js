document.addEventListener('DOMContentLoaded', function () {
    var searchInput = document.getElementById('searchInput');
    var searchButton = document.getElementById('searchButton');
    var placesList = document.getElementById('placesList');

    var latitude = null;
    var longitude = null;

    searchButton.addEventListener('click', function () {
        var searchTerm = searchInput.value;
        searchPlaces(searchTerm);
    });

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
                    latitude = place.geometry.location.lat();
                    longitude = place.geometry.location.lng();

                    placesList.appendChild(listItem);
                }
            } else {
                placesList.innerHTML = '未找到相符的店家。';
            }
        });
    }

    // 添加點擊事件監聽器以在點擊時顯示經緯度信息
    placesList.addEventListener('click', function () {
        if (latitude !== null && longitude !== null) {
            alert('經度: ' + longitude + ', 緯度: ' + latitude);
        } else {
            alert('未提供經緯度信息。');
        }
    });
});
