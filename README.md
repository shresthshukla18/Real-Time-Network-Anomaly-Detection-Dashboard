# Real-Time-Network-Anomaly-Detection-Dashboard
A cloud-based system that monitors live network traffic, detects cyber threats using machine learning, and displays real-time results on an interactive dashboard. It ensures scalable, automated, and intelligent anomaly detection to enhance network security and response efficiency.

Overview: The Real-Time Network Anomaly Detection Dashboard is a cloud-based intelligent monitoring system that detects unusual network behavior in real-time using machine learning. It helps administrators identify potential cyber threats, visualize network traffic, and respond quickly through a dynamic dashboard interface.

Objectives: 
            
            Detect real-time network anomalies using ML models.

            Visualize live network traffic and anomaly patterns.

            Ensure scalable and automated monitoring via cloud deployment.

            Improve detection accuracy and reduce response time.

System Architecture:

             Data Collection: Captures live packets from routers, firewalls, or logs.

             Preprocessing: Extracts features (IP, ports, bytes, protocol, etc.).

             Anomaly Detection: Uses ML models like Isolation Forest or Autoencoder.

             Storage: Saves results to cloud databases (AWS S3 / MongoDB).

             Visualization: Displays metrics, alerts, and charts on a web dashboard.

| Category             | Tools                          |
| -------------------- | ------------------------------ |
| **Language**         | Python                         |
| **Data Processing**  | Pandas, NumPy, Scapy           |
| **Machine Learning** | Scikit-learn, TensorFlow       |
| **Streaming**        | Apache Kafka / Spark Streaming |
| **Database**         | MongoDB / Firebase             |
| **Dashboard**        | Plotly Dash / Streamlit        |
| **Cloud**            | AWS / GCP / Azure              |
| **Containerization** | Docker                         |



Features:

        Real-time traffic monitoring

        AI-based anomaly detection

        Cloud-hosted for scalability

        Interactive dashboard visualization

        Automatic alert system for anomalies


Installation:

        # Clone repository
        git clone https://github.com/yourusername/real-time-anomaly-dashboard.git
        cd real-time-anomaly-dashboard

        # Install dependencies
        pip install --upgrade pip
        pip install -r requirements.txt 

        # requirements.txt
        streamlit==1.38.0
        pandas==2.2.2
        numpy==1.26.4
        pytz==2024.1

        # alternative for dependencies
        pip install --upgrade pip
        pip install streamlit pandas numpy pytz


        # Run the dashboard
        streamlit run Network_Anomaly_Detector_Streamlit.py


Output: 

         Live graphs of packet flow and anomaly trends

         Alerts with timestamps and IP details

         Cloud-stored reports for later review


<img width="1919" height="1079" alt="Screenshot 2025-10-16 232601" src="https://github.com/user-attachments/assets/32482384-aa5a-44d9-a029-f23b7159b6ba" />
