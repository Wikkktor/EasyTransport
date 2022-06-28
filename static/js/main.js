window.onload = function () {

    const body = document.querySelector("body"),
        sidebar = body.querySelector(".sidebar"),
        toggle = body.querySelector(".toggle"),
        modeSwitch = body.querySelector(".toggle-switch"),
        modeText = body.querySelector(".mode-text");


    toggle.addEventListener("click", () => {
        sidebar.classList.toggle("close");
    })


    modeSwitch.addEventListener("click", () => {
        body.classList.toggle("dark");
        try {
           initMap();
        }
        catch (error) {
            null
        }
        let cook = darkCookieGet("stdark");
        if (body.classList[0] === "dark"){
            if (cook == "")  {
                setDarkCookie("stdark", 1, 30);
            }
        }
        else {
            if (cook != "")  {
                document.cookie = "stdark=1;expires=Thu, 01 Jan 1970 00:00:01 GMT";
            }
        }
    })
}
    function setDarkCookie(cname, cvalue, exdays) {
        const d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        let expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    function darkCookieGet(cname) {
        let name = cname + "=";
        let ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }
