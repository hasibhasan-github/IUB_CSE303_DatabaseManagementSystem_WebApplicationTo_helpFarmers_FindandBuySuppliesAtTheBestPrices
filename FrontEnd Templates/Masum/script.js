window.onload = function(){
    const sidebar = document.querySelector(".sidebar");
    const closeBtn = document.querySelector("#btn");
    const searchBtn = document.querySelector(".bx-search")

    closeBtn.addEventListener("click",function(){
        sidebar.classList.toggle("open")
        menuBtnChange()
    })

    searchBtn.addEventListener("click",function(){
        sidebar.classList.toggle("open")
        menuBtnChange()
    })

    function menuBtnChange(){
        if(sidebar.classList.contains("open")){
            closeBtn.classList.replace("bx-menu","bx-menu-alt-right")
        }else{
            closeBtn.classList.replace("bx-menu-alt-right","bx-menu")
        }
    }

    // new Chart(document.getElementById("chartjs-pie"), {
    //     type: "pie",
    //     data: {
    //       labels: ["Social", "Search Engines", "Direct", "Other"],
    //       datasets: [{
    //         data: [260, 125, 54, 146],
    //         backgroundColor: [
    //           window.theme.primary,
    //           window.theme.success,
    //           window.theme.warning,
    //           "#dee2e6"
    //         ],
    //         borderColor: "transparent"
    //       }]
    //     },
    //     options: {
    //       maintainAspectRatio: false,
    //       cutoutPercentage: 65,
    //     }
    //   });

}