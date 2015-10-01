// A no-dependancy quick and dirty method of adding basic
// placeholder functionality to Internet Explorer 5.5+
// Author: Jay Williams <myd3.com>
// License: MIT License
// Link: https://gist.github.com/1105055

function add_placeholder (el, placeholder)
{
//	var el = document.getElementById(id);
	el.placeholder = placeholder;

    el.onfocus = function ()
    {
		if(this.value == this.placeholder)
		{
			this.value = '';
			el.style.cssText  = '';
		}
    };

    el.onblur = function ()
    {
		if(this.value.length == 0)
		{
			this.value = this.placeholder;
			el.style.cssText = 'color:#A9A9A9;';
		}
    };

	el.onblur();
}


$(document).ready(function() {
    $("input").each(function() {
        add_placeholder($(this), $(this).attr('placeholder'));
    })
});