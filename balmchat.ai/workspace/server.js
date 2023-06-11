const express = require('express');
const cors = require('cors');
const chatController = require('./chatController');

const app = express();

app.use(cors({
  origin: 'https://geniusgeek-shiny-funicular-456xgqxvg6h7x5w-3000.preview.app.github.dev/' // Replace with the appropriate frontend URL
}));
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello, World!'); // Replace with your desired response
});

app.post('/api/chat', chatController.processMessage);

const PORT = process.env.PORT || 3003; // Change to a different port number
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
