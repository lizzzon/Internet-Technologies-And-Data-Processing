const sliderWrapper = document.querySelector('.slider-wrapper');
const sliderPrev = document.querySelector('.slider-prev');
const sliderNext = document.querySelector('.slider-next');
const sliderItems = document.querySelectorAll('.slider-item');
const sliderItemWidth = sliderItems[0].offsetWidth;

let currentIndex = 0;
console.log(sliderItems);
sliderPrev.addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
    sliderWrapper.style.transform = `translateX(-${currentIndex * (sliderItemWidth + 50)}px)`;
  }
});

sliderNext.addEventListener('click', () => {
  if (currentIndex < sliderItems.length - 3) {
    currentIndex++;
    sliderWrapper.style.transform = `translateX(-${currentIndex * (sliderItemWidth + 50)}px)`;
  }
});
