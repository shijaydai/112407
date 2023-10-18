// 這是要檢測變化的元素的選擇器
var elementSelector = '.title.full-width';

// 這是顯示變化內容的目標 div 元素
var placeInfoDiv = document.getElementById('placeInfo');

// 開始定期檢查元素內容
function detectTextChange() {
    var targetElement = document.querySelector(elementSelector);
    console.log("我在這");
    if (targetElement) {
        var currentText = targetElement.textContent;

        if (currentText !== initialText) {
            
            // 文本內容已經變化，將其放入 placeInfoDiv
            var addressElement = document.querySelector('.address-line.full-width');
            var addressText = addressElement ? addressElement.textContent : '地址未提供';

            var phoneElement = document.querySelector('.view-link a');
            var phoneText = phoneElement ? phoneElement.textContent : '聯絡電話未提供';

            var info = '<h3>店家信息</h3>';
            info += '<strong>店家名稱:</strong> ' + currentText + '<br>';
            info += '<strong>地址:</strong> ' + addressText + '<br>';
            info += '<strong>聯絡電話:</strong> ' + phoneText + '<br>';
           

            placeInfoDiv.innerHTML = info;
            $.ajax({
                url: '',  // 伺服器端的 URL
                type: 'GET',  // 請求類型為 GET
                data: {
                    currentText: currentText,  // 傳遞給伺服器的參數，以 a_id 為名
                    address: addressText,
                },
                success: function (response) {
                    console.log('hello'+response);
                    var resultDiv = document.getElementById('results');
                    var info = '<strong>店家信息</strong><br>';
                    info += '店家名稱: ' + currentText + '<br>';
                    info += '地址: ' + addressText + '<br>';
                    info += '聯絡電話: ' + phoneText + '<br><br>';
                    info += '<strong>用戶信息</strong><br>';

                    
                    var jsonData = JSON.parse(response.comment);
                    console.log(jsonData[0]);
                    for (let i = 0; i < jsonData.length; i++) {
                        info += '留言者名字: ' + jsonData[i].username + '<br>';
                        info += '留言時間: ' + jsonData[i].msgtime + '<br>';
                        info += '星星數: ' + jsonData[i].star + '<br>';
                        info += '評論: ' + jsonData[i].comment + '<br>';
                        info += '有效性: ' + jsonData[i].effflag + '<br>';    
                    }

                    
                    resultDiv.innerHTML = info;
                },
                
                error: function (xhr, status, error) {
                    // 請求失敗時的處理
                    console.log("search_textAJAX請求失敗: " + error);
                }
            });
            return true;
        } else {
            // 文本內容未變化
            return false;
        }
    } else {
        // 如果找不到指定的元素，可以在這裡處理相應的情況
        return false;
    }
}

// 初始化最初的文本內容
var initialText = detectTextChange();

// 定期檢查變化
setInterval(function () {
    if (detectTextChange()) {
        console.log("文字已變化");
        // 在這裡執行相關的操作
    }
}, 1000); // 以毫秒為單位，此處設定為每秒檢查一次
