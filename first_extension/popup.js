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


