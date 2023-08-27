document.getElementById("submitBtn").addEventListener("click", async function (e) {
		e.preventDefault();

        let name = document.getElementById("name").value;

        const formData = new FormData();
        formData.append("name", name);

        fetch("/studentCreate", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
        name = "";
            if(data === "user logged in!"){
                return alert("User: "+ name+" successfully logged in!");
            }else{
                return alert("User: "+ name+" failed to log in!");
            }
        })
        .catch(error => console.log("Error: "+error));
    });


document.getElementById("logout_btn").addEventListener("click", async function(e) {
	e.preventDefault();

	let name = document.getElementById("name").value;

    const formData = new FormData();
    formData.append("name", name);


    fetch("/studentRemove", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            name = "";
            if(data === "user logged out!"){
                return alert("User: "+ name+" successfully logged out!");
            }else{
                return alert("User: "+ name+" failed to log out!");
            }
        })
        .catch(error => console.log("Error: "+error));
});