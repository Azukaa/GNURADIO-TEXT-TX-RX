# GNURADIO-TX-RX-TEXT
This project gives a detailed explanation on how to build a Digital transmitter and receiver for transmitting and receiving texts using GNU Radio blocks and python programming based on Pulse amplitude modulation with different pulse shapes. 


**pulse_shapes.py** is the python program that gives different pulse shapes that were implemented in carrying out the simulation.

**text_simulation.grc** is the flow graph created in gnuradio that carries out the simulation.

**text_simulation.py** is the generated python code for the flow graph generated.

From the whole analysis, text was able to be transmitted and received by the receiver with little errors in the presence of noise up to 0.71 in amplitude. The best pulse shape in the whole analysis was proven to be the rrcf.

