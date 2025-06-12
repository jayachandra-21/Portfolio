import streamlit as st

# Set page config
st.set_page_config(page_title="Jaya Chandra Goud - Portfolio",page_icon=":mortar_board:", layout="wide")

# Custom dark mode CSS
# Custom CSS to make radio tab names black
st.markdown("""
    <style>
    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #f2f2f2 !important;
    }

    /* Radio label text (tab names) */
    .stRadio > div > label {
        color: black !important;
        font-weight: 600;
        font-size: 16px;
    }

    /* Sidebar heading */
    .css-1d391kg {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)



# Title and contact
st.title("👨‍💻 Abbagouni Jaya Chandra Goud")

# Sidebar for navigation
with st.sidebar:
    st.markdown("""
    <div style='font-size:20px; color:black; font-weight:bold;'>👨‍💻 Abbagouni Jaya Chandra Goud</div>
    <div style='font-size:16px; color:black;'>Software Engineer</div>
    <hr style='border: 1px solid black;'>
    """, unsafe_allow_html=True)

    page = st.radio(
    "🧾 Contents",
    ["👤 Profile", "💼 Experience", "🛠️ Projects", "🧰 Skills", "📬 Contact"],
    index=0
)

if page == "👤 Profile":
    st.markdown("## 👤 About Me")
    st.markdown("""
I'm a passionate **Machine Learning Engineer** with a strong foundation in **Python**, **data preprocessing**, and **model deployment**.  
I specialize in transforming real-world problems into intelligent solutions using **machine learning**, **deep learning**, and modern deployment frameworks like **Streamlit** and **Flask**.

With hands-on experience on:
- Data cleaning,Model building using numpy,pandas, Scikit-learn,Tensorflow,Pytorch.
- Visualisation on matplotlib and Seaborn.
- Model deployment using streamlit and dockor.

I’ve built end-to-end systems that involve:
- **Data cleaning and transformation** using Pandas, NumPy, and OpenCV  
- **Model training** with Scikit-learn, TensorFlow, and PyTorch  
- **Visualization** with Matplotlib and Seaborn  
- **Web deployment** using Streamlit and Docker  
- And collaboration tools like Git for version control

My goal is to continue developing scalable, impactful machine learning applications that bridge the gap between data and decision-making.

I'm always eager to learn, innovate, and contribute to projects that solve meaningful problems in society using AI and data science.
""")

    st.markdown("---")
    st.markdown("## 🎓 Education")
    st.markdown("""
**B.Sc. Electronics Communication and Technology**  
📍 Loyola Academy Degree & PG College  
🗓️ 2021 – 2024  
    """)

    st.markdown("---")
    st.markdown("## 📬 Contact Information")
    st.markdown("""
- **📞 Phone:** 9666069791  
- **📧 Email:** [Chandragoud2105@gmail.com](mailto:Chandragoud2105@gmail.com)  
- **📍 Location:** Hyderabad, India
    """)


elif page == "💼 Experience":
    st.markdown("## 💼 Professional Experience")

    st.markdown("### Software Engineer – Lyros Technologies Pvt. Ltd.")
    st.markdown("📍 Hyderabad, India  🗓️ Feb 2025 – Present")
    st.markdown("""
- Designed and deployed multiple **end-to-end machine learning solutions** including real-time web applications and predictive models.
- Developed a **Used Car Price Prediction** app with data preprocessing (scaling, encoding), trained **RandomForestRegressor**, and deployed using **Streamlit** with live car recommendations.
- Built a deep learning-based **Malaria Detection System** using **CNNs** with **TensorFlow/Keras**, leveraging **OpenCV** for image preprocessing and achieving high classification accuracy.
- Created a **Student Grading System** with role-based access (admin/teacher), **data visualization**, and performance analytics using **Tkinter**, **Pandas**, and **Matplotlib**.
- Skilled in handling the full ML lifecycle: **data acquisition**, **EDA**, **model training**, **evaluation (MAE, R², accuracy, confusion matrix)**, and **deployment**.
- Utilized version control and collaboration tools like **Git**, and containerization tools like **Docker** for reproducibility and scalability.
- Collaborated with cross-functional teams to align technical solutions with business needs, following agile workflows.
""")


# 🛠️ Projects Tab
elif page == "🛠️ Projects":
    st.markdown("### 🔬 Malaria Screening Using Microscopic Images")
    st.markdown("""
- **🎯 Objective:**  
  Built an AI-based malaria detection system using deep learning to classify blood smear images. The aim was to automate and accelerate the diagnostic process in healthcare using image classification.

- **🧰 Tools & Technologies:**  
  **Languages:** Python  
  **Libraries:** OpenCV, TensorFlow, Keras, NumPy  
  **Techniques:** CNNs, Image Preprocessing  
  **Others:** Jupyter Notebook for prototyping
- **🧩 Implementation:**  
  Developed an **image classification model** using **Convolutional Neural Networks (CNNs)** to detect **malaria-infected cells** from microscopic images.  
  Preprocessed the image dataset with **OpenCV** — including **resizing**, **RGB conversion**, and creation of structured **train/test splits** for efficient loading and labeling.  
  Built and trained the model using **TensorFlow** and **Keras**, implementing deep learning techniques such as **dropout**, **batch normalization**, and **ReLU activations** to improve generalization.  
  Evaluated model performance using **accuracy**, **confusion matrix**, and **classification reports**, with visualizations created via **Seaborn** and **Matplotlib**.  
  Achieved **high accuracy** in detecting malaria, demonstrating potential for use in **automated medical diagnostics** with real-world healthcare applications.

    """)

    st.markdown("### 🚗 Used Car Price Prediction Web App")
    st.markdown("""
- **🎯 Objective:**  
  Developed an interactive machine learning web app to predict used car prices based on features like mileage, engine size, brand, and transmission. Helps users estimate accurate car values using ML predictions.

- **🧰 Tools & Technologies:**  
  **Languages:** Python  
  **Libraries:** Scikit-learn, Pandas, NumPy, Joblib  
  **UI & Visualization:** Streamlit, Matplotlib, Seaborn
- **🧩 Implementation:**  
  Developed a **preprocessing pipeline** that included **feature scaling** and **one-hot encoding** for categorical variables.  
  Trained a **RandomForestRegressor** model on cleaned data.  
  Evaluated the model and achieved metrics like **MAE: 890.02**, **R²: 0.84** on the test set (replace with your actual values).  
  Deployed the model using **Streamlit**, creating an **interactive web app** for live predictions.  
  Integrated a **similar car suggestion feature** that displays vehicles close to the selected input using filtering and conditional logic.

    """)

# 🧰 Skills Tab
elif page == "🧰 Skills":
    st.markdown("### Technical Skills")

    st.markdown("#### 🧑‍💻 Programming Languages & Tools")
    st.markdown("""
- 🐍 Python, 🌐 HTML, 🎨 CSS, 🐳 Docker, 🐙 Git
    """)

    st.markdown("#### 📚 Libraries & Frameworks")
    st.markdown("""
- 🤖 Scikit-learn, 🔥 PyTorch, 🧠 TensorFlow, 📊 Pandas, 🧮 NumPy, 📈 Matplotlib, 🌈 Seaborn  
- 🌐 Flask, 📺 Streamlit, 🧾 Natural Language Processing (NLP)
    """)

    st.markdown("#### 📊 Data & Analysis Skills")
    st.markdown("""
- 📘 Data Analysis, 🧹 Data Cleaning, 📉 Machine Learning, 🧪 Model Deployment
    """)
elif page == "📬 Contact":
    st.markdown("## 📬 Get in Touch")
    st.markdown("""
- **📞 Phone:** 9666069791  
- **📧 Email:** [Chandragoud2105@gmail.com](mailto:Chandragoud2105@gmail.com)  
- **📍 Location:** Hyderabad, India  
- **💼 LinkedIn:** www.linkedin.com/in/jaya-chandra-goud-abbagouni-47bbb9313
- **🐙 GitHub:** [github.com/jayachandra-21](https://github.com/jayachandra-21)
""")

    # Download Resume Button
    with open("Jayachandraresume (2).pdf", "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Jayachandraresume (2).pdf",
            mime="application/pdf"
        )

