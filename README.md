The proposed project, PathSense, focuses on developing a multi-objective route optimization system that provides efficient and customizable navigation solutions. Unlike traditional routing systems that prioritize only a single factor such as distance or time, this system incorporates multiple parameters including distance, travel time, and congestion level.
The system models a road network as a weighted graph where nodes represent intersections and edges represent roads with associated attributes. A modified shortest-path algorithm based on Dijkstra’s approach is implemented to calculate optimal routes using a dynamic cost function. This cost function combines multiple parameters using user-defined weights, enabling flexible route selection based on different scenarios such as shortest, fastest, or emergency routing.
The project aims to provide transparency and adaptability in route planning while maintaining computational efficiency. The system is being developed in C++ using standard libraries and simulated datasets for testing. The final outcome will demonstrate how multi-objective optimization improves decision-making in real-world transportation scenarios.
The system follows a modular and scalable architecture. The road network is represented as a weighted graph using adjacency lists, where each edge contains attributes such as distance, travel time, and congestion level.
The core algorithm is a modified version of Dijkstra’s algorithm, where instead of a single weight, a dynamic cost function is used:
Cost = w1 × distance + w2 × time + w3 × congestion
User-defined weights (w1, w2, w3) allow customization of routing priorities. The implementation is done in python using STL components such as priority queues and vectors for efficient computation.
The system consists of the following modules:
•	Graph Construction Module 
•	Optimization Engine 
•	User Input Handler 
•	Output/Visualization Module 
Currently, simulated datasets are used for testing different routing scenarios. The architecture ensures flexibility for future extensions like real-time data integration.

