const result = document.getElementById("results");
const form = document.getElementById("form");
const requestURL = "https://nba-players.herokuapp.com/players/James/Lebron";
const requestURL2 =
  "https://9kxw5l4vg7.execute-api.us-east-1.amazonaws.com/Prod/hello/";
form.addEventListener("submit", (e) => {
  e.preventDefault();
  send_image();
});

async function send_image() {
  console.log("Called");
  const res = await fetch(requestURL);
  const data = await res.blob();
  const url = URL.createObjectURL(data);
  document.querySelector("img").src = url;

  // var img = new Image();
  // img.src = url;

  // const res2 = await fetch(requestURL2);
  // const data2 = await res2.json()
  // document.getElementById("lambda").innerHTML = data2
  // console.log(data2)

  const res3 = await fetch(requestURL2, {
    method: "post",
    body: JSON.stringify("HI"),
  });
  const data3 = await res3.json();
  console.log(data3);
}
