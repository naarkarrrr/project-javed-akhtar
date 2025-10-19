const chatbox = document.getElementById('chatbox');
const input = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');

sendBtn.addEventListener('click', async () => {
  const message = input.value;
  if (!message) return;
  
  appendMessage(`You: ${message}`);
  input.value = '';

  const reply = await sendMessage(message);
  appendMessage(`Javed Akhtar: ${reply}`);
});

function appendMessage(text) {
  const p = document.createElement('p');
  p.textContent = text;
  chatbox.appendChild(p);
}

async function sendMessage(message) {
  try {
    const res = await fetch('/.netlify/functions/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
    const data = await res.json();
    return data.reply;
  } catch (err) {
    console.error(err);
    return "Sorry, something went wrong!";
  }
}
