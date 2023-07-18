// 当收到来自弹出窗口或内容脚本的消息请求时
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    // 根据消息请求进行不同的处理
    if (request.requestMessage === 'Hello from popup') {
      // 如果是来自弹出窗口的消息请求，返回响应消息
      sendResponse({responseMessage: 'Hello from background to popup!'});
    } else if (request.requestMessage === 'Hello from content script') {
      // 如果是来自内容脚本的消息请求，返回响应消息
      sendResponse({responseMessage: 'Hello from background to content script!'});
    }
  });