    document.addEventListener('DOMContentLoaded', function () {
        const numFactsInput = document.getElementById('num-facts-input');
        const funFactContainer = document.getElementById('fun-fact-container');
        const getFunFactsBtn = document.getElementById('get-fun-fact-btn');

        const getFunFacts = async () => {
            try {
                const numFacts = numFactsInput.value || 1; // Default to 1 if input is empty
                const response = await fetch(`/api/fun-facts?num_facts=${numFacts}`);
                const data = await response.json();

                if (data && data.fun_facts) {
                    // Clear previous content
                    funFactContainer.innerHTML = '';

                    // Display each fun fact and its corresponding image
                    data.fun_facts.forEach((fact, index) => {
                        const factContainer = document.createElement('div');
                        factContainer.classList.add('fact-container');
                        factContainer.classList.add(index % 2 === 0 ? 'even' : 'odd'); // Alternate styles

                        // Create text container
                        const textContainer = document.createElement('div');
                        textContainer.classList.add('text-container');
                        textContainer.innerHTML = `<p>${fact.fun_fact}</p>`;

                        // Create image container
                        const imageContainer = document.createElement('div');
                        imageContainer.classList.add('image-container');
                        imageContainer.innerHTML = `<img src="data:image/jpeg;base64,${fact.image}" alt="${fact.fun_fact}">`;

                        // Append text and image containers to fact container
                        factContainer.appendChild(textContainer);
                        factContainer.appendChild(imageContainer);

                        // Append fact container to the main container
                        funFactContainer.appendChild(factContainer);
                    });
                } else {
                    console.error('Invalid or empty response:', data);
                }
            } catch (error) {
                console.error('Error fetching fun facts:', error);
            }
        };

        // Attach click event listener to the "Get Fun Facts" button
        getFunFactsBtn.addEventListener('click', getFunFacts);

        // Initial fetch when the page loads
        getFunFacts();
        setInterval( getFunFacts, 15000); // 10000 milliseconds = 10 seconds
    });