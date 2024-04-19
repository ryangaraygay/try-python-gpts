# try-python-gpts

This is to try out some code related GPTs from the ChatGPT store to see what they are capable of at a high level.

#### Note
- Even for exactly the same prompt, they might (likely) generate a different code/application example. The first time I tried the 2nd GPT it generated a file system watcher and notifier but I interrupted it so I decided to retry and generated a new app below.
- The prompt I used here is a conversation starter for the 2nd GPT whereas the 1st GPT has different conversation starters with some ```/<command>``` type hints. This may or may not give the former an advantage.

# 1) Code Copilot by promptspellsmith.com
- ranked #1 with 4.2 rating
- 600K+ chats as of writing
- created 11/6/23
- Code Smarter, Build Faster—With the Expertise of a 10x Programmer by Your Side.
- https://promptspellsmith.com/g/g-2DQzU5UZl

### Prompt: Please write an advanced example script to demonstrate your capabilities.
Certainly! Here's an advanced Python script that demonstrates the capabilities of a fictional AI-powered text summarization tool. This script uses machine learning models to preprocess text, extract keywords, and generate summaries. It incorporates error handling, file operations, and utilizes the spaCy library for linguistic processing.

### Python Script: AI-powered Text Summarization Tool
It generated some python code I placed in [codecopilot.py](codecopilot.py)

This script is an advanced example that combines text processing, keyword extraction, and summary generation using topic modeling. It uses the Natural Language Toolkit (`spaCy`) for preprocessing and the `sklearn` library for applying TF-IDF and NMF algorithms, showcasing a real-world application of AI in text analysis.

#### Generated code
See generated code in [codecopilot.py](codecopilot.py)

### ChatGPT short description of generated code/application
The Python application provided is designed for natural language processing and text analysis. It automates the process of reading text from a file, preprocessing it to remove stopwords and punctuation, and extracting key lemmatized tokens using spaCy. The application then uses the TF-IDF vectorization technique to identify the most significant words or keywords. Additionally, it employs Non-negative Matrix Factorization (NMF) for topic modeling to generate a concise summary of the text, highlighting the main themes by grouping related terms into topics. This program is useful for extracting insights and summarizing content from textual documents efficiently.

### Additional Actions
#### Needed to install packages
including some specificl spaCy language model to use
```
pip install scikit-learn
pip install spacy
python -m spacy download en_core_web_sm
```
#### input text file is [testinputfile.txt](testinputfile.txt)

### Run the app and Results
```
python codecopilot.py 
Enter the file path of the text document: testinputfile.txt
Keywords: ['young', 'year', 'world', 'wildlife', 'weight', 'way', 'water', 'warm', 'wane', 'walk']
Summary: fox turtle river water old riverbank way carry brown forest | bring life dog distant eyelid ripple thank unfold hi hill | turn decide voice sense dog merely sight lazy shadow peace | gentle turtle walk deep leap alongside resume lift dog continue | observe hello escape story scent local stir path trek life
```

#### Comment


# 2) Python by Nicholas Barker
- ranked #2 with 4.2 rating
- 700K+ chats as of writing
- created 12/7/23
- A highly sophisticated GPT tailored for advanced Python programmers focusing on efficient and high-quality production code.
- https://promptspellsmith.com/g/g-cKXjWStaE

### Prompt: Please write an advanced example script to demonstrate your capabilities.
Sure! Let's design a Python script that illustrates some advanced capabilities. I'll describe the scenario and then dive into the implementation details.

### Scenario: Real-time Data Stream Analysis

Imagine we need a Python script that can handle a stream of data in real-time. This script will perform the following tasks:

1. **Data Ingestion:** Continuously receive data points from a simulated sensor (e.g., temperature readings).
2. **Data Processing:** Apply a moving average filter to smooth out the data and detect significant changes.
3. **Alert Generation:** If the processed data shows a deviation greater than a specified threshold from the last known stable value, generate an alert.
4. **Logging:** Maintain logs for significant events and data points for later analysis.

### Components:

1. **Data Source Simulation:** For demonstration, we'll simulate the data source using a generator function that mimics sensor data.
2. **Moving Average Filter:** To smooth the incoming data stream.
3. **Change Detection:** Detects and logs when significant deviations occur.
4. **Logging:** Simple file or console logging of key events and data.

### Implementation Steps:

- **Simulated Data Source:** We'll use a generator to create pseudo-random data points.
- **Moving Average Filter:** This will use a deque from the `collections` module for efficient append and pop operations to maintain a window of the last 'n' readings.
- **Threshold Detection:** We'll implement logic to compare the current average against a threshold to detect significant changes.
- **Logging Mechanism:** For simplicity, we'll log events to the console, but this can be expanded to file logging.

Let's get started with the code implementation in the Python Code Interpreter. I'll write the core functions first, then put them together into the script. Let's head to the PCI to start coding this.

I've written the script with several advanced features, structured as follows:

1. **Data Source Simulation:** A generator function `data_source` produces random temperature-like data points, simulating a sensor's behavior.

2. **Moving Average Filter:** The `moving_average` function uses a deque for efficient data management, maintaining a window of the last 'n' readings to calculate a moving average.

3. **Change Detection:** The function `detect_change` compares the current average to the last stable value. If the difference exceeds a predefined threshold, it identifies this as a significant change.

4. **Logging:** Events are logged with timestamps, showing either regular updates or alerts when significant changes are detected.

This script combines data stream processing with real-time analytics and can be adapted for scenarios like IoT data monitoring or financial tick data analysis. The main function, `process_data_stream`, orchestrates these components. It initializes with the first data point and continuously processes incoming data to apply the moving average filter, detect significant changes, and log the results.

This example demonstrates handling real-time data, applying statistical methods, and using Python's built-in modules for performance-efficient computations.

Would you like to discuss any part of the script in more detail, or do you have any modifications or additional features in mind?

#### Generated code
See generated code in [python-gpt.py](python-gpt.py)

### ChatGPT short description of generated code/application
The provided Python script simulates real-time data processing for temperature readings using a moving average filter. It generates random temperature values around a mean of 20 with a standard deviation of 5, simulating sensor readings with a delay. A deque-based moving average is computed over a window of 10 values to smooth out the data. The script detects significant changes in the temperature average, defined as shifts exceeding a threshold of 5 units. When a significant change is detected, the script logs the event with the new average and updates the reference value. The program continuously logs the current average temperature, enabling monitoring of fluctuations over time. This script is ideal for environments where constant data stream processing and anomaly detection are required.

### Additional Actions
None

### Run the app and Results
```
python python-gpt.py 
2024-04-19 17:22:44 - Current average: 17.64
2024-04-19 17:22:45 - Current average: 18.35
2024-04-19 17:22:46 - Current average: 17.81
2024-04-19 17:22:47 - Current average: 17.85
2024-04-19 17:22:48 - Current average: 19.23
2024-04-19 17:22:49 - Current average: 20.91
....
2024-04-19 17:23:02 - Current average: 19.93
2024-04-19 17:23:03 - Current average: 21.21
2024-04-19 17:23:04 - Current average: 20.42
2024-04-19 17:23:05 - Current average: 20.58
2024-04-19 17:23:06 - Current average: 20.59
2024-04-19 17:23:07 - Current average: 20.86
2024-04-19 17:23:08 - Current average: 21.13
2024-04-19 17:23:09 - Current average: 21.10
2024-04-19 17:23:10 - Current average: 20.56
2024-04-19 17:23:11 - Current average: 21.19
2024-04-19 17:23:12 - Current average: 20.57
2024-04-19 17:23:13 - Current average: 19.20
^CTraceback (most recent call last):
  File "/workspaces/test-python-gpts/python-gpt.py", line 54, in <module>
    main()
  File "/workspaces/test-python-gpts/python-gpt.py", line 51, in main
    process_data_stream()
  File "/workspaces/test-python-gpts/python-gpt.py", line 40, in process_data_stream
    for data in data_gen:
  File "/workspaces/test-python-gpts/python-gpt.py", line 13, in data_source
    time.sleep(1)  # Simulate sensor delay
KeyboardInterrupt
```

### Comments
There was no way to gracefully stop so I interrupted the run.
