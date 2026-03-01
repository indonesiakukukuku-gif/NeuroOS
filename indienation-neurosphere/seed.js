const mongoose = require('mongoose');

// Ganti <PASSWORD> dengan password MongoDB Atlas Anda
const URI = process.env.MONGODB_URI;

mongoose.connect(URI)
  .then(() => {
    console.log("NEUROSPHERE: Connected to Core Memory.");
    const CitizenSchema = new mongoose.Schema({
      iid: String,
      founder_alias: String,
      status: String,
      anchor_value: Number,
      currency: String,
      joined_at: Date,
      relay_status: Object
    });

    const Citizen = mongoose.model('Citizen', CitizenSchema);

    const newFounder = new Citizen({
      iid: "IID-021-000001",
      founder_alias: "INDIE-Founder",
      status: "Active",
      anchor_value: 100000,
      currency: "EUR",
      joined_at: new Date("2026-02-26T07:49:39Z"),
      relay_status: { step_1: 1000, step_2: 270, step_3: 990 }
    });

    return newFounder.save();
  })
  .then(() => {
    console.log("SUCCESS: IID INDIE-Founder has been anchored to MongoDB.");
    process.exit();
  })
  .catch(err => {
    console.error("ERROR: SEC-04 Stabilization failed.", err);
    process.exit(1);
  });
