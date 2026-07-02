[Read me file.txt](https://github.com/user-attachments/files/29599926/Read.me.file.txt)
Project Title:
Facial Recognition Smart Glasses for Visually Challenged People

1. Introduction
This project focuses on developing a wearable assistive system to support visually challenged individuals in recognizing people, understanding their surroundings, and responding to emergency situations. The smart glasses provide real-time audio feedback using facial recognition, distance measurement, text reading through OCR, and an emergency alert system. The system is designed to improve independence, safety, and confidence during daily activities.

2. Software Requirements
• Raspberry Pi 4 Model B
• Camera (Webcam mounted on glasses frame)
• Ultrasonic Sensor (HC-SR04)
• Wired Earphones
• SOS Push Button
• Jumper Wires
• 100 kΩ Resistor
• Power Bank (Type-C power supply)
• Glass frame

3. Hardware Requirements
• Raspberry Pi OS
• Python 3
• OpenCV
• NumPy
• LBPH Face Recognizer
• PyTesseract (OCR)
• Text-to-Speech Engine
• Telegram Bot API

4. Project Files Description
• facerec.txt – Face recognition module
• read.txt – Text reading using OCR
• ultrasonic.txt– Distance measurement using ultrasonic sensor
• sos.txt – Emergency alert system using Telegram

5. Steps to Execute the Project

A. Hardware Setup, Power ON and Remote Access 
    1. Ensure that all hardware components such as the camera, ultrasonic sensor,earphones, and SOS push button are properly        connected to the Raspberry Pi camera mounted on the smart glasses.
    2. Confirm that the micro SD card containing Raspberry Pi OS and all project files is permanently fixed inside the              Raspberry Pi.
    3. Connect the Raspberry Pi to a power bank using a Type-C (C-pin) cable.
    4. Switch ON the power bank to supply power to the Raspberry Pi.
    5. Wait for the Raspberry Pi to complete the booting process.Once booted, ensure that the camera mounted on the glasses         is facing forward and the earphones are properly connected for audio output.
    6. Enable mobile hotspot on the laptop or mobile phone.
    7. Connect the Raspberry Pi to the same hotspot network.
    8. Open the terminal or desktop on the Raspberry Pi and check the IP address assigned to the Raspberry Pi.
    9. Note down the IP address displayed for the active network connection.
    10. Open the RealVNC Viewer application on the laptop.
    11. In RealVNC Viewer, paste the Raspberry Pi IP address into the address bar.
    12. Press Enter to establish a remote connection with the Raspberry Pi.
    13. When prompted, enter the Raspberry Pi username and password to log in.
    14. After successful login, the Raspberry Pi desktop is displayed on the laptop through the RealVNC Viewer.
B. Face Recognition Module (ONLY)
    15. Open the terminal window on the Raspberry Pi desktop using RealVNC.
    16. Navigate to the project directory where the facial recognition program file is stored.
    17. Run the facial recognition program.
    18. After execution, a menu is displayed in the terminal with the following options:
       1 – Train Face
       2 – Recognize Face
       3 – Exit
    19. To train a new face, enter option 1 from the keyboard.
    20. After selecting option 1, the camera is activated and starts capturing facial images of the person.
    21. The system captures approximately 150 face images automatically and stores them in the dataset folder for training           purposes.
    22. Once image capture is completed, the system trains the facial recognition model using the stored images.
    23. After training is finished, end the code program and the system returns to the main menu.
    24. To recognize faces, run the program again and enter option 2 from the keyboard.
    25. After selecting option 2, the camera starts live video capture for recognition.
    26. When a known person appears in front of the camera, the system detects the face, compares it with the trained                dataset, and announces the recognized person’s name through audio output.
    27. To avoid repeated announcements for the same person, a time delay is applied before announcing the name again.
    28. To stop the face recognition process, select option 3 (Exit) from the menu.
C. Distance Measurement Module (Separate Execution)
    26. Open a new terminal window.
    27. Navigate to the project directory.
    28. Run the distance measurement Python program.
    29. The ultrasonic sensor starts measuring the distance between the user and nearby objects.
    30. The measured distance is continuously announced through voice output.
    31. Stop the distance measurement program after testing.
D. OCR Text Reading Module (Separate Execution)
    32. Open a new terminal window.
    33. Navigate to the project directory.
    34. Run the OCR Python program.
    35. Place printed text in front of the camera.
    36. The camera captures the text and the OCR module reads the text aloud through the earphones.
    37. Stop the OCR program after testing.
E. Emergency Alert (SOS) Module (Separate Execution)
    38. Open a new terminal window.
    39. Navigate to the project directory.
    40. Run the SOS Python program.
    41. Press the SOS push button connected to the Raspberry Pi.
    42. An emergency alert message is sent to the predefined contacts using the Telegram bot.
    43. Stop the SOS program after verification.
F. Power OFF
    44. Colse all the tabs and click on shut down . After 2 minutes disconnect the power bank from the Raspberry Pi to power         OFF the system.

6. Project Output
• Successful identification of known individuals with clear audio announcements of recognized face names.
• Accurate measurement of distance to nearby objects using an ultrasonic sensor, with continuous voice-based distance feedback.
• Effective recognition of printed text captured by the camera and conversion of the extracted text into audible speech using OCR.
• Reliable transmission of emergency alert messages to predefined contacts through the Telegram bot when the SOS button is activated.

7. Applications
• Assistive device for visually challenged people
• Social awareness through facial recognition
• Indoor and outdoor navigation assistance
• Emergency safety support

8. Publication
Our research paper for this project has been officially published:
Title: Facial Recognition Smart Glasses for Visually Challenged
Authors: Harshitha R, Sakshi Deshpande, Vaishnavi R, Varshitha D P, Ankitha K S
Journal: International Journal of Engineering Development and Research (IJEDR)
Volume & Issue: Volume 13, Issue 4, December-2025, Paper ID: IJEDR2504651 

10. Developed By : 
Sakshi Deshpande , Vaishnavi R , Varshitha D P and Ankitha K S 

Department: Electronics & Communication Engineering , 
College: GSSS Institute of Engineering & Technology for Women, Mysuru , 
Academic Year: 2025–26
