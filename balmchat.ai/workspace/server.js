const express = require('express');
const cors = require('cors');
const chatController = require('./chatController');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/chat', chatController.processMessage);

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
