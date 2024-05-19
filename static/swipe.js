let startX;

document.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
});

document.addEventListener('touchend', (e) => {
    const endX = e.changedTouches[0].clientX;
    const deltaX = startX - endX; // Change this line to calculate the difference correctly

    // Adjust the threshold as needed
    const swipeThreshold = 50;

    if (deltaX > swipeThreshold) {
        // Left swipe detected
         location.reload(true);
        // Add your logic or function call here
    }
});
