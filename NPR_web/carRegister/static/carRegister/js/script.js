const myCheckbox = document.querySelector('#my-checkbox');
const cameras = document.querySelector('.cameras');

myCheckbox.addEventListener('change', () => {
  if (myCheckbox.checked) {
    cameras.style.display = 'none';
  } else {
    cameras.style.display = 'flex';
  }
});