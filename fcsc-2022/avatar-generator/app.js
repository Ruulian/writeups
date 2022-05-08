let currentSeed = 0
let currentPrimaryColor = ""
let currentSecondaryColor = ""

let shareText = 'My new avatar created with Avatar-Generator 😀'
let shareHashtag = 'CTF,FCSC2022'

function randomSeed(){
    return Math.floor(Math.random() * 1000000);
}

function makePRNG(seed){
    return function(){
        var x = Math.sin(seed++) * 10000
        return x - Math.floor(x)
    }
}

function getURLParams(){
    let url = new URL(window.location.href)
    return url.searchParams
}

function updateSettings(seed, primaryColor, secondaryColor){
    currentSeed = seed
    currentPrimaryColor = primaryColor
    currentSecondaryColor = secondaryColor
    document.getElementById('seed').innerHTML = integerPolicy.createHTML(currentSeed)
    document.getElementById('primaryColor').innerHTML = colorPolicy.createHTML(currentPrimaryColor)
    document.getElementById('secondaryColor').innerHTML = colorPolicy.createHTML(currentSecondaryColor)
    document.getElementById('topColor').style.backgroundColor = currentPrimaryColor
    let notyf = new Notyf()
    notyf.confirm('New avatar generated!')
}

function generateAvatar(seed, primaryColor, secondaryColor){
    let options = new minBlock({
        canvasID: 'avatar',
        color: {
            primary: primaryColor,
            secondary:  secondaryColor
        },
        random: makePRNG(seed)
    })
    updateSettings(seed, options.color.primary, options.color.secondary)
}

function generateRandomAvatar(){
    generateAvatar(randomSeed(), null, null)
}

function makeAvatarUrl(){
    let baseUrl = document.location.href.split('?')[0]
    let primary = encodeURIComponent(currentPrimaryColor)
    let secondary = encodeURIComponent(currentSecondaryColor)
    return escape(`${baseUrl}?seed=${currentSeed}&primary=${primary}&secondary=${secondary}`)
}

function shareAvatar(){
    link = 'https://twitter.com/share?text=' + shareText + '&url=' + makeAvatarUrl() + '&hashtags=' + shareHashtag
    window.open(link, '_blank').focus();
}

document.addEventListener('DOMContentLoaded', function(){
    debug = false
    if (window.location.hash.substr(1) == 'debug'){
        debug = true
    }
    try {
        params = getURLParams()
        let seed = params.get('seed') === null ? randomSeed() : params.get('seed')
        let primaryColor = params.get('primary')
        let secondaryColor = params.get('secondary')
        generateAvatar(seed, primaryColor, secondaryColor)
    }
    catch(error){
        if (debug) {
	    let errorMessage = "Error! An error occured while loading the page... Details: " + error
	    document.querySelector('.container').innerHTML = errorMessage
        }
        else {
            generateRandomAvatar()
        }
    }

    document.getElementById('randomAvatar').addEventListener('click', generateRandomAvatar)
    document.getElementById('shareAvatar').addEventListener('click', shareAvatar)
})