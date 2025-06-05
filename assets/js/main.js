import lottie from "lottie-web";
import { defineElement } from "@lordicon/element";


defineElement(lottie.loadAnimation);

$(document).ready(function () {
    const copy_btn = `<div style="background: #0F6CBD; height: 32px;" class="flex text-sm p-1 place-items-center rounded-lg"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-3M8 7V5a2 2 0 012-2h5a2 2 0 012 2v3M8 7h8a2 2 0 012 2v8"></path></svg> Copy</div>`
    $('pre').each(function() {
        var copyButton = $('<button>')
          .addClass('absolute top-2  right-2 bg-gray-800 text-white p-1 rounded opacity-0 group-hover:opacity-100 copy-button')
          .html(copy_btn)
          .click(function() {
            var code = $(this).parent().text().slice(0, -5);
            navigator.clipboard.writeText(code).then(() => {
              $(this).html('<div style="background: #0F6CBD; height: 32px;" class="flex text-sm p-1 place-items-center rounded-lg"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Copied</div>');
              setTimeout(() => {
                $(this).html(copy_btn);
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
