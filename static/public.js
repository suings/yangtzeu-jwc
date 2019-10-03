function setData(k, v) {
    // v需要为json类型或对象
    // sessionStorage.setItem(k, JSON.stringify(v))
    localStorage.setItem(k, JSON.stringify(v))
}
function getData(k) {
    // k = sessionStorage.getItem(k);
    k = localStorage.getItem(k);
    if (k) {
        k = JSON.parse(k);
        return k
    } else {
        // k=null
        return k;
    }
}


function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name) == 0) { return c.substring(name.length, c.length); }
    }
    return "";
}


function clearCookies() {
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
}
function clear() {
    clearCookies();
    sessionStorage.clear();
    // localStorage.clear();
    localStorage.removeItem("data")
}
function randomNum(minNum, maxNum) {
    // 返回范围内随机整数
    switch (arguments.length) {
        case 1:
            return parseInt(Math.random() * minNum + 1, 10);
            break;
        case 2:
            return parseInt(Math.random() * (maxNum - minNum + 1) + minNum, 10);
            break;
        default:
            return 0;
            break;
    }
}

function IsPC() {
    var userAgentInfo = navigator.userAgent;
    var Agents = new Array("Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod");
    var flag = true;
    for (var v = 0; v < Agents.length; v++) {
        if (userAgentInfo.indexOf(Agents[v]) > 0) { flag = false; break; }
    }
    return flag;
}

function getWeek() {
    let now = new Date();
    let begin = new Date("2019/09/01 17:40:00");
    let del = (now - begin)/(1000*60*60*24*7);
    return Math.ceil(del);
}