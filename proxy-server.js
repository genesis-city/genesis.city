const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();

const corsOptions = {
    origin: '*',
    methods: 'GET',
    allowedHeaders: 'Content-Type,Authorization',
};

app.use(cors(corsOptions));
app.use(express.json());

// Proxy endpoint
app.use('/proxy', async (req, res) => {
    try {
        const queryString = req.url.substring(1);

        const { data } = await axios.get(`https://places.decentraland.org/api/places?${queryString}`);

        res.json(data);
    } catch (error) {
        res.status(error.response ? error.response.status : 500);
        res.json(error.response ? error.response.data : {});
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`listening on ${PORT}`);
});
