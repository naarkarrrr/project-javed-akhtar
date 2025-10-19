import fetch from 'node-fetch';

export async function handler(event, context) {
  const body = JSON.parse(event.body);
  const userMessage = body.message;

  const response = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${process.env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: userMessage }]
    })
  });

  const data = await response.json();
  const reply = data.choices[0].message.content;

  return {
    statusCode: 200,
    body: JSON.stringify({ reply })
  };
}
