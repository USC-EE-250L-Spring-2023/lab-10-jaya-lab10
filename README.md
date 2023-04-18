# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Jaya Travis 


## Lab Question Answers

Question 1: Under what circumstances do you think it will be worthwhile to offload one or both of the processing tasks to your PC? And conversely, under what circumstances will it not be worthwhile?

Answer: Offloading processing tasks to a PC can be beneficial in certain circumstances, such as when the PC has more processing power and memory than the device running the application, offloading tasks to the PC can improve the overall application performance and responsiveness or when the PC has specialized hardware, such as a GPU or FPGA, that can accelerate specific processing tasks, offloading those tasks to the PC can significantly speed up the processing. Conversely, it is not optimal when the PC is not available or is being used for other tasks, offloading processing tasks to the PC may not be possible or when the processing tasks are relatively simple or do not require significant computational resources, offloading tasks to the PC may not provide significant performance benefits.

Question 2: Why do we need to join the thread here?

Answer: We need to join the thread because it synchronizes the execution of multiple threads and ensure that the main program waits for the thread for process 1 to finish its task before continuing with its another execution.

Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?

Answer: The processing functions are executing concurrently as the processes are executed independently.The difference between concurrent and parallel processing is that concurrent processing involves executing multiple tasks or processes simultaneously, while parallel processing involves executing them truly in parallel, with each task using its own processing resources.

Question 4: What is the best offloading mode? Why do you think that is?

Answer: Process 2 has the fastest makespan out of the four groups as the process has the simplest and faster computation than all.

Question 5: What is the worst offloading mode? Why do you think that is?
Answer: The both condition was the worst in offloading mode as it ran through both process 1 and process 2 in order to compile. 

Question 6: The processing functions in the example aren't very likely to be used in a real-world application. What kind of processing functions would be more likely to be used in a real-world application?

Answer: Model training and optimization functions that include various algorithms such as linear regression, logistic regression, decision trees, random forests, and deep learning models like convolutional neural networks (CNN) and recurrent neural networks (RNN) are examples of function used in real-world application.

When would you want to offload these functions to a server?

Answer: Offloading processing functions to a server can provide several benefits in terms of scalability, security, reliability, and performance, particularly in scenarios where the client-side device has limited resources or requires high-speed network access.
