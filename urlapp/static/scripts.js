$(document).ready(function () {
    $("#submit_btn").click(function () {
        entered_url = $("#base_url_field").val()
        if ((entered_url.indexOf("http://") == 0 || entered_url.indexOf("https://") == 0) == false) {
            alert("Missing HTTP protocol");
        }
        else {
            $.ajax({
                type: "GET",
                url: "shorten_url",
                data: {base_url: entered_url},
                success: function (response) {
                    let link = response.url;
                    console.log(link);
                    $("#short_url").text(link);
                    $("#short_url").attr("href", "http://" + link);
                },
                error: function (response) {
                console.log(response);
                },
            });
        }
    });
});