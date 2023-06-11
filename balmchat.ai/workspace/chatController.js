const Therapist = require('./therapist');

const therapist = new Therapist();

exports.processMessage = (req, res) => {
  const message = req.body.message;
  const response = therapist.getResponse(message);
  res.json({ response });
};
