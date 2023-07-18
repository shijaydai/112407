// 当文档加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 在这里获取评论数据并进行分析，然后根据结果绘制图表或展示数据
    // 以下是一个简单的示例使用Chart.js绘制柱状图：
  
    // 假设这是您的评论数据
    const commentsData = {
      positive: 50,
      negative: 30,
      neutral: 20
    };
  
    // 使用Chart.js绘制柱状图
    const ctx = document.getElementById('chart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['正面', '负面', '中立'],
        datasets: [{
          label: '评论情感分析',
          data: [commentsData.positive, commentsData.negative, commentsData.neutral],
          backgroundColor: ['green', 'red', 'gray'],
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        legend: {
          display: false
        }
      }
    });
  });
