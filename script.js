// Navigation to Form Page
document.addEventListener('DOMContentLoaded', () => {
    const getStartedButton = document.querySelector('.btn');
    if (getStartedButton) {
        getStartedButton.addEventListener('click', () => {
            document.querySelector('.landing-page').style.display = 'none';
            document.querySelector('.form-container').style.display = 'flex';
        });
    }
});

// Predict Energy Function
async function predictEnergy() {
    const formData = {
        X1: document.getElementById('X1').value,
        X2: document.getElementById('X2').value,
        X3: document.getElementById('X3').value,
        X4: document.getElementById('X4').value,
        X5: document.getElementById('X5').value,
        X6: document.getElementById('X6').value,
        X7: document.getElementById('X7').value,
        X8: document.getElementById('X8').value
    };

    try {
        // Validate inputs
        for (let key in formData) {
            if (formData[key] === "") {
                alert(`Please fill in all fields! Missing: ${key}`);
                return;
            }
        }

        // Simulated API Call
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            throw new Error(`Failed to fetch: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById('results').innerHTML = `
            <p>Heating Load: ${result['Heating Load (Y1)']} kW</p>
            <p>Cooling Load: ${result['Cooling Load (Y2)']} kW</p>
        `;
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to get prediction. Check console for details.');
    }
}
