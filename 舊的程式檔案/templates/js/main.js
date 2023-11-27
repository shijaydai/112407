const chartData = {
    labels: ["有效評論", "無效評論"],
    data: [30, 70],
  };
  
  const myChart = document.querySelector(".my-chart");
  const ul = document.querySelector(".programming-stats .details ul");
  
  new Chart(myChart, {
    type: "doughnut",
    data: {
      labels: chartData.labels,
      datasets: [
        {
          label:"佔比",
          data: chartData.data,
        },
      ],
    },
    options: {
      borderWidth: 10,
      borderRadius: 2,
      hoverBorderWidth: 0,
      plugins: {
        legend: {
          display: false,
        },
      },
    },
  });
  
  const populateUl = () => {
    chartData.labels.forEach((l, i) => {
      let li = document.createElement("li");
      li.innerHTML = `${l}: <span class='percentage'>${chartData.data[i]}%</span>`;
      ul.appendChild(li);
    });
  };
  
  populateUl();

  /*----------login---------- */
  function show_hide() {
    var login = document.getElementById("container1");
    var signup = document.getElementById("container2");
    var copyright = document.getElementById("copyright");
  
    if (login.style.display === "none") {
        login.style.display = "block";  //lonin出現
        document.getElementById("username").value="";
        document.getElementById("password").value="";
        signup.style.display = "none";  //signup消失
        copyright.style.margin = "200px 0px 0px 0px";
    } else {
        login.style.display = "none";   //login消失
        signup.style.display = "block"; //signup出現
        signup.style.visibility="visible";
        copyright.style.margin = "200px 0px 0px 0px";
     
        document.getElementById("fullname").value="";
        document.getElementById("username2").value="";
        document.getElementById("password2").value="";
        document.getElementById("comfirm_password").value="";
    }
}
  