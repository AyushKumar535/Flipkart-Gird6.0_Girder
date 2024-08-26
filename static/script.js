document.getElementById('predictButton').addEventListener('click', function () {
    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);
    const waist = parseFloat(document.getElementById('waist').value);
    const hip = parseFloat(document.getElementById('hip').value);
    const bust = parseFloat(document.getElementById('bust').value);
    const gender = document.getElementById('gender').value;
    const Cup_Size = document.getElementById('cupsize').value;

    const requestData = {
        height: height,
        weight: weight,
        waist: waist,
        hip: hip,
        bust: bust,
        gender: gender,
        Cup_Size: Cup_Size
    };
    console.log(requestData)
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(`Error: ${data.error}`);
        } else {
            alert(`Predicted Size: ${data.size}`);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while predicting the size.');
    });
});
