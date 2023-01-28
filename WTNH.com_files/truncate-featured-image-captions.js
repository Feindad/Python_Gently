const featuredImageCaption = document.getElementById("featured-image-caption");
const featuredImageCaptionOriginal = document.getElementById(
  "featured-image-caption-original"
);
const featuredImageCaption2 = document.getElementById("featured-image-caption-2");
const featuredImageCaptionOriginal2 = document.getElementById(
  "featured-image-caption-original-2"
);

if ( featuredImageCaption ) {

  if ( document?.getElementById("caption-read-more-button") ) {
    document.getElementById("caption-read-more-button").onclick = function truncate() {
      featuredImageCaption.style.display = "none";
      featuredImageCaptionOriginal.style.display = "block";
    };
  }

  if ( document?.getElementById("caption-original-read-more-button") ) {
    document.getElementById("caption-original-read-more-button").onclick =
      function truncate() {
        featuredImageCaption.style.display = "block";
        featuredImageCaptionOriginal.style.display = "none";
      };
  }

  if ( document?.getElementById("caption-read-more-button-2") ) {
    document.getElementById("caption-read-more-button-2").onclick = function truncate() {
      featuredImageCaption2.style.display = "none";
      featuredImageCaptionOriginal2.style.display = "block";
    };
  }

  if ( document?.getElementById("caption-original-read-more-button-2") ) {
    document.getElementById("caption-original-read-more-button-2").onclick =
      function truncate() {
        featuredImageCaption2.style.display = "block";
        featuredImageCaptionOriginal2.style.display = "none";
      };
  }
}
