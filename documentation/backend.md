### FASTAPI BACKEND: How to run the backend and test the sample?

1. **app.py** file includes API of chat_response from model

2. Run command in terminal```uvicorn app:app --reload ```

3. Go to this given [page](http://127.0.0.1:8000/docs) which includes Swagger UI documentation

4. Test the sample input as below
    ```json
    {
        "message": "How much is BTech fee?" // Virat Kohli or any outside will not be processed
    }
    ```

5. Result will be something like this
    ```json
    {
        "response": "The tuition fee is approximately ₹50,000 per year."
    }
    ```