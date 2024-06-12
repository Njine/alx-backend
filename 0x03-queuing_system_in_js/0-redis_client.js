#!/usr/bin/yarn dev

import { createClient } from 'redis';

// Creating a Redis client instance
const client = createClient();

// Event handler for error events - logs an error message when connection fails
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Event handler for connect events - logs a success message when connection is established
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
