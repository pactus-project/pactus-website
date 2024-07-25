import lottie from "lottie-web";
import { defineElement } from "@lordicon/element";


defineElement(lottie.loadAnimation);

$(document).ready(function () {
    $('pre').css({
        'background-color': '#000',
        'color': '#f9fafb',
        'padding': '1.3rem',
        'border-radius': '0.5rem',
        'overflow': 'auto',
        'font-size': '1rem',
        'line-height': '1.5rem',
        'margin-bottom': '1rem',
        "border-radius": "20px",
        "border": "1px solid #747474"
    });

    $('code').css({
        'background-color': 'inherit',
        'color': 'inherit',
        'font-family': 'monospace, monospace'
    });

    const copybtn = `<div style="background: #0F6CBD" class="p-1 place-items-center flex rounded-lg"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-3M8 7V5a2 2 0 012-2h5a2 2 0 012 2v3M8 7h8a2 2 0 012 2v8"></path></svg> Copy</div>`
    $('pre').each(function() {
        var copyButton = $('<button>')
          .addClass('absolute top-2  right-2 bg-gray-800 text-white p-1 rounded opacity-0 group-hover:opacity-100 copy-button')
          .html(copybtn)
          .click(function() {
            var code = $(this).siblings('code').text();
            code = code.replace(/^"|"$/g, '');
            navigator.clipboard.writeText(code).then(() => {
              $(this).html('<div style="background: #0F6CBD " class="flex p-1 place-items-center rounded-lg"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Copied</div>');
              setTimeout(() => {
                $(this).html(copybtn);
              }, 1000);
            }, function(err) {
              console.error('Could not copy text: ', err);
            });
          });
    
        $(this).append(copyButton);
      });
    
      $('pre').addClass('relative group bg-gray-900 text-white p-4 rounded');
      $('code').addClass('bg-gray-900 text-white');
});
