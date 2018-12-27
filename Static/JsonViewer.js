function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
async function updateJsonViewer() {
    while (true) {
        const Http = new XMLHttpRequest();
        Http.open("GET", url);
        Http.send();
        Http.onreadystatechange=(e)=>{
            console.log(Http.responseText)
            var newJson = (Http.responseText).replace(/\\/g,"")
            console.log(newJson)
            document.getElementById("JsonViewer").innerHTML = newJson;
        }
        // console.log(ApiType)
        await sleep(1000);
    }
}

url='http://104.230.28.139:5002/'+ApiType+'/api?dump=True';

updateJsonViewer();