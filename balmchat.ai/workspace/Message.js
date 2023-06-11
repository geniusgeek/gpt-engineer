import React from 'react';
import './Message.css';

function Message({ message }) {
  return (
    <div className={`Message ${message.sender}`}>
      <p>{message.content}</p>
    </div>
  );
}

export default Message;
