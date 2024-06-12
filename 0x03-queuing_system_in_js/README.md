# Redis Queuing System in JavaScript

This project demonstrates how to use Redis with Node.js for various operations including basic operations, asynchronous operations, advanced operations, and using a queue system with Kue. It also includes building a basic Express app that interacts with a Redis server.

## Installation

### Install Redis

1. **Install Redis:**

    ```sh
    sudo apt-get update
    sudo apt-get install redis-server
    ```

2. **Start Redis in the background:**

    ```sh
    /usr/bin/redis-server &
    ```

3. **Verify Redis is running:**

    ```sh
    redis-cli ping
    # Expected output: PONG
    ```

4. **Set and get a key-value pair:**

    ```sh
    redis-cli set Holberton School
    # Expected output: OK

    redis-cli get Holberton
    # Expected output: "School"
    ```

5. **Kill the Redis server:**

    ```sh
    ps aux | grep redis-server
    kill [PID_OF_Redis_Server]
    ```

6. **Copy `dump.rdb` to the project directory:**

    ```sh
    sudo cp /var/lib/redis/dump.rdb ~/alx-backend/0x03-queuing_system_in_js/
    ```

### Setting Up Your Project

1. **Clone the project repository:**

    ```sh
    git clone <repository-url>
    cd 0x03-queuing_system_in_js
    ```

2. **Install Node.js dependencies:**

    ```sh
    npm install
    ```

## Running the Application

1. **Run basic Redis operations:**

    ```sh
    node 1-redis_op.js
    ```

2. **Run asynchronous Redis operations:**

    ```sh
    node 2-redis_op_async.js
    ```

3. **Run advanced Redis operations:**

    ```sh
    node 4-redis_advanced_op.js
    ```

4. **Start the subscriber:**

    ```sh
    node 5-subscriber.js
    ```

5. **Publish a message:**

    ```sh
    node 5-publisher.js
    ```

6. **Create a job:**

    ```sh
    node 6-job_creator.js
    ```

7. **Process jobs:**

    ```sh
    node 6-job_processor.js
    ```

8. **Run the Express app:**

    ```sh
    node 9-stock.js
    ```

## Testing

Run the tests using Mocha:

```sh
npm test
