
document.addEventListener('DOMContentLoaded', function() {
    const productElement = document.getElementById('iphone14');
    const detailsElement = document.getElementById('text');
    const sliderElement = document.getElementById('slider');

    if (productElement && detailsElement && sliderElement) {

        productElement.addEventListener('click', function() {

            detailsElement.classList.toggle('show-details');
            sliderElement.classList.toggle('show-details');
        });
    }
});