console.log('background running');

chrome.runtime.onMessage.addListener(receiver);

window.word = "coding train";

function receiver(request, sender, sendResponse) {
  word = request.text;
  console.log(word);
}