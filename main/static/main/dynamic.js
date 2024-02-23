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

})();
