window.onload = function () {

    // Validation e-mail

    const e_mail = document.getElementById("email");
    const e_mail_icon = document.querySelector(".email_icon");
    e_mail.addEventListener("keyup", (event) => {
        var re = /\S+@\S+\.\S+/;
        if (re.test(e_mail.value)) {
            e_mail_icon.classList.add("green");
            e_mail.style.borderColor = "green";
        }
    });


}
