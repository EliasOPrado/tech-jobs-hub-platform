document.addEventListener('DOMContentLoaded', function (event) {
    // array with texts to type in typewriter
    var dataText = [
      "Discover top talent effortlessly.", 
      "Your dream job, one click away.", 
      "Elevate your team seamlessly.", 
      "Your dream career, simplified.",
      "Your dream career, simplified.",
      "Recruit smarter, not harder.",
      "Tech Jobs: Your platform for hiring and apply for new opportunities."
    ];

    // type one text in the typewriter
    // keeps calling itself until the text is finished
    function typeWriter(text, i, fnCallback) {
      // check if text isn't finished yet
      if (i < text.length - 1) { // Fix: Use text.length - 1
        // add the next character to h1
        document.getElementById("text-container").innerHTML = text.substring(0, i + 1) + '<span aria-hidden="true"></span>';

        // wait for a while and call this function again for the next character
        setTimeout(function () {
          typeWriter(text, i + 1, fnCallback)
        }, 100);
      }
      // text finished, call callback if there is a callback function
      else if (typeof fnCallback == 'function') {
        // call the callback after a timeout
        setTimeout(fnCallback, 1000);
      }
    }

    // start a typewriter animation for a text in the dataText array
    function startTextAnimation(i) {
      if (typeof dataText[i] == 'undefined') {
        setTimeout(function () {
          startTextAnimation(0);
        }, 20000);
      }
      // check if dataText[i] exists
      if (i < dataText.length) { // Fix: Use dataText.length
        // text exists! start typewriter animation
        typeWriter(dataText[i], 0, function () {
          // after the callback (and the whole text has been animated), start the next text
          startTextAnimation(i + 1);
        });
      }
    }

    // start the text animation
    startTextAnimation(0);
  });