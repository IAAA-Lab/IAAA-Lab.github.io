themes = [
    'theme-orange',
    'theme-light',
    'theme-dark',
]
theme = -1
function switch_theme() {
    theme = (theme + 1) % themes.length
    document.documentElement.className = themes[theme]
}
switch_theme()
document.getElementById("logo").onclick = switch_theme

function pad(n){
    return (n < 10) ? "0" + n : n;
}

var title = '';
var date = '';

function currentTime() {


    // Title
    const newtitle = unescape(window.location.hash.substring(1))
    if (newtitle != title){
        title = newtitle
        document.getElementById("title").innerText = title

    }

    const dt = new Date();
    
    // Date
    var [dd, MM, yyyy] = [dt.getDate(), dt.getMonth(), dt.getFullYear()];
    const day = ['LUN','MAR','MIE','JUE','VIE','SAB','DOM'][dt.getDay()];

    [dd, MM] = [pad(dd), pad(MM)];
    const newdate = `${dd}/${MM}/${yyyy}`;

    if (newdate != date) {
        date = newdate;
        document.getElementById("date").innerText = date;
    } 

    // Hour
    var [hh, mm, ss] = [dt.getHours(), dt.getMinutes(), dt.getSeconds()];

    const session = (hh > 12) ? "PM" : "AM";
    hh = hh % 12;
    if (hh == 0) hh = 12;

    [hh, mm, ss] = [pad(hh), pad(mm), pad(ss)];
    const time = `${hh}:${mm}:${ss} ${session}`;

    document.getElementById("time").innerText = time;
    const t = setTimeout(function(){ currentTime() }, 1000);
}
currentTime();
