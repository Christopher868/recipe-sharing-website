// JavaScript for editing print formatted recipe page
document.addEventListener('DOMContentLoaded', function () {
    const btns = document.querySelectorAll('.option-btn');
    const picture = document.querySelector('#picture');
    const equipment = document.querySelector('#equipment');
    const text = document.querySelector('#text'); 
    const image = document.querySelector('.recipe-image');
    const equipment_section = document.querySelector('#equipment-section');
    const text_size = document.querySelectorAll('.recipe-instructions li');

    btns.forEach(btn => {
        btn.addEventListener('click', () => {  
            if (btn === picture) {
                 image.style.display = image.style.display === 'none' ? 'block' : 'none';
            } else if (btn === equipment) {
                    equipment_section.style.display = equipment_section.style.display === 'none' ? 'flex' : 'none';
            } else if (btn === text) {
                    text.textContent = text.textContent === 'Text Size: Large' ? 'Text Size: Small' : 'Text Size: Large';
                    text_size.forEach(item => {
                        item.style.fontSize = item.style.fontSize === '20px' ? '16px' : '20px';
                    });
            }

        });
    });


})