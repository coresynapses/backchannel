(function () {
    function hide(arg) {arg.style.display = "none";}
    function show(arg) {arg.style.display = "block";}

    make_thread = document.getElementById("make-thread");

    if(make_thread) {
	post_thread_form = document.getElementById("post-thread-form");
	close_form = document.getElementById("close-form");

	show(make_thread);
	hide(post_thread_form);

	make_thread.addEventListener("click", (event) => {
	    console.log(event);
	    hide(make_thread);
	    show(post_thread_form);
	});

	close_form.addEventListener("click", (event) => {
	    console.log(event);
	    show(make_thread);
	    hide(post_thread_form);
	});
    }


    style_mode = document.getElementById("style-mode");
    light_mode = document.getElementById("light-mode");
    dark_mode = document.getElementById("dark-mode");

    light_mode_css = "body{background: white; color: black;}"
    dark_mode_css = "body{background: black; color: white;}"

    style_mode.innerText = dark_mode;

    light_mode.addEventListener("click", (event) => {
	hide(light_mode);
	show(dark_mode);
	style_mode.innerText = light_mode_css;
    });
    dark_mode.addEventListener("click", (event) => {
	show(light_mode);
	hide(dark_mode);
	style_mode.innerText = dark_mode_css;
    });


    custom_css_button = document.getElementById("custom-css-button");
    custom_css_controller = document.getElementById("custom-css-controller");
    custom_css_close = document.getElementById("custom-css-close");
    custom_css_area = document.getElementById("custom-css-area");
    custom_css_save = document.getElementById("custom-css-close");

    custom_css_button.addEventListener("click", (event) => {
	custom_css_controller.style.display = "flex";
    });

    custom_css_close.addEventListener("click", (event) => {
	custom_css_controller.style.display = "none";
    });

    custom_css_save.addEventListener("click", (event) => {
	localStorage.setItem("custom-css", custom_css_area.value);
	console.log(localStorage.getItem("custom-css"));
    });
    

    custom_js_button = document.getElementById("custom-js-button");
    custom_js_controller = document.getElementById("custom-js-controller");
    custom_js_close = document.getElementById("custom-js-close");
    custom_js_area = document.getElementById("custom-js-area");
    custom_js_save = document.getElementById("custom-js-close");

    custom_js_button.addEventListener("click", (event) => {
	custom_js_controller.style.display = "flex";
    });

    custom_js_close.addEventListener("click", (event) => {
	custom_js_controller.style.display = "none";
    });

    custom_js_save.addEventListener("click", (event) => {
	localStorage.setItem("custom-js", custom_js_area.value);
	console.log(localStorage.getItem("custom-js"));
    });
})();
