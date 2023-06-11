import React, { useState } from 'react';
import Chat from './Chat';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);

  const addMessage = (message) => {
    setMessages([...messages, message]);
  };

  return (
    <div className="App">
      <Chat messages={messages} addMessage={addMessage} />
    </div>
  );
}

export default App;
