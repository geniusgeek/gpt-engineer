import React, { useState } from 'react';
import Message from './Message';
import './Chat.css';

function Chat({ messages, addMessage }) {
  const [input, setInput] = useState('');

  const sendMessage = async (e) => {
    e.preventDefault();

    if (input.trim() === '') {
      // Handle empty input, display an error message, or prevent sending the request
      return;
    }

    addMessage({ sender: 'user', content: input });
    setInput('');

    try {
      const response = await fetch('https://geniusgeek-shiny-funicular-456xgqxvg6h7x5w-3003.preview.app.github.dev/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });

      if (!response.ok) {
        throw new Error('Failed to send message.');
      }

      const data = await response.json();
      addMessage({ sender: 'therapist', content: data.response });
    } catch (error) {
      console.error(error);
      // Handle the error, display an error message, or perform any necessary actions
    }
  };

  return (
    <div className="Chat">
      <div className="messages">
        {messages.map((message, index) => (
          <Message key={index} message={message} />
        ))}
      </div>
      <form onSubmit={sendMessage}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default Chat;
