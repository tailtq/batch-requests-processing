# Batch requests processing Demo

## Approach 1

Assume we have a server to capture multiple requests and we want to handle them at the same time. We push these requests to a queue (Redis) and make them wait for a limited time. Workers running in different processes will get the items from the queue, handle them, and respond back to the server by using the uuid in the item. (This one was recommended by my colleague)

## Approach 2
