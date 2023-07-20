
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.type === 'applyFilter') {
      // 向content_script發送篩選評價的訊息
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { type: 'applyFilter', keyword: request.keyword });
      });
    } else if (request.type === 'clearFilter') {
      // 向content_script發送清除篩選的訊息
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { type: 'clearFilter' });
      });
    }
  });
  