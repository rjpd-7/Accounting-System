document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu');
    const sidebar = document.querySelector('.sidebar');

    menuToggle.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent page jump
        sidebar.classList.toggle('collapsed');
        
        // Optional: toggle icon direction
        const icon = menuToggle.querySelector('i');
        if (sidebar.classList.contains('collapsed')) {
            icon.classList.remove('bi-arrow-left-circle');
            icon.classList.add('bi-arrow-right-circle');
        } else {
            icon.classList.remove('bi-arrow-right-circle');
            icon.classList.add('bi-arrow-left-circle');
        }
    });
});