
  // 
  document.addEventListener('DOMContentLoaded', function() {
    const applyFilterButton = document.getElementById('applyFilter');
  
    // 监听“应用筛选”按钮点击事件
    applyFilterButton.addEventListener('click', function() {
      // 获取用户输入的筛选关键词
      const filterKeyword = document.getElementById('filter').value;
  
      // 向当前激活的标签页发送筛选关键词
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { type: 'applyFilter', keyword: filterKeyword });
      });
    });
  });
