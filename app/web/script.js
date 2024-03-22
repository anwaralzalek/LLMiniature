function generateCode() {
    const description = document.getElementById("problemDescription").value;

    fetch('/generate_code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description: description })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("codeOutput").textContent = data.code;
        });
}

document.getElementById('likeButton').addEventListener('click', function() {
    sendFeedback('like');
});

document.getElementById('dislikeButton').addEventListener('click', function() {
    sendFeedback('dislike');
});

function sendFeedback(feedback) {
    fetch('/submit_feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ feedback: feedback })
    })
        .then(response => response.json());
}