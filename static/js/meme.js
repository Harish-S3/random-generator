 document.addEventListener('DOMContentLoaded', function () {
            let prevMemeUrl = '';
    
            // Function to fetch a new meme from the server
            function getNewMeme() {
                fetch('/meme-generator')
                    .then(response => response.text())  // Use response.text() for HTML content
                    .then(data => {
                        const container = document.createElement('div');
                        container.innerHTML = data;
    
                        const memeContainer = document.getElementById('meme-container');
                        const newMeme = container.querySelector('.meme-container');
    
                        // Store the previous meme's URL before updating it
                        prevMemeUrl = memeContainer.querySelector('img').src;
    
                        // Update the 'meme-container' with the new meme HTML
                        memeContainer.innerHTML = newMeme.innerHTML;
                    })
                    .catch(error => console.error('Error fetching meme:', error));
            }
    
            // Attach the function to the button click event
            const getMemeButton = document.getElementById('get-meme-btn');
            getMemeButton.addEventListener('click', getNewMeme);
            getMemeButton.addEventListener('keydown', function(event) {
                if (event.key === 'Enter' || event.key === ' ') {
                    getNewMeme();
                }
            });
    
            // Attach click event to home button
            const homeButton = document.querySelector('.home-btn');
            homeButton.addEventListener('click', function () {
                window.location.href = "/";
            });
    
            // Function to go back to the previous meme
            function goToPrevMeme() {
                if (prevMemeUrl) {
                    const memeContainer = document.getElementById('meme-container');
                    memeContainer.innerHTML = `<img src="${prevMemeUrl}" alt="Previous Meme" class="meme-image">`;
                } else {
                    console.log('No previous meme available');
                }
            }
    
            // Attach the function to the button click event
            const prevMemeButton = document.getElementById('prev-meme-btn');
            prevMemeButton.addEventListener('click', goToPrevMeme);
            prevMemeButton.addEventListener('keydown', function(event) {
                if (event.key === 'Enter' || event.key === ' ') {
                    goToPrevMeme();
                }
            });
    
            // Initial fetch when the page loads
            getNewMeme();
            // Set interval for automatic update (e.g., every 15 seconds)
            setInterval(getNewMeme, 15000); // 15000 milliseconds = 15 seconds
        });