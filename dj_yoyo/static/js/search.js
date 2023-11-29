var map;
var service;
var markers = [];
var marker ;
var Favorite = document.getElementById('Favorite');
var selectedLocation = null;
var searchHistory = [];

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
    service.textSearch(request,  function(results, status){
        displayResults(results, status);
        
        // 將搜尋結果保存到搜尋記錄陣列中
        searchHistory.push({ query: searchInput, results: results});
        localStorage.setItem('searchHistory', JSON.stringify(searchHistory));
        // 顯示搜尋記錄
        showSearchHistory();
    });
}

function displayResults(results, status) {
    var placesList = document.getElementById('placesList');
    placesList.innerHTML = '';
    console.log('000000000000000000')
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
        
        // console.log(place.name);
        // searchHistory.push(place.name);
        // showSearchHistory(searchHistory)
        // console.log(searchHistory)
        


        // 如果有搜尋結果，設定地圖中心和縮放級別以顯示第一個結果
        map.setCenter(results[0].geometry.location);
        map.setZoom(15);
    } else {
        placesList.innerHTML = '未找到相符的店家。';
    }
}

function showSearchHistory() {
    var historyContainer = document.getElementById('searchHistoryContainer');

    // 清空搜尋記錄容器
    historyContainer.innerHTML = '';

    // 迭代搜尋記錄陣列
    for (var i = 0; i < searchHistory.length; i++) {
        var searchRecord = document.createElement('div');
        searchRecord.textContent = '搜尋記錄 ' + (i + 1) + ': ' + searchHistory[i].query ;
        historyContainer.appendChild(searchRecord);
    }
}



document.addEventListener('DOMContentLoaded', function() {
    console.log('7777777777777777777')
    var myList = document.getElementById('myList').getElementsByTagName('tbody')[0];

    var storedSearchHistory = localStorage.getItem('searchHistory');
    var searchHistory = storedSearchHistory ? JSON.parse(storedSearchHistory) : [];

    // 清空表格內容
    myList.innerHTML = '';

    // 迭代陣列，將每個元素插入表格
    searchHistory.forEach(function(item, index) {
        var row = myList.insertRow();
        var cell1 = row.insertCell(0);
        cell1.textContent = item.query;

        var cell2 = row.insertCell(1);
        var deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = '刪除';
        deleteBtn.onclick = function() {
            // 刪除陣列中的對應項目
            searchHistory.splice(index, 1);
            // 重新渲染表格
            renderTable();
        };
        cell2.appendChild(deleteBtn);
    });

    // 重新渲染表格的函數
    function renderTable() {
        // 清空表格內容
        myList.innerHTML = '';

        // 迭代陣列，將每個元素插入表格
        searchHistory.forEach(function(item, index) {
            var row = myList.insertRow();
            var cell1 = row.insertCell(0);
            cell1.textContent = item.query;

            var cell2 = row.insertCell(1);
            var deleteBtn = document.createElement('span');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = '刪除';
            deleteBtn.onclick = function() {
                // 刪除陣列中的對應項目
                searchHistory.splice(index, 1);
                // 重新渲染表格
                renderTable();
            };
            cell2.appendChild(deleteBtn);
        });

        // 更新本地存儲的數據
        localStorage.setItem('searchHistory', JSON.stringify(searchHistory));
    }
});




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











