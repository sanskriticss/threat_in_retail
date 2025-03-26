# Threat Detection in Retail Stores

## Overview
The Threat Detection ML model is designed to identify potential threats in retail store environments using advanced computer vision and deep learning techniques. The model analyzes surveillance footage in real time, detecting suspicious activities, such as weapon detection, aggressive behavior, or unauthorized access.

## Features
- **Real-time Monitoring**: Continuously processes live video feeds for immediate threat identification.
- **Weapon Detection**: Recognizes firearms, knives, and other potential weapons.
- **Behavior Analysis**: Detects suspicious or aggressive movements and actions.

## Model Architecture
The model utilizes a deep learning approach with a **YOLO (You Only Look Once)**for object detection (e.g., weapons, unauthorized individuals).

## Data Collection
- **Dataset Used**: The model is trained using the **Anomaly Detection Dataset UCF** from Kaggle.
- **Filtering Process**: Only videos relevant to retail store environments were selected.
- **Classes Identified**:
  - Assault
  - Fighting
  - Gun
  - Knife
  - Vandalism
- **Data Preprocessing**:
  - Extracted frames from videos.
  - Applied augmentation techniques such as scaling, flipping, noise injection, and occlusion.
  - Labeled and annotated frames accordingly.

## Model Training
- **Preprocessing**: Frame extraction, resizing, normalization, and annotation.
- **Training Pipeline**:
  - Supervised learning using labeled threat scenarios.
  - Fine-tuning with retail-specific filtered data from the dataset.
  - Transfer learning from pre-trained models to enhance performance.
- Evaluation Metrics:

Dataset: 75 images, 75 instances

Precision: 0.91

Recall: 0.733

mAP@50: 0.772

mAP@50-95: 0.372

## Deployment Status
- **Future Plans**: Potential deployment and integration with retail security systems.


## Conclusion
This ML-based threat detection system provides enhanced security for retail stores by leveraging real-time video analysis. While currently in the training phase, future deployments and integrations will further increase efficiency and safety in retail environments.

