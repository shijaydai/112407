
// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
//   if (request.type === 'applyFilter') {
//     const keyword = request.keyword;
//     console.log('篩選評價，關鍵字：', keyword);

//     // 執行篩選評價的函數
//     filterReviews(keyword);
//   } else if (request.type === 'clearFilter') {
//     console.log('清除篩選');

//     // 執行清除篩選的函數
//     clearFilter();
//   }
// });

// // 篩選評價的函數
// function filterReviews(keyword) {
//   // 獲取所有店家評價元素
//   const reviewElements = document.querySelectorAll('div.section-review-content');

//   // 遍歷所有評價元素並篩選評價
//   reviewElements.forEach(function(reviewElement) {
//     const reviewText = reviewElement.querySelector('span.section-review-text').textContent;

//     // 將篩選的關鍵字用顏色標示
//     if (keyword && keyword !== '' && reviewText.includes(keyword)) {
//       reviewElement.style.color = 'green'; // 使用綠色表示包含關鍵字的評價
//     } else {
//       reviewElement.style.color = ''; // 恢復默認的評價顏色
//     }
//   });
// }

// // 清除篩選的函數
// function clearFilter() {
//   // 獲取所有店家評價元素
//   const reviewElements = document.querySelectorAll('div.section-review-content');

//   // 清除所有評價元素的標示顏色
//   reviewElements.forEach(function(reviewElement) {
//     reviewElement.style.color = ''; // 恢復默認的評價顏色
//   });
// }
// // 直接導航到 Google Maps 的評論區
// function redirectToGoogleMaps() {
//   // 修改當前頁面的 URL，導向 Google Maps 的評論區
//   window.location.href = "https://www.google.com/maps/reviews";
// }

// // 點擊擴充按鈕時的點擊事件處理
// document.getElementById('applyFilter').addEventListener('click', function() {
//   redirectToGoogleMaps();
// });

