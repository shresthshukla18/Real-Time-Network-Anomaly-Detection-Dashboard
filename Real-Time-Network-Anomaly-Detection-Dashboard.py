import streamlit as st
import pandas as pd
import random
from datetime import datetime
import pytz
import time

# Multi-country timezones
TIMEZONES = {
    "India": "Asia/Kolkata",
    "USA": "America/New_York",
    "Brazil": "America/Sao_Paulo",
    "China": "Asia/Shanghai",
    "Germany": "Europe/Berlin",
    "Australia": "Australia/Sydney"
}

# Event types
EVENT_TYPES = [
    "Login Attempt", "Malware Alert", "Port Scan", "Data Exfiltration",
    "DDoS Attack", "SQL Injection", "Phishing Email", "Privilege Escalation",
    "Unauthorized Access", "Brute Force Attempt", "Suspicious File Upload"
]

# Critical attack types (always anomalies)
CRITICAL_ATTACKS = {"DDoS Attack", "SQL Injection", "Privilege Escalation"}

# Track source IP frequency
ip_tracker = {}

# Generate one event
def generate_network_event():
    country = random.choice(list(TIMEZONES.keys()))
    tz = pytz.timezone(TIMEZONES[country])
    timestamp = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    
    source_ip = f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"
    destination_ip = f"10.0.{random.randint(0, 255)}.{random.randint(1, 254)}"
    event_type = random.choice(EVENT_TYPES)
    bytes_sent = random.randint(500, 50000)
    
    # Track IP usage
    ip_tracker[source_ip] = ip_tracker.get(source_ip, 0) + 1
    
    # Anomaly detection rules
    anomaly = "Normal"
    if bytes_sent > 40000:
        anomaly = "High Traffic"
    if ip_tracker[source_ip] > 3:
        anomaly = "Repeated Source IP"
    if event_type in CRITICAL_ATTACKS:
        anomaly = "Critical Attack"
    
    return {
        "timestamp": timestamp,
        "country": country,
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "event_type": event_type,
        "bytes_sent": bytes_sent,
        "anomaly_flag": anomaly
    }

# Streamlit UI
st.set_page_config(page_title="Real-Time Network Anomaly Detection", layout="wide")
st.title(" Real-Time Network Anomaly Detection Dashboard")

placeholder = st.empty()
event_log = []

# Live data loop
for _ in range(50):                                                      # For adjusting number of updates
    event = generate_network_event()
    event_log.append(event)
    
    df = pd.DataFrame(event_log)

    with placeholder.container():
        st.subheader("Live Network Events")
        st.dataframe(df, use_container_width=True)

                                                                             # Charts
        col1, col2, col3 = st.columns(3)

        with col1:
            st.bar_chart(df["event_type"].value_counts())

        with col2:
            st.line_chart(df["bytes_sent"])

        with col3:
            st.bar_chart(df["anomaly_flag"].value_counts())

    time.sleep(1)
