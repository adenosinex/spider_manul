async function sendText() {
    const text = document.querySelector('body > div.container > div.mybox > div.txtnav').textContent;

    let resp = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });

    let result = await resp.json();
    console.log(result);
}
      
 
    sendText();
    document.querySelector("body > div.container > div.mybox > div.page1 > a:nth-child(4)").click()
 
