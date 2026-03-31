# -Fundamentals-of-AI-and-ML-Evaluated-Course-Project
MOVIR RECOMMENDATION SYSTEM
A simple yet powerful **AI/ML-based Movie Recommendation System** built using Python.
This project suggests movies based on similarity using **Content-Based Filtering**.


Recommends movies based on user input
Uses Machine Learning concepts
Fast and efficient similarity calculation
Clean and scalable dataset structure
Command-line interaction

 How It Works
This project uses **Content-Based Filtering**:
* Movie features (tags) are converted into numerical vectors using **CountVectorizer**
* Similarity between movies is calculated using **Cosine Similarity**
* The system recommends top similar movies

Technologies Used
* Python
* Pandas
* Scikit-learn

 Project Structure

movie-recommendation-system/
│
├── movie_recommender.py   # Main Python file
├── README.md              # Project documentation

 Installation

1. Clone the repository:
git clone https://github.com/PrasajBajpai/-Fundamentals-of-AI-and-ML-Evaluated-Course-Project

2. Navigate to the project folder:
cd movie-recommendation-system

3. Install required libraries:
pip install pandas scikit-learn

Usage

Run the program:
python movie_recommender.py


Then enter a movie name:
Enter a movie name: Avatar

 Example Output
Top Recommendations for 'Avatar':

Avengers  
Interstellar  
Matrix  
Thor  
Iron Man  
Doctor Strange  
Man of Steel  

Objective
To demonstrate the working of a basic **AI-based recommendation system** using machine learning techniques.

 Future Improvements
 Add large real-world dataset (TMDB 5000 movies)
Build a web interface using Streamlit
Include user ratings for better recommendations
Add posters and UI for better experience

 Contributing
Feel free to fork this project and improve it!

License
This project is for educational purposes only.

Author
Prasaj Bajpai
B.Tech CSE | VIT Bhopal
