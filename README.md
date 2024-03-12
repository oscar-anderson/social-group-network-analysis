# Network Analysis of my Social Group

## Project Overview

This project focuses on the analysis of a social network dataset to gain insights into the relationships and dynamics within my own personal social group. The dataset includes information about members of the group (nodes) and their relationships (edges), along with details such as relationship types and strength.

### Dataset

The dataset is stored in a CSV file named `social_circle2.csv` and contains the following columns:

- **source:** The person initiating the relationship.
- **target:** The person receiving or reciprocating the relationship.
- **relationship_type:** The type of relationship (e.g., Family, Spouse, In-law, Acquaintance, Friend, Colleague, Stranger).
- **relationship_strength:** A numerical value representing the strength of the relationship.

I created this dataset myself, to reflect the members of and relationships within my own social circle.

### Script

The Python script `social_network_analysis.py` is responsible for loading the dataset, creating a directed graph using the NetworkX library, visualising the social network, and conducting various analyses. The script is divided into three main functions:

1. **create_graph:** Reads the dataset and creates a directed graph, incorporating nodes and edges with relationship type and strength attributes.

2. **draw_graph:** visualises the social network using matplotlib, with customizable node positions, edge colours based on relationship type, and edge widths based on relationship strength.

3. **analyse_graph:** Provides insights into the social network's characteristics, including network density, degree centrality, in-degree centrality, and betweenness centrality.

### Results

#### Network visualisation

The social network visualisation provides a clear representation of the relationships, distinguishing them by colour and width based on relationship type and strength, respectively.

![Social Network visualisation](/plot/social_network.png)

#### Network Analysis

1. **Network Density:** The overall network density is approximately 73%, indicating a relatively interconnected social structure. A higher density suggests that a significant portion of individuals in the network are connected, fostering a closely-knit social environment.

2. **Top 5 Nodes with Highest Degree Centrality:**
   - **Oscar:** With a degree centrality of 1.86, Oscar has the highest number of direct connections in the network. This indicates that Oscar is a central figure with a broad social circle and numerous relationships.
   - **Christopher:** Similarly, Christopher and Brailen also exhibit high degree centrality, signifying their prominence in the social network.
   - **Emma and Honor:** Emma and Honor have slightly lower degree centrality but are still significant players in the network.

3. **Top 5 Nodes with Lowest In-Degree Centrality:**
   - **Jaccaba and Francis:** Jaccaba and Francis have lower in-degree centrality, suggesting they have fewer incoming relationships compared to others.
   - **Emma, Honor, and Radek:** Emma, Honor, and Radek also appear in this list, indicating that although they have strong relationships, their direct connections are not as extensive.

4. **Top 5 Nodes with Highest Betweenness Centrality:**
   - **Oscar:** Oscar has the highest betweenness centrality, indicating that he plays a crucial role in connecting different parts of the network. Oscar may act as a bridge between individuals or groups, influencing the flow of information.
   - **Radek, Christopher, and Brailen:** These individuals also have notable betweenness centrality, suggesting that they serve as important connectors within the social network.
   - **Emma:** Emma, despite having lower betweenness centrality, still contributes to connecting different parts of the network.

These results provide valuable insights into the central nodes, influential individuals, and potential bridge nodes in the social network, shedding light on the structure and dynamics of the social circle.

## How to Use

1. Ensure that you have Python installed on your system.
2. Install the required libraries using `pip install pandas networkx matplotlib`.
3. Download the script and dataset.
4. Update the `data_path` variable in the script to the correct path of your dataset.
5. Run the script using `python social_network_analysis.py`.

Feel free to customise the script and visualisation parameters based on your specific dataset and analysis goals.
