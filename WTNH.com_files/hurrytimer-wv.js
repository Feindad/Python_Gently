var headlines = document.querySelectorAll('.hurrytimer-headline');

/**  
 * Checks if a hurrytimer headline has more than one line by measuring the height,
 * if so, hides the subheadline.
 */
var headlineObserver = new ResizeObserver(function(entries) {
    entries.forEach(function(entry) {
        var subHeadline = entry.target.parentNode.querySelector('.hurrytimer-content');
        var height = Math.floor(entry.contentRect.height);

        subHeadline.style.display = height > 40 ? 'none' : 'block';
    });
});

// If there are hurrytimer headlines in the page, observe each one of them.
if(headlines){
    headlines.forEach(function(headline){
        headlineObserver.observe(headline);
    });
}

