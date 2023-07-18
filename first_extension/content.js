// // 收集评论数据并发送给后台页面
// function collectCommentsData() {
//     // 假设这里是您收集评论数据的逻辑，实际上您需要根据您的实际需求来获取评论数据
//     const commentsData = {
//       positive: 50,
//       negative: 30,
//       neutral: 20
//     };
  
//     // 向后台页面发送评论数据
//     chrome.runtime.sendMessage({type: 'getCommentsData', data: commentsData});
//   }
  
//   // 在页面加载完成后，调用收集评论数据的函数
//   document.addEventListener('DOMContentLoaded', function() {
//     collectCommentsData();
//   });
// 從 Google Maps 評論頁面獲取評論資料
function getCommentsData() {
  const comments = document.querySelectorAll('.section-review .section-review-content');
  const commentsData = [];

  comments.forEach(comment => {
    const authorName = comment.querySelector('.section-review-title').textContent;
    const commentText = comment.querySelector('.section-review-text').textContent;
    const userProfilePic = comment.querySelector('.section-review-creator-profile-image img').src;

    // 假設這裡是您的情感分析程式碼，計算真實性百分比（這裡使用假設的百分比）
    const reliabilityPercentage = 80; // 假設真實性百分比為 80%

    commentsData.push({
      authorName,
      commentText,
      userProfilePic,
      reliabilityPercentage
    });
  });

  return commentsData;
}

// 將評論資料傳遞給彈出式視窗
function sendCommentsDataToPopup(commentsData) {
  const popupWindow = chrome.extension.getViews({ type: 'popup' })[0];

  if (popupWindow) {
    const commentsContainer = popupWindow.document.getElementById('comments');

    commentsData.forEach(commentData => {
      const commentDiv = document.createElement('div');
      commentDiv.classList.add('comment');

      const userProfilePic = document.createElement('img');
      userProfilePic.src = commentData.userProfilePic;
      commentDiv.appendChild(userProfilePic);

      const commentText = document.createElement('p');
      commentText.textContent = commentData.commentText;
      commentDiv.appendChild(commentText);

      const reliability = document.createElement('p');
      reliability.textContent = `真實性百分比：${commentData.reliabilityPercentage}%`;
      commentDiv.appendChild(reliability);

      commentsContainer.appendChild(commentDiv);
    });
  }
}

// 在 Google Maps 評論頁面準備就緒時執行
document.addEventListener('DOMContentLoaded', function() {
  const commentsData = getCommentsData();
  sendCommentsDataToPopup(commentsData);
});
