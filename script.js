/* static/js/script.js */
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
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            throw new Error('Prediction failed');
        }
        
        const result = await response.json();
        document.getElementById('heatingResult').innerText = `Heating Load: ${result['Heating Load (Y1)']}`;
        document.getElementById('coolingResult').innerText = `Cooling Load: ${result['Cooling Load (Y2)']}`;
    } catch (error) {
        console.error('Error:', error);
        alert('Prediction failed. Please check your input values.');
    }
}
