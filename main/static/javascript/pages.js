function SetBlocks() {
  var blocks = document.getElementsByClassName('segment-block');
  for (var i = 0; i < blocks.length; i++) {
    blocks[i].style.width = document.documentElement.clientWidth + "px";
    blocks[i].style.height = document.documentElement.clientHeight + "px";
  }
}
SetBlocks();
