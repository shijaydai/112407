var app = new Vue({
    el: '#app',
    data: {
        currentSlide: 0,
        isPreviousSlide: false,
        isFirstLoad: true,
        slides: [
            {
                headlineFirstLine: "Lorem",
                headlineSecondLine: "Vitaer",
                sublineFirstLine: "Nihil sub sole",
                sublineSecondLine: "novum",
                bgImg: "https://i.postimg.cc/C5yvGSkm/slide0.jpg",
                rectImg: "https://i.postimg.cc/vTW0XkvM/slide-rect0.jpg"
            },
            {
                headlineFirstLine: "Nulla",
                headlineSecondLine: "Auctor",
                sublineFirstLine: "Il n'y a rien de neuf sous",
                sublineSecondLine: "le soleil",
                bgImg: "https://i.postimg.cc/Qx34VNXM/slide1.jpg",
                rectImg: "https://i.postimg.cc/ryWZ8R2b/slide-rect1.jpg"
            },
            {
                headlineFirstLine: "Nullam",
                headlineSecondLine: "Ultricies",
                sublineFirstLine: "Τίποτα καινούργιο κάτω από",
                sublineSecondLine: "τον ήλιο",
                bgImg: "https://i.postimg.cc/t4RBtrnQ/slide2.jpg",
                rectImg: "https://i.postimg.cc/3JFLGMRF/slide-rect2.jpg"
            }
        ]
    },
  mounted: function () {
    var productRotatorSlide = document.getElementById("app");
        var startX = 0;
        var endX = 0;

        productRotatorSlide.addEventListener("touchstart", (event) => startX = event.touches[0].pageX);

        productRotatorSlide.addEventListener("touchmove", (event) => endX = event.touches[0].pageX);

        productRotatorSlide.addEventListener("touchend", function(event) {
            var threshold = startX - endX;

            if (threshold < 150 && 0 < this.currentSlide) {
                this.currentSlide--;
            }
            if (threshold > -150 && this.currentSlide < this.slides.length - 1) {
                this.currentSlide++;
            }
        }.bind(this));
  },
    methods: {
        updateSlide(index) {
            index < this.currentSlide ? this.isPreviousSlide = true : this.isPreviousSlide = false;
            this.currentSlide = index;
            this.isFirstLoad = false;
        }
    }
})


// 获取按钮和下拉菜单元素
var dropdownButton = document.querySelector(".dropbtn");
var dropdownContent = document.querySelector(".dropdown-content");

// 添加按钮点击事件监听器
dropdownButton.addEventListener("click", function() {
  // 切换下拉菜单的显示/隐藏状态
  if (dropdownContent.style.display === "block") {
    dropdownContent.style.display = "none";
  } else {
    dropdownContent.style.display = "block";
  }
});

