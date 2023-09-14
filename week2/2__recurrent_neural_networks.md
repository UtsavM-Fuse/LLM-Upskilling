# 2. Recurrent Neural Networks

## 2.1 Understanding RNN Input-Output Relationships

  

Recurrent Neural Networks (RNNs) are a class of artificial neural networks well-suited for handling sequential data. One of their key strengths is their flexibility in managing different input and output relationships. Here are some common configurations:

![](https://t9007106573.p.clickup-attachments.com/t9007106573/49e2c949-54f7-4ed0-b902-1c8cfa6d50df/Screenshot%202023-09-14%20at%2010.37.58%20AM.png)

  

### 2.1.1. **One-to-One (1:1) RNN**:

*   **Description**: In the simplest configuration, an RNN operates on a one-to-one basis, where there is a one-to-one correspondence between input and output elements. This is similar to a traditional feedforward neural network.
*   **Example Tasks**:
    *   **Image Classification**: When classifying individual images, such as recognizing handwritten digits in the MNIST dataset, a 1:1 RNN can be used. Each image is treated as a separate input.
    *   **Non-sequential Data**: For non-sequential data, like tabular data, a 1:1 RNN can process each row independently for tasks such as fraud detection.

  

### 2.1.2. **One-to-Many (1:N) RNN**:

*   **Description**: In a one-to-many configuration, the RNN takes a single input and produces a sequence of outputs.
*   **Example Tasks**:
    *   **Image Captioning**: Given an image, an RNN can generate a descriptive sentence or a sequence of words describing the image.
    *   **Music Generation**: With a single seed note or chord, an RNN can generate an entire piece of music as a sequence.

  

### 2.1.3. **Many-to-One (N:1) RNN**:

*   **Description**: In a many-to-one setup, the RNN takes a sequence of inputs and produces a single output.
*   **Example Tasks**:
    *   **Sentiment Analysis**: Analyzing a sequence of words (e.g., a movie review) to determine its sentiment (positive, negative, or neutral).
    *   **Gesture Recognition**: Processing a time series of sensor data from a motion sensor to classify a gesture as a particular action.

  

### 2.1.4. **Many-to-Many (Seq2Seq style) RNN**:

*   **Description**: This architecture combines two RNNs, an encoder and a decoder. The encoder processes a sequence of inputs, and the decoder generates a sequence of outputs.
*   **Example Tasks**:
    *   **Neural Machine Translation**: The encoder processes the source language, and the decoder generates the target language, enabling translation between languages.
    *   **Chatbots**: Encoding user queries with the encoder and decoding with relevant responses using the decoder.

  

### 2.1.5. **Many-to-Many (N:N) RNN**:

*   **Description**: A many-to-many RNN receives a sequence of inputs and produces a sequence of outputs. Both input and output sequences can have different lengths.
*   **Example Tasks**:
    *   **Video Action Recognition**: Analyzing a video frame by frame to identify actions or activities happening over a sequence of frames.

  

## 2.2 Character Level Language Models

![](https://t9007106573.p.clickup-attachments.com/t9007106573/c6a60b81-acc7-4acf-b70a-1194254dbc27/Screenshot%202023-09-14%20at%2010.53.45%20AM.png)

Character-level language models using RNNs predict the next character in a sequence. They encode characters, employ RNN architecture with a hidden state for context, and use backpropagation to learn. At test time, they sample characters based on predicted probabilities, allowing text generation one character at a time. These models find applications in generating text, creative writing, and more.

  

## 2.3 LSTM

Reference: [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

  

### **2.3.1 The Long-term Dependency Problem:**

In some cases, like predicting the next word in a sentence, recent information suffices. For instance, "The cat is on the" strongly suggests the next word is "mat".

However, for more complex tasks like discerning the language in "I grew up in **France** … I speak fluent" we need context from further back.

  

### **2.3.2 LSTM Networks**

**LSTM Overview**: LSTMs mitigate the long-term dependency problem by having a more sophisticated structure than standard RNNs.

**Components**: LSTMs consist of the cell state, forget gate, input gate, and output gate.

![](https://t9007106573.p.clickup-attachments.com/t9007106573/097bc91c-2de6-413c-9b10-4c6b937e83e8/Screenshot%202023-09-14%20at%2012.07.26%20PM.png)

![](https://t9007106573.p.clickup-attachments.com/t9007106573/7fbf5631-532e-4736-9119-8caf9326ad01/Screenshot%202023-09-14%20at%2012.07.36%20PM.png)

  

**Understanding Gates**: (Gates as controllers) Gates in LSTMs act as controllers, deciding what information to keep, update, or discard. These gates are influenced by sigmoid functions, which output values between 0 and 1.

  

### **2.3.3. Step-by-Step LSTM Walk Through**

**2.3.3.1 Forget Gate**: The forget gate evaluates what information from the cell state should be discarded based on the previous hidden state and current input.

![](https://t9007106573.p.clickup-attachments.com/t9007106573/aef1dab6-ec83-4d39-8b86-c9bddf01d365/Screenshot%202023-09-14%20at%2012.10.11%20PM.png)

*       Example: Imagine a weather prediction model. When predicting tomorrow's temperature, the forget gate assesses if it should disregard yesterday's humidity if it's irrelevant.

**2.3.3.2 Input Gate**: The input gate determines what new information should be stored in the cell state and combines it with the candidate values.

![](https://t9007106573.p.clickup-attachments.com/t9007106573/1a13d9bd-b16c-4ce6-80cc-f2ae1d65b6de/Screenshot%202023-09-14%20at%2012.10.37%20PM.png)

*       Example: In language translation, if you're translating from English to French, the input gate might decide to store French grammatical rules when you encounter them.

  

**2.3.3.3 Update of Cell State**: This step involves updating the old cell state by removing unnecessary information and adding the newly determined information.

![](https://t9007106573.p.clickup-attachments.com/t9007106573/364c79f9-6db4-4cd8-8526-1f1b064a8dc5/Screenshot%202023-09-14%20at%2012.12.32%20PM.png)

*       Example: Think of a stock price prediction model. The cell state updates to keep only the most relevant historical price information while discarding less useful data.

  

  

**2.3.3.4 Output Gate**: The output gate filters the cell state to produce the final output.

![](https://t9007106573.p.clickup-attachments.com/t9007106573/a188bf73-c68e-4289-94b5-4b58d949b9f1/Screenshot%202023-09-14%20at%2012.12.42%20PM.png)

*       Example: In a speech recognition system, the output gate emphasizes the phonemes relevant to the spoken word while suppressing irrelevant ones.