
document.addEventListener('DOMContentLoaded', function () {
    // 添加消息監聽器，接收來自 content.js 的經緯度信息
    chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
        if (message.type === 'location_info') {
            var locationInfo = document.getElementById('locationInfo');
            locationInfo.textContent = '緯度：' + message.latitude + ', 經度：' + message.longitude;
        }
    });
});
