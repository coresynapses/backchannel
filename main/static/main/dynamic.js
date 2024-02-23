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
})();
