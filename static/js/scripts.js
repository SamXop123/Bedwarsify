document.addEventListener('DOMContentLoaded', () => {
    const triggers = document.querySelectorAll('.tab-trigger');
    const contents = document.querySelectorAll('.tab-content');

    triggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            triggers.forEach(t => t.classList.remove('active:bg-primary', 'active:text-primary-foreground'));
            contents.forEach(c => c.classList.add('hidden'));

            trigger.classList.add('active:bg-primary', 'active:text-primary-foreground');
            document.getElementById(trigger.dataset.tab).classList.remove('hidden');
        });
    });
});