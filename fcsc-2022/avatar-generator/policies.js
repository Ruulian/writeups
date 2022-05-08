const RE_HEX_COLOR = /^#[0-9A-Fa-f]{6}$/i
const RE_INTEGER = /^\d+$/

function sanitizeHTML(html){
    return html
        .replace(/&/, "&amp;")
        .replace(/</, "&lt;")
        .replace(/>/, "&gt;")
        .replace(/"/, "&quot;")
        .replace(/'/, "&#039;")
}

let sanitizePolicy = TrustedTypes.createPolicy('default', {
    createHTML(html) {
        return sanitizeHTML(html)
    },
    createURL(url) {
        return url
    },
    createScriptURL(url) {
	return url
    }
})

let colorPolicy = TrustedTypes.createPolicy('color', {
    createHTML(color) {
        if (RE_HEX_COLOR.test(color)){
            return color
        }
        throw new TypeError(`Invalid color '${color}'`);
    }
})

let integerPolicy = TrustedTypes.createPolicy('integer', {
    createHTML(integer) {
        if (RE_INTEGER.test(integer)){
            return integer
        }
        throw new TypeError(`Invalid integer '${integer}'`);
    }
})
