import scapy.all as scapy
import pandas as pd
from scapy.layers.inet import IP, TCP, UDP
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import os
import re
import json
from datetime import datetime
import requests

nltk.download('punkt')
nltk.download('stopwords')

THREAT_DATASET_PATH = './archive/cyber-threat-intelligence_all.csv'
API_URL = 'https://metaitcoding.com/b93b0c7645894ce6b193c4fa69454f0/?secretkey=c55d47f942c79e312982f60d1a584b46'

def load_threat_dataset(path):
    try:
        df = pd.read_csv(path)
        if 'Threat' not in df.columns:
            print("Dataset does not contain a 'Threat' column.")
            return None
        return df
    except Exception as e:
        print(f"Error loading threat dataset: {e}")
        return None

def send_threat_notification(ip, threat_id, threat_name):
    data = {
        'ip': ip,
        'threat_id': threat_id,
        'threat_name': threat_name,
        'secretkey': 'c55d47f942c79e312982f60d1a584b46'
    }
    try:
        response = requests.post(API_URL, data=data)
        if response.status_code == 200:
            print("Threat notification sent successfully.")
        else:
            print(f"Failed to send threat notification: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Error sending threat notification: {e}")

def analyze_packet(packet, threat_df, results, threats_results):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        if TCP in packet:
            port_src = packet[TCP].sport
            port_dst = packet[TCP].dport
        elif UDP in packet:
            port_src = packet[UDP].sport
            port_dst = packet[UDP].dport
        else:
            port_src = port_dst = None
        
        analysis_result = {
            'IP Source': ip_src,
            'IP Destination': ip_dst,
            'Protocol': proto,
            'Port Source': port_src,
            'Port Destination': port_dst
        }
        
        results.append(analysis_result)
        
        if threat_df is not None:
            threats = threat_df['Threat'].tolist()
            words = word_tokenize(str(packet))
            filtered_words = [w.lower() for w in words if w.lower() not in stopwords.words('english')]
            freq_dist = FreqDist(filtered_words)
            
            for threat in threats:
                if re.search(threat, str(packet), re.IGNORECASE):
                    threats_results.append({'Threat': threat, 'Packet': str(packet)})
                    send_threat_notification(ip_src, 'unknown_id', threat)

def live_capture(interface, threat_df):
    print(f"Starting live capture on interface {interface}...")
    
    results = []
    threats_results = []
    
    def packet_handler(packet):
        analyze_packet(packet, threat_df, results, threats_results)
    
    try:
        scapy.sniff(iface=interface, prn=packet_handler, store=0)
    except Exception as e:
        print(f"Error during live capture: {e}")
    
    return results, threats_results

def analyze_captured_file(file_path, threat_df):
    print(f"Analyzing captured file: {file_path}")
    
    results = []
    threats_results = []
    
    packets = scapy.rdpcap(file_path)
    for packet in packets:
        analyze_packet(packet, threat_df, results, threats_results)
    
    return results, threats_results

def save_results(timestamp, results, threats_results, capture_file_path=None):
    results_dir = 'results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    folder_path = os.path.join(results_dir, timestamp)
    os.makedirs(folder_path, exist_ok=True)
    
    if capture_file_path:
        capture_file_dest = os.path.join(folder_path, os.path.basename(capture_file_path))
        os.rename(capture_file_path, capture_file_dest)
    
    with open(os.path.join(folder_path, 'packets.json'), 'w') as f:
        json.dump(results, f, indent=4)
    
    with open(os.path.join(folder_path, 'threats.json'), 'w') as f:
        json.dump(threats_results, f, indent=4)

def main():
    print("IoT Network Traffic Analysis")
    
    mode = input("Choose mode (live/capture): ").strip().lower()
    
    threat_df = load_threat_dataset(THREAT_DATASET_PATH)
    
    timestamp = datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
    
    if mode == 'live':
        interface = input("Enter network interface for live capture (e.g., Ethernet, Wi-Fi): ").strip()
        results, threats_results = live_capture(interface, threat_df)
        save_results(timestamp, results, threats_results)
    elif mode == 'capture':
        file_path = input("Enter path to the captured file (e.g., capture.pcap): ").strip()
        if os.path.exists(file_path):
            results, threats_results = analyze_captured_file(file_path, threat_df)
            save_results(timestamp, results, threats_results, file_path)
        else:
            print("File not found.")
    else:
        print("Invalid mode selected. Please choose 'live' or 'capture'.")

if __name__ == '__main__':
    main()
