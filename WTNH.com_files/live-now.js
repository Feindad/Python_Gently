const homeUrl = live_now_script_object.homeUrl;
const templateVariablesUrl = homeUrl + '/wp-json/lakana/v1/template-variables/';
const liveAlertType = document.querySelector('.site-header__live-button.watch-now') ? 'watchnow' : 'livenow';

/*
* Rotate to the next live alert every 5 seconds.
*/
function rotateLiveAlerts(liveNowAlerts) {
    const liveNowLink = document.querySelector('.site-header__live-button-desktop a');
    const liveNowContent = document.querySelector('.site-header__live-button-desktop .site-header__live-button-description span');
    let currentAlertPosition = 1;

    if(liveNowLink && liveNowAlerts.length > 1) {
        setInterval( function() {
            liveNowLink.href = liveNowAlerts[currentAlertPosition].url;
            liveNowContent.textContent = liveNowAlerts[currentAlertPosition].content_truncated;
            liveNowContent.setAttribute('title', liveNowAlerts[currentAlertPosition].content);
            currentAlertPosition += 1;

            if(currentAlertPosition >= liveNowAlerts.length){
                currentAlertPosition = 0;
            }
       }, 5000);
    }
}

/*
* Load the live alerts to be shown in the live now button.
*/
function loadLiveAlerts() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        const response = JSON.parse(this.response);
        let liveNowAlerts = [];
        liveNowAlerts = ('watchnow' === liveAlertType) ? response.watch_now_btn : response.live_now_btn;
        rotateLiveAlerts(liveNowAlerts);
    }
    xhttp.open("GET", templateVariablesUrl, true);
    xhttp.send();
  }

loadLiveAlerts();
