var debounce = function(fn, t) {
    let ctr = null;
    return function(...args) {
        if (ctr) clearTimeout(ctr);
        ctr = setTimeout(() => fn(...args), t);
    }
};