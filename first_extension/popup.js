
// // 點擊"篩選評價"按鈕後，向content發送篩選評價的訊息
// document.getElementById('applyFilter').addEventListener('click', function() {
//   const keyword = document.getElementById('keyword').value;
//   chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//     chrome.tabs.sendMessage(tabs[0].id, { type: 'applyFilter', keyword: keyword });
//   });
// });

// // 點擊"清除篩選"按鈕後，向content發送清除篩選的訊息
// document.getElementById('clearFilter').addEventListener('click', function() {
//   chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//     chrome.tabs.sendMessage(tabs[0].id, { type: 'clearFilter' });
//   });
// });
// 假設這是您獲取的店家評論資料和真實性百分比（假設真實性百分比為固定值）
// 假設這是您獲取的店家評論資料和真實性百分比（假設真實性百分比為固定值）
const commentsData = [
  { comment: "這個地方很棒！食物非常好吃！", reliabilityPercentage: 80 },
  { comment: "糟糕透了！這裡的服務太差了！", reliabilityPercentage: 40 },
  // 更多評論資料...
];

// 動態生成店家評論和真實性百分比
function generateComments() {
  const commentContainer = document.getElementById('commentContainer');
  commentContainer.innerHTML = ''; // 清空先前生成的評論內容

  commentsData.forEach(data => {
    const commentDiv = document.createElement('div');
    commentDiv.classList.add('comment');

    const commentText = document.createElement('p');
    commentText.textContent = data.comment;
    commentDiv.appendChild(commentText);

    const reliability = document.createElement('p');
    reliability.textContent = `真實性百分比：${data.reliabilityPercentage}%`;
    commentDiv.appendChild(reliability);

    commentContainer.appendChild(commentDiv);
  });
}

// 當擴充軟體視窗載入時，動態生成店家評論和真實性百分比
document.addEventListener('DOMContentLoaded', function() {
  generateComments();
});

// // 搜尋按鈕的點擊事件處理
// document.getElementById('applyFilter').addEventListener('click', function() {
//   // 在這裡可以獲取並處理搜尋關鍵字
//   const keyword = document.getElementById('keyword').value;
//   // 處理搜尋關鍵字的邏輯...
// });

// // 清除按鈕的點擊事件處理
// document.getElementById('clearFilter').addEventListener('click', function() {
//   // 將搜尋關鍵字的值清空
//   document.getElementById('keyword').value = '';
//   // 觸發搜尋按鈕的點擊事件，重新生成評論和真實性百分比（這裡假設搜尋按鈕有個 id 為 "applyFilter"）
//   document.getElementById('applyFilter').click();
// });

// 搜尋按鈕的點擊事件處理
document.getElementById('applyFilter').addEventListener('click', function() {
  searchPlaces();
});

// 清除按鈕的點擊事件處理
document.getElementById('clearFilter').addEventListener('click', function() {
  document.getElementById('keyword').value = '';
  searchPlaces();
});

// 店家搜尋功能
function searchPlaces() {
  const keyword = document.getElementById('keyword').value;
  
  // 使用 Google Maps Places API 進行店家搜尋
  const service = new google.maps.places.PlacesService(document.createElement('div'));
  const request = {
    query: keyword,
    fields: ['name', 'formatted_address', 'geometry'],
  };

  service.findPlaceFromQuery(request, (results, status) => {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
      displayResults(results);
    } else {
      alert('找不到符合搜尋條件的店家。');
    }
  });
}

// 顯示搜尋結果
function displayResults(results) {
  const resultContainer = document.getElementById('resultContainer');
  resultContainer.innerHTML = '';

  results.forEach(result => {
    const placeName = result.name;
    const placeAddress = result.formatted_address;

    const placeDiv = document.createElement('div');
    placeDiv.classList.add('place');

    const nameText = document.createElement('p');
    nameText.textContent = `店家名稱：${placeName}`;
    placeDiv.appendChild(nameText);

    const addressText = document.createElement('p');
    addressText.textContent = `地址：${placeAddress}`;
    placeDiv.appendChild(addressText);

    resultContainer.appendChild(placeDiv);
  });
}


