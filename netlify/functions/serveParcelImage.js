const https = require('https');

exports.handler = async function(event, context) {
  const path = event.path;
  const imageName = path.split('/').pop();
  
  // Construct the GitHub raw content URL for the 'parcels' repository
  const imageUrl = `https://media.githubusercontent.com/media/genesis-city/parcels/master/api/v1/land/${imageName}`;

  try {
    // Fetch the image from GitHub
    const imageBuffer = await fetchImage(imageUrl);

    // Return the image with appropriate headers
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'image/jpeg',
        'Cache-Control': 'public, max-age=31536000' // Cache for 1 year
      },
      body: imageBuffer.toString('base64'),
      isBase64Encoded: true
    };
  } catch (error) {
    return {
      statusCode: 404,
      body: JSON.stringify({ message: 'Image not found' })
    };
  }
};

function fetchImage(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch image: ${response.statusCode}`));
        return;
      }

      const data = [];
      response.on('data', (chunk) => data.push(chunk));
      response.on('end', () => resolve(Buffer.concat(data)));
    }).on('error', reject);
  });
}