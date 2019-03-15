function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
async function updateJsonViewer() {
    while (true) {
        const Http = new XMLHttpRequest();
        Http.open("GET", url);
        Http.send();
        Http.onreadystatechange=(e)=>{
            // console.log(Http.responseText)
            var newJson = (Http.responseText).replace(/\\/g,"")
            // console.log(newJson)
            document.getElementById("JsonViewer").innerHTML = newJson;
        }
        // console.log(ApiType)
        await sleep(1000);
    }
}

url=window.location+'/api?dump=True';

console.log(url)

updateJsonViewer();