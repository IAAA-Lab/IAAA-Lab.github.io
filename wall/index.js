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

function updateTextFromURL() {
    const newtitle = unescape(window.location.hash.substring(1));
    if (newtitle != title) {
        title = newtitle;
        document.getElementById("text").value = title;
    }
}

function updateURLFromText() {
    const textarea = document.getElementById("text");
    const newText = textarea.value;
    if (newText !== title) {
        title = newText;
        window.location.hash = escape(newText);
    }
}

function currentTime() {
    // Title
    updateTextFromURL();

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

// Add event listener for textarea changes
document.getElementById("text").addEventListener("input", updateURLFromText);

// Countdown clock functionality
let targetTime = null;
let countdownInterval = null;

function validateTimeInput(hours, minutes, seconds) {
    return hours >= 0 && hours < 24 && minutes >= 0 && minutes < 60 && seconds >= 0 && seconds < 60;
}

function updateCountdown() {
    const countdownElement = document.getElementById("countdown");
    const countdownContainer = document.getElementById("countdown-container");
    
    if (!targetTime) {
        countdownElement.classList.add("hidden");
        return;
    }
    
    const now = new Date();
    const target = new Date();
    const [hours, minutes, seconds] = targetTime;
    
    target.setHours(hours, minutes, seconds, 0);
    
    if (target < now) {
        target.setDate(target.getDate() + 1);
    }
    
    const diff = target - now;
    const hoursLeft = Math.floor(diff / (1000 * 60 * 60));
    const minutesLeft = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const secondsLeft = Math.floor((diff % (1000 * 60)) / 1000);
    
    countdownElement.textContent = `${pad(hoursLeft)}:${pad(minutesLeft)}:${pad(secondsLeft)}`;
    countdownElement.classList.remove("hidden");
}

function handleTimeInput() {
    const inputs = document.querySelectorAll('.time-digit');
    const values = Array.from(inputs).map(input => {
        const value = input.value;
        return value === '' ? 0 : parseInt(value);
    });
    
    if (validateTimeInput(...values)) {
        targetTime = values;
        if (countdownInterval) clearInterval(countdownInterval);
        updateCountdown();
        countdownInterval = setInterval(updateCountdown, 1000);
    } else {
        targetTime = null;
        if (countdownInterval) clearInterval(countdownInterval);
        document.getElementById("countdown").textContent = "--:--:--";
    }
}

// Add event listeners to all time digit inputs
document.querySelectorAll('.time-digit').forEach((input, index) => {
    // Handle input changes
    input.addEventListener('input', (e) => {
        // Auto-advance to next input when two digits are entered
        if (e.target.value.length === 2 && index < 2) {
            document.querySelectorAll('.time-digit')[index + 1].focus();
        }
        handleTimeInput();
    });

    // Handle keydown events
    input.addEventListener('keydown', (e) => {
        // Handle Enter key
        if (e.key === 'Enter') {
            e.target.blur();
            return;
        }

        // Handle backspace
        if (e.key === 'Backspace' && e.target.value.length === 0 && index > 0) {
            document.querySelectorAll('.time-digit')[index - 1].focus();
        }
    });
});
