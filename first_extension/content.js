// 监听来自popup.js的消息请求
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.type === 'applyFilter') {
    // 获取筛选关键词
    const keyword = request.keyword;

    // 获取所有评论元素
    const reviewElements = document.querySelectorAll('div[data-review-id]');

    // 遍历所有评论，根据关键词筛选
    reviewElements.forEach(function(reviewElement) {
      const reviewText = reviewElement.innerText.toLowerCase();

      if (reviewText.includes(keyword)) {
        // 使用黄色表示筛选出的评论
        reviewElement.style.color = 'yellow';
      } 
      else {
        // 恢复默认的评论颜色
        reviewElement.style.color = '';
      }
    });
  }
});