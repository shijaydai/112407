
// 點擊"篩選評價"按鈕後，向content發送篩選評價的訊息
document.getElementById('applyFilter').addEventListener('click', function() {
  const keyword = document.getElementById('keyword').value;
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { type: 'applyFilter', keyword: keyword });
  });
});

// 點擊"清除篩選"按鈕後，向content發送清除篩選的訊息
document.getElementById('clearFilter').addEventListener('click', function() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { type: 'clearFilter' });
  });
});
