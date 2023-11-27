
// 添加事件監聽器，捕捉 Google Maps 上店家位置的點擊事件
document.addEventListener('click', function (event) {
    // 檢查是否點擊了具有 'store-location' 類的元素
    if (event.target.classList.contains('store-location')) {
        // 獲取店家位置的經緯度信息
        var latitude = parseFloat(event.target.getAttribute('data-latitude'));
        var longitude = parseFloat(event.target.getAttribute('data-longitude'));

        // 發送經緯度信息到 popup.js
        chrome.runtime.sendMessage({
            type: 'location_info',
            latitude: latitude,
            longitude: longitude
        });
    }
});
