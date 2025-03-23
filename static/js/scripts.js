document.addEventListener('DOMContentLoaded', () => {
    const triggers = document.querySelectorAll('.tab-trigger');
    const contents = document.querySelectorAll('.tab-content');

    triggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            triggers.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            trigger.classList.add('active');
            const targetContent = document.getElementById(trigger.dataset.tab);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });
});