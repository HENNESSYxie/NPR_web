const myCheckbox = document.querySelector('#my-checkbox');
const table = document.getElementById('table');
const cameras = document.querySelector('.cameras');

myCheckbox.addEventListener('change', () => {
  if (myCheckbox.checked) {
    cameras.style.display = 'none';
    table.style.display = 'none';
  } else {
    cameras.style.display = 'flex';
    table.style.display = 'table';
  }
});