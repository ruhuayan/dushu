export const debounced = function (func, timeout = 100) {
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(function () { func.apply(this, args); }, timeout);
    };
}