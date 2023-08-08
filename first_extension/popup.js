// 搜尋按鈕的點擊事件處理
document.getElementById('applyFilter').addEventListener('click', function() {
  searchPlaces();
});

// 清除按鈕的點擊事件處理
document.getElementById('clearFilter').addEventListener('click', function() {
  document.getElementById('keyword').value = '';
  searchPlaces();
});


// 點擊店家時的點擊事件處理
function onPlaceClick(place) {
  displayPlaceInfo(place);

  // 將店家資訊顯示在小視窗中
  const popupWindow = chrome.extension.getViews({ type: "popup" })[0];
  if (popupWindow) {
    const placeInfoDiv = popupWindow.document.getElementById('placeInfo');
    placeInfoDiv.innerHTML = '';
    placeInfoDiv.appendChild(createPlaceInfo(place));
  }
}

// 創建店家資訊元素
function createPlaceInfo(place) {
  const placeInfoDiv = document.createElement('div');

  const nameText = document.createElement('p');
  nameText.textContent = `店家名稱：${place.name}`;
  placeInfoDiv.appendChild(nameText);

  const addressText = document.createElement('p');
  addressText.textContent = `地址：${place.formatted_address}`;
  placeInfoDiv.appendChild(addressText);

  const phoneText = document.createElement('p');
  phoneText.textContent = `連絡電話：${place.formatted_phone_number || '未提供'}`;
  placeInfoDiv.appendChild(phoneText);

  return placeInfoDiv;
}

// // 店家搜尋功能
// function searchPlaces() {
//   const keyword = document.getElementById('keyword').value;
  
//   // 使用 Google Maps Places API 進行店家搜尋
//   const service = new google.maps.places.PlacesService(document.createElement('div'));
//   const request = {
//     query: keyword,
//     fields: ['name', 'formatted_address', 'geometry'],
//   };

//   service.findPlaceFromQuery(request, (results, status) => {
//     if (status === google.maps.places.PlacesServiceStatus.OK) {
//       displayResults(results);
//     } else {
//       alert('找不到符合搜尋條件的店家。');
//     }
//   });
// }